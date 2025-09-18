
# Sales Analysis System - Technical Test

This project is a full-stack web application designed to analyze and visualize sales data. It features a Django backend with a REST API, a PostgreSQL database, a data analysis environment with Jupyter, and a dynamic React frontend dashboard. The entire application is containerized using Docker for easy setup and consistent deployment.

---

## Features

* **Containerized Environment:** The entire stack (Backend, Frontend, Database, Analysis) runs in Docker containers for seamless setup.
* **REST API:** A robust API built with Django REST Framework provides paginated and filterable access to the sales data.
* **Optimized Analytics Endpoints:** Dedicated, pre-aggregated API endpoints for high-performance dashboard loading.
* **Bulk Data Ingestion:** An optimized custom Django command to load large CSV datasets (300,000+ rows) efficiently.
* **Data Analysis Notebook:** A JupyterLab environment for exploratory data analysis and visualization.
* **Interactive React Dashboard:** A dynamic frontend built with React and Vite, featuring several charts and interactive filters (by date and region).

---

## Technology Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** React, Vite, Chart.js, Axios
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose
* **Data Analysis:** JupyterLab, Pandas, Matplotlib, Seaborn

---

## Installation & Execution

### Prerequisites

* [Docker](https://www.docker.com/products/docker-desktop/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Step-by-Step Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd sales_analysis_system
    ```

2.  **Set Up Environment Variables:**
    Copy the example environment file and fill in your unique `SECRET_KEY`. You can generate one easily online.
    ```bash
    cp env.example .env
    ```
    *Now, open the `.env` file and add your secret key.*

3.  **Build and Run the Containers:**
    This command will build the images and start all services (Django, React, PostgreSQL, Jupyter) in the background.
    ```bash
    docker-compose up -d --build
    ```

4.  **Generate Sample Data:**
    Run the provided script to generate the `sales_data.csv` file (Note: this file is not committed to Git).
    ```bash
    python generate_sales_data.py
    ```

5.  **Load Data into the Database:**
    Execute the custom Django command to load the 300,000 sales records into the database.
    ```bash
    docker-compose exec web python manage.py load_sales_data
    ```

6.  **Access the Applications:**
    * **Web Dashboard (React):** [http://localhost:5173/](http://localhost:5173/)
    * **Backend API (Django):** [http://localhost:8000/api/](http://localhost:8000/api/)
    * **Data Analysis (JupyterLab):** [http://localhost:8888/](http://localhost:8888/)
        * *(Note: You'll need to get the access token from the Jupyter container's logs: `docker-compose logs notebook`)*

---

## Key Technical Decisions

* **Fully Containerized Development:** Using Docker for all services ensures a consistent, isolated, and easily reproducible environment, eliminating "it works on my machine" issues.
* **Dedicated Analytics API:** Instead of fetching raw data, the backend provides pre-aggregated endpoints (`/api/analytics/...`). This shifts the heavy computational load to the server, resulting in a significantly faster and more responsive frontend dashboard.
* **Optimized Data Ingestion:** The `load_sales_data` command uses `pandas` chunking and Django's `bulk_create` to efficiently load a large dataset without overwhelming the server's memory.
* **Containerized Frontend with Vite:** The React development environment is also containerized, removing the need for local Node.js/npm installation. Vite was chosen for its modern architecture and extremely fast development server.
* **Separation of Concerns:** The project is clearly divided into a backend API, a frontend UI, and a data analysis notebook, each serving a distinct purpose.

---
