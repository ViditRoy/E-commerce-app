# E-Commerce Analytics Pipeline

## Overview
A scalable data pipeline for real-time analytics on e-commerce transactions. It ingests, processes, stores, and visualizes data, providing RESTful APIs and a dashboard.

## Features
- **Real-Time Data Ingestion**: Simulated using Kafka.
- **Data Processing**: Transformation and storage in PostgreSQL.
- **APIs**: Expose analytics via FastAPI.
- **Dashboard**: Real-time insights using Streamlit.

## File Structure
```plaintext
ecommerce_pipeline/
├── data_ingestion/        # Kafka producer for transaction data
├── data_processing/       # Consumer for ETL and database storage
├── database/              # SQL scripts and DB connection
├── backend_api/           # FastAPI for analytics endpoints
├── dashboard/             # Streamlit dashboard
├── docker/                # Docker Compose setup
├── config/                # Configuration files
```

## Setup

### Prerequisites
- Python 3.9+
- Docker & Docker Compose

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ecommerce_pipeline
   ```
2. Start Kafka and PostgreSQL:
   ```bash
   docker-compose up -d
   ```
3. Initialize the database:
   ```bash
   psql -h localhost -U postgres -d postgres -f database/init_db.sql
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Repeat for all modules.
5. Run the pipeline:
   - **Producer**: `python data_ingestion/producer.py`
   - **Consumer**: `python data_processing/consumer.py`
   - **API**: `uvicorn backend_api.api:app --reload`
   - **Dashboard**: `streamlit run dashboard/dashboard.py`

## API Endpoints
- `/analytics/revenue`: Total revenue.
- `/analytics/top-products`: Top-selling products.

## Contributors
- Vidit Roy

