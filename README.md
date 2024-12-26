# E-Commerce Analytics Pipeline

## Project Overview
This project implements a scalable data pipeline for real-time analytics on e-commerce transaction data. The pipeline simulates real-time data ingestion, processes the data, stores it in a database, and provides APIs and a dashboard for analytics.

### Key Features
- **Data Ingestion**: Real-time ingestion of transaction data using Kafka.
- **Data Processing**: Transformation and storage of data in PostgreSQL.
- **APIs**: RESTful APIs for querying analytics.
- **Dashboard**: A Streamlit-based dashboard for visualizing analytics.
- **Scalable Design**: Supports real-time and batch processing.

---

## File Structure
```plaintext
ecommerce_pipeline/
├── data_ingestion/        # Data ingestion logic
│   ├── producer.py        # Simulates and sends transaction data to Kafka
├── data_processing/       # Data processing and ETL
│   ├── consumer.py        # Consumes, transforms, and stores data in PostgreSQL
├── database/              # Database management
│   ├── init_db.sql        # SQL script to create tables
│   └── db_config.py       # Database connection helper
├── backend_api/           # Backend APIs for querying analytics
│   ├── api.py             # FastAPI application for analytics
├── dashboard/             # Visualization layer
│   ├── dashboard.py       # Streamlit-based analytics dashboard
├── config/                # Configuration files
│   ├── settings.yaml      # Centralized configuration
├── docker/                # Docker setup
│   ├── docker-compose.yml # Multi-container setup for Kafka, PostgreSQL, etc.
│   ├── Dockerfile         # Dockerfile for backend services
├── README.md              # Project overview and instructions
```

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker & Docker Compose
- Streamlit (for dashboard)
- PostgreSQL
- Kafka (via Docker)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd ecommerce_pipeline
```

### Step 2: Start Services Using Docker Compose
```bash
docker-compose up -d
```
- **Kafka**: Starts at `localhost:9092`
- **PostgreSQL**: Starts at `localhost:5432`

### Step 3: Set Up the Database
1. Access the PostgreSQL database:
   ```bash
   psql -h localhost -U postgres -d postgres
   ```
2. Run the SQL script to initialize tables:
   ```bash
   \\i database/init_db.sql
   ```

### Step 4: Install Python Dependencies
Navigate to each module folder and install dependencies.
```bash
pip install -r requirements.txt
```
Repeat for `data_ingestion/`, `data_processing/`, `backend_api/`, and `dashboard/`.

### Step 5: Run Each Module
#### 1. Start the Kafka Producer:
```bash
python data_ingestion/producer.py
```
#### 2. Start the Kafka Consumer:
```bash
python data_processing/consumer.py
```
#### 3. Run the FastAPI Backend:
```bash
uvicorn backend_api.api:app --reload
```
Access the APIs at `http://127.0.0.1:8000`.
#### 4. Run the Streamlit Dashboard:
```bash
streamlit run dashboard/dashboard.py
```
Access the dashboard at `http://localhost:8501`.

---

## API Endpoints

### 1. **Get Total Revenue**
**Endpoint**: `/analytics/revenue`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "total_revenue": 150000
  }
  ```

### 2. **Get Top Products**
**Endpoint**: `/analytics/top-products`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "top_products": [
          {"product_id": 1, "sales": 500},
          {"product_id": 2, "sales": 300}
      ]
  }
  ```

---

## Example Outputs

### Total Revenue
- Displayed on the dashboard as a metric.

### Top-Selling Products
- Visualized in a table or bar chart on the dashboard.

---

## Future Improvements
1. **Scalability**:
   - Add horizontal scaling for Kafka consumers.
   - Use distributed processing frameworks like Apache Spark.
2. **Advanced Analytics**:
   - Add customer segmentation and predictive analytics.
   - Incorporate machine learning models.
3. **Deployment**:
   - Deploy on cloud platforms like AWS or GCP using Kubernetes.

---

## Contributors
- Vidit Roy

