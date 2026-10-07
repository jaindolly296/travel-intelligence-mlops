# ✈️ Travel Intelligence MLOps

> **An End-to-End Production Ready MLOps System for Flight & Hotel Price Prediction**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-orange)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-purple)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Project Overview

Travel Intelligence MLOps is an end-to-end machine learning system that predicts:

- ✈️ Flight Ticket Prices
- 🏨 Hotel Booking Costs

The project follows a production-style MLOps workflow that includes data preprocessing, feature engineering, model training, experiment tracking, REST APIs, interactive dashboards, workflow orchestration, containerization, and CI/CD.

---

# Key Features

- Flight Price Prediction
- Hotel Price Prediction
- Automated Data Pipeline
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- MLflow Experiment Tracking
- FastAPI REST API
- Streamlit Web Application
- Apache Airflow Workflow
- Docker Containerization
- Docker Compose
- Jenkins CI/CD Pipeline
- Environment Variable Configuration
- Centralized Logging

---

# Tech Stack

### Programming

- Python 3.11

### Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

### MLOps

- MLflow
- Apache Airflow
- Docker
- Docker Compose
- Jenkins

### Backend

- FastAPI

### Frontend

- Streamlit

### Database

- PostgreSQL

### Version Control

- Git
- GitHub

---

# Project Architecture

```text
GitHub
    │
    ▼
Jenkins CI/CD
    │
    ▼
Docker
    │
    ▼
Airflow Pipeline
    │
    ▼
Data Pipeline
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
MLflow Tracking
    │
    ▼
FastAPI
    │
    ▼
Streamlit

---

# 📂 Project Structure

```text
travel-intelligence-mlops/
│
├── api/
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── app/
│   ├── app.py
│   ├── views/
│   ├── utils/
│   └── styles/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── artifacts/
│
├── logs/
│
├── notebooks/
│
├── requirements/
│
├── src/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── pipeline/
│   ├── utils/
│   ├── exception.py
│   └── logger.py
│
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.api
├── Dockerfile.airflow
├── Dockerfile.mlflow
├── Jenkinsfile
├── README.md
└── .env
---

# 🔄 End-to-End Workflow

```text
Raw Data
     │
     ▼
Data Validation
     │
     ▼
Data Transformation
     │
     ▼
Feature Engineering
     │
     ▼
Train/Test Split
     │
     ▼
Model Training
     │
     ▼
Hyperparameter Tuning
     │
     ▼
Model Evaluation
     │
     ▼
MLflow Tracking
     │
     ▼
Save Best Model
     │
     ▼
FastAPI
     │
     ▼
Streamlit

---

# 🚀 CI/CD Pipeline

```text
Developer

     │

     ▼

GitHub Repository

     │

     ▼

Jenkins Pipeline

     │

     ▼

Install Dependencies

     │

     ▼

Run ML Pipeline

     │

     ▼

Build Docker Images

     │

     ▼

Pipeline Success

---

# 🌬 Airflow Pipeline

```text
Start Pipeline
      │
      ▼
Data Pipeline
      ▼
Flight Model Training
      ▼
Hotel Model Training
      ▼
Finish Pipeline

---

# ⭐ Features

- End-to-End MLOps Pipeline
- Flight Price Prediction
- Hotel Cost Prediction
- Automated Data Validation
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- MLflow Experiment Tracking
- REST API using FastAPI
- Interactive Streamlit Dashboard
- Apache Airflow Orchestration
- Jenkins CI/CD
- Docker Containerization
- Docker Compose
- PostgreSQL Integration
- Environment Variable Management
- Centralized Logging
---

# ⭐ Features

- End-to-End MLOps Pipeline
- Flight Price Prediction
- Hotel Cost Prediction
- Automated Data Validation
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- MLflow Experiment Tracking
- REST API using FastAPI
- Interactive Streamlit Dashboard
- Apache Airflow Orchestration
- Jenkins CI/CD
- Docker Containerization
- Docker Compose
- PostgreSQL Integration
- Environment Variable Management
- Centralized Logging
---

# 📡 REST API

## Home

```
GET /
```

Returns project information.

---

## Health Check

```
GET /health
```

Returns API health status.

---

## Flight Prediction

```
POST /predict
```

Example Request

```json
{
  "gender":"male",
  "age":30,
  "age_group":"Adult",
  "company_frequency":120,
  "company":"Umbrella LTDA",
  "from_city":"Brasilia (DF)",
  "to_city":"Rio de Janeiro (RJ)",
  "flight_type":"economic",
  "time":540,
  "distance":1150,
  "travel_year":2026,
  "travel_month":8,
  "travel_day":2,
  "travel_weekday":"Sunday",
  "is_weekend":1
}
```

---

## Hotel Prediction

```
POST /predict/hotel
```

Example Request

```json
{
  "name":"Hotel Example",
  "place":"Rio de Janeiro (RJ)",
  "stay_weekday":"Sunday",
  "days":3,
  "stay_year":2026,
  "stay_month":8,
  "stay_day":2
}
---

# 🐳 Docker

Build all services

```bash
docker compose build
```

Start all services

```bash
docker compose up
```

Stop all services

```bash
docker compose down
```

Rebuild containers

```bash
docker compose up --build

---


# 🚀 Future Enhancements

- MLflow Model Registry
- Kubernetes Deployment
- Cloud Deployment (AWS / Azure)
- Automated Monitoring
- Model Drift Detection
- Authentication & Authorization
- Real-time Prediction Service

---

# 👨‍💻 Author

**Dolly Jain**

- GitHub: https://github.com/jaindolly296
- LinkedIn: www.linkedin.com/in/Dolly-singh-ds](https://www.linkedin.com/in/Dolly-singh-ds

If you found this project useful, consider giving it a ⭐ on GitHub.

