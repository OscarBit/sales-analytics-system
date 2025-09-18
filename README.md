
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
## 🚀 Running the Project on your Machine

Because this project is fully containerized with Docker, setting it up on a new computer is simple and reliable. The Docker environment handles all dependencies, so you don't need to install Python, Node.js, or PostgreSQL locally.

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


### 💡 Tips & Troubleshooting

* **"Unable to Connect" Error?** This usually means a container isn't running. Check the status of all services with `docker-compose ps`. If a service has `Exited`, check its specific logs for an error message, e.g., `docker-compose logs frontend`.

* **Need a Fresh Start?** To completely stop and reset the entire application, including deleting the database data, run `docker-compose down -v`. The `-v` flag is important as it removes the database volume, ensuring a perfectly clean start on your next `docker-compose up`.

* **JupyterLab Access Token:** To log in to JupyterLab for the first time, you'll need a security token. You can find it by checking the logs of the notebook service: `docker-compose logs notebook`.

* **No Local `npm` or `python` Needed:** Remember that you don't need to install any programming languages on your computer. To run commands inside a container, use `docker-compose exec <service_name> <command>`.

---

## Key Technical Decisions

* **Fully Containerized Development:** Using Docker for all services ensures a consistent, isolated, and easily reproducible environment, eliminating "it works on my machine" issues.
* **Dedicated Analytics API:** Instead of fetching raw data, the backend provides pre-aggregated endpoints (`/api/analytics/...`). This shifts the heavy computational load to the server, resulting in a significantly faster and more responsive frontend dashboard.
* **Optimized Data Ingestion:** The `load_sales_data` command uses `pandas` chunking and Django's `bulk_create` to efficiently load a large dataset without overwhelming the server's memory.
* **Containerized Frontend with Vite:** The React development environment is also containerized, removing the need for local Node.js/npm installation. Vite was chosen for its modern architecture and extremely fast development server.
* **Separation of Concerns:** The project is clearly divided into a backend API, a frontend UI, and a data analysis notebook, each serving a distinct purpose.

---
