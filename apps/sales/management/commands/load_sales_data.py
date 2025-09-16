import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from apps.sales.models import Customer, Seller, Product, Sale


class Command(BaseCommand):
    help = "Loads sales data from a CSV file into the database using optimized bulk operations"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Starting data load process...")

        # --- Optimization 1: Pre-fetch existing data into memory (caches) ---
        self.stdout.write("Caching existing Customers, Sellers, and Products...")
        customers = {c.email: c for c in Customer.objects.all()}
        sellers = {s.name: s for s in Seller.objects.all()}
        products = {(p.name, p.category): p for p in Product.objects.all()}

        # Keep track of objects created in this run to avoid DB hits
        new_sales_to_create = []

        # --- Optimization 2: Use pandas to read the CSV in memory-efficient chunks ---
        chunk_size = 10000
        file_path = "sales_data.csv"

        self.stdout.write(f"Reading {file_path} in chunks of {chunk_size}...")

        for chunk_df in pd.read_csv(file_path, chunksize=chunk_size, iterator=True):
            for index, row in chunk_df.iterrows():
                # --- Get or Create related objects using the in-memory caches ---

                # Customer
                customer_email = row["CustomerEmail"]
                if customer_email not in customers:
                    customers[customer_email] = Customer.objects.create(
                        name=row["CustomerName"],
                        email=customer_email,
                        region=row["CustomerRegion"],
                    )
                customer = customers[customer_email]

                # Seller
                seller_name = row["SellerName"]
                if seller_name not in sellers:
                    sellers[seller_name] = Seller.objects.create(name=seller_name)
                seller = sellers[seller_name]

                # Product
                product_key = (row["ProductName"], row["ProductCategory"])
                if product_key not in products:
                    products[product_key] = Product.objects.create(
                        name=row["ProductName"], category=row["ProductCategory"]
                    )
                product = products[product_key]

                # --- Prepare Sale object for bulk creation (don't save yet) ---
                sale = Sale(
                    sale_id=row["SaleID"],
                    customer=customer,
                    seller=seller,
                    product=product,
                    sale_amount=row["SaleAmount"],
                    sale_date=row["SaleDate"],
                )
                new_sales_to_create.append(sale)

            # --- Optimization 3: Bulk create the sales in batches ---
            Sale.objects.bulk_create(new_sales_to_create)
            self.stdout.write(
                f"Loaded {len(new_sales_to_create)} sales records from a chunk."
            )
            new_sales_to_create = []  # Clear the list for the next chunk

        self.stdout.write(
            self.style.SUCCESS("Data loading process completed successfully!")
        )
