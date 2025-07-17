#  PakWheels ETL Pipeline – Scalable Web Scraping & Data Processing

This project builds an end-to-end ETL pipeline to scrape, clean, and process vehicle listings from **PakWheels.com**, using a modern data engineering stack. It combines **Selenium** for web scraping, **PySpark** for big data processing, **Apache Airflow** for task orchestration, and **Docker** for containerization.

The goal: turn raw, unstructured web data into clean, analysis-ready datasets for automotive insights and modeling.


##  Tech Stack

-  **Selenium** – For dynamic scraping of vehicle listings  
-  **Apache Airflow** – For scheduling and orchestrating ETL tasks  
-  **PySpark** – For scalable data transformation and cleaning  
-  **Docker** – For containerizing the entire workflow  
-  **CSV / Parquet Output** – Clean datasets for downstream use

---

##  Workflow Overview

1. **Scraping:**  
   Selenium script dynamically scrapes car listing data from PakWheels (price, brand, year, engine, mileage, location, etc.)

2. **ETL Scheduling:**  
   Airflow DAG schedules the scraping, transformation, and loading tasks to run on a defined frequency.

3. **Transformation:**  
   PySpark processes and cleans the raw data—handling nulls, types, price formats, duplicate listings, etc.

4. **Export:**  
   Final cleaned dataset is saved in CSV/Parquet format for use in dashboards or ML models.

---

## 🔍 Key Features

- Scrapes real-time listings from PakWheels using Selenium  
- Cleans and structures messy scraped data using PySpark  
- Task automation with Airflow DAGs (fully scheduled + monitored)  
- Dockerized pipeline for easy deployment and scalability  
- Output ready for dashboarding, analytics, or machine learning

---

##  Folder Structure
pakwheels-etl/
├── airflow/
│ └── dags/
│ └── pakwheels_etl_dag.py
├── docker/
│ ├── Dockerfile
│ └── requirements.txt
├── scraper/
│ └── pakwheels_scraper.py
├── spark_jobs/
│ └── clean_transform.py
└── output/
└── cleaned_data.csv


---

##  How to Run

1. Clone the repo  
2. Build Docker containers  
3. Launch Airflow with Docker Compose  
4. Trigger DAG or schedule run  
5. Cleaned data will appear in `/output` folder

---

##  Sample Use Cases

- Build a Power BI dashboard on market trends by city, brand, price range  
- Train an ML model to predict resale value based on features  
- Analyze market demand for different car types over time

---

##  Contact

**Muhammad Abdullah Sheikh**  
📧 abdullahsheeikh.638@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-abdullah-sheikh) | [GitHub](https://github.com/yk-Abdullah)


