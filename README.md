Project Documentation:
# **Resilience Watch: Disaster Response Analytics**

**ResilienceWatch Analytics**, in partnership with **SafeGuard Insurance**, identified challenges in managing disaster-related insurance claims.  
After major disasters, SafeGuard faced delays in claims processing, lack of real-time insights, and fragmented data systems, resulting in poor customer experience.

To address these issues, the **Disaster Response KPI Dashboard** was developed as a **data engineering solution** to automate the ingestion, processing, and storage of disaster data while enabling **real-time KPI monitoring**.  
This allows SafeGuard Insurance to improve claims efficiency, make data-driven decisions, and enhance customer satisfaction.

---

## **Overview**

The Disaster Response KPI Dashboard:
- Extracts disaster project data from **FEMA APIs**
- Stores and organizes data in a **PostgreSQL database**
- Provides **real-time KPIs** for claims processing, resolution time, and customer satisfaction
- Uses **Dockerized containers** to ensure portability and consistent environments
- Includes automated **ETL pipelines** built with Python and secure handling of sensitive information via `.env` files

---

### Project Architecture
Below is the high-level architecture of the Disaster Response KPI Dashboard:

![project architecture](https://github.com/user-attachments/assets/bb950b23-843a-45e8-bd0e-10d2c579c1cd)


## **Project Usage**

The project can be used to:
- Automate the extraction of disaster-related data  
- Centralize claims and disaster data for analysis  
- Generate actionable KPIs for operational managers  
- Test and deploy ETL pipelines and dashboards in a containerized environment  

---

## **Prerequisites**

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Python **3.9+**
- [Git](https://git-scm.com/)
- Power BI or Tableau (for dashboard visualization)
- Astronomer Airflow
- Virtual environment management (`venv`)

---

## **Setup Instructions**
This guide gives instructions on how to setup the project environment and necessary configurations
### 1. Clone the repository
    git clone https://github.com/erhivwor-fortune/Resilience_Watch_Disaster_Response_Analytics.git
    cd Resilience_Watch_Disaster_Response_Analytics

### 2. Create a virtual environment
    python -m venv venv

### 3. Activate virtual environment
#### Windows
    venv\Scripts\activate
#### Mac OS
    source venv/bin/activate

### 4. Install dependencies
    pip install -r requirements.txt

### 5. Set up enviroment variables
#### Create a .env file in the project root and add:
    API_URL=<FEMA_API_URL>
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=admin
    DB_PASSWORD=admin
    DB_NAME=disaster_insurance

### 6. Build and run Docker containers
    docker compose build
    docker compose up -d

### 7. Verify database and pgAdmin
Open http://localhost:5050

Log in using the credentials from your compose file

Confirm that the disaster_insurance database and disaster table exist

### 8. Run ETL pipeline
    python main.py

### 9. Dashboard visualization
Connect Power BI or Tableau to the PostgreSQL database and visualize KPIs such as:

Claims processed

Claims in progress

Resolution time

Customer satisfaction
