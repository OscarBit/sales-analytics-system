import pandas as pd
from faker import Faker
import random
import uuid

# --- Configuration ---
NUM_ROWS = 300000
FILE_NAME = "sales_data.csv"

# Initialize Faker for data generation
fake = Faker()

# --- Predefined realistic data pools ---
# To make data more realistic, we'll choose from predefined lists
product_categories = ["Electronics", "Clothing", "Home Goods", "Books", "Sports"]
product_names = {
    "Electronics": ["Laptop", "Smartphone", "Headphones", "Smartwatch"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
    "Home Goods": ["Coffee Maker", "Blender", "Lamps", "Towels"],
    "Books": ["Fiction Novel", "Biography", "Science Journal", "Cookbook"],
    "Sports": ["Yoga Mat", "Dumbbells", "Basketball", "Running Shoes"],
}
regions = ["North", "South", "East", "West"]
sellers = [fake.name() for _ in range(10)]  # Pool of 10 unique sellers


# --- Data Generation Function ---
def generate_sales_data(num_rows):
    print(f"Generating {num_rows} rows of sales data...")
    data = []
    for _ in range(num_rows):
        category = random.choice(product_categories)
        product = random.choice(product_names[category])

        sale = {
            "SaleID": str(uuid.uuid4()),
            "SaleDate": fake.date_time_between(start_date="-2y", end_date="now"),
            "ProductName": product,
            "ProductCategory": category,
            "CustomerName": fake.name(),
            "CustomerEmail": fake.email(),
            "CustomerRegion": random.choice(regions),
            "SaleAmount": round(random.uniform(10.50, 899.99), 2),
            "SellerName": random.choice(sellers),
        }
        data.append(sale)

    print("Data generation complete.")
    return data


# --- Main Execution ---
if __name__ == "__main__":
    sales_data = generate_sales_data(NUM_ROWS)

    print(f"Converting to DataFrame and saving to {FILE_NAME}...")
    df = pd.DataFrame(sales_data)

    # Ensure SaleDate is in a consistent format
    df["SaleDate"] = pd.to_datetime(df["SaleDate"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    df.to_csv(FILE_NAME, index=False)
    print("Script finished successfully.")
