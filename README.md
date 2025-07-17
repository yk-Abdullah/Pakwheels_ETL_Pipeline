# 🚗 PakWheels ETL Pipeline

A real-time data pipeline for extracting, transforming, and loading classified car listings from PakWheels.com using Kafka, Spark, PostgreSQL, and Apache Airflow.

## 📁 Project Structure

```
PakWheels-ETL-Pipeline/
├── dags/                  <- Airflow DAGs for orchestrating ETL flow
├── producer/              <- Kafka producer for pushing scraped listings
├── spark/                 <- Spark scripts for real-time data processing
├── sql/                   <- SQL scripts for database initialization
├── utils/                 <- Utility scripts (data cleaning, helpers)
├── logs/                  <- Log outputs
├── docker-compose.yml     <- Docker-based orchestration for full stack
├── requirements.txt       <- Python dependencies
├── .env                   <- Environment variable configuration
└── README.md              <- Project documentation
```

## 🏗️ System Architecture

- **Kafka Producer**: Web scrapes listings and streams to Kafka topic.
- **Spark Streaming**: Consumes Kafka stream, transforms and validates data.
- **PostgreSQL**: Stores the cleaned and enriched listings.
- **Airflow**: Manages the workflow with DAGs to automate ETL steps.

## 📦 Dataset Overview

Fields included:
- Car Make & Model
- Year
- Price
- Location
- Mileage
- Engine Type
- Transmission

## 🔄 ETL Workflow

1. **Extract**: Scrape listings using a Kafka producer.
2. **Transform**: Normalize and clean data using Spark.
3. **Load**: Save clean data to PostgreSQL.

## 📊 Monitoring & Dashboards

While visualization is not part of this repo, PostgreSQL is ready to be connected to Superset or Metabase. Optionally, Streamlit can be integrated.

## ⚙️ Deployment

### Step 1: Run services
```bash
docker-compose up --build
```

### Step 2: Access Airflow UI
```
URL: http://localhost:8080
Username: airflow
Password: airflow
```

## ✅ Features

- Real-time Kafka streaming
- Spark-based data transformation
- PostgreSQL data storage
- Apache Airflow orchestration
- Docker-based deployment

## 🔧 Configuration

- `.env`: Environment variables for DB, Kafka
- `docker-compose.yml`: All services defined here
- `requirements.txt`: Python dependencies

## 🚀 Future Work

- Add dashboards using Superset
- Cloud deployment (AWS EC2 + RDS + MSK)
- Data deduplication
- Scheduled historical reprocessing

---

© 2025 PakWheels ETL Project - For educational and development use.