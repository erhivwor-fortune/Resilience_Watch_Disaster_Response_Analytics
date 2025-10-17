Project Documentation:

# Resilience Watch: Disaster Response Analytics
ResilienceWatch Analytics, in partnership with SafeGuard Insurance, identified challenges in managing disaster-related insurance claims. After major disasters, SafeGuard faced delays in claims processing, lack of real-time insights, and fragmented data systems, resulting in poor customer experience.
To address these issues, the Disaster Response KPI Dashboard was developed as a data engineering solution to automate the ingestion, processing, and storage of disaster data while enabling real-time KPI monitoring. This allows SafeGuard Insurance to improve claims efficiency, make data-driven decisions, and enhance customer satisfaction.
## Overview
The Disaster Response KPI Dashboard:
- Extracts disaster project data from FEMA APIs.
- Stores and organizes data in a PostgreSQL database.
- Provides real-time KPIs for claims processing, resolution time, and customer satisfaction.
- Uses Dockerized containers to ensure portability and consistent environments.
- Includes automated ETL pipelines built with Python and secure handling of sensitive information via .env files.
## Project Usage
- The project can be used to:
- Automate the extraction of disaster-related data.
- Centralize claims and disaster data for analysis.
- Generate actionable KPIs for operational managers.
- Test and deploy ETL pipelines and dashboards in a containerized environment.
## Prerequisites
- Docker Desktop
- Python 3.9+
- Git
- Power BI or Tableau for dashboard visualization
- Virtual environment management (venv).
## Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/erhivwor-fortune/Resilience_Watch_Disaster_Response_Analytics.git
 
2. Create a Virtual Environment:
   python -m venv venv
   
3. Activate virtual environment:
   # Windows
venv\Scripts\activate

   # Mac/Linux
   
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Set Up Environment Variables
Create a .env file in the project root with:
API_URL=<FEMA_API_URL>
DB_HOST=postgres
DB_PORT=5432
DB_USER=admin
DB_PASSWORD=admin
DB_NAME=disaster_insurance

7. Build and Run Docker Containers
docker compose build
docker compose up -d

8. Verify Database and pgAdmin
- Open pgAdmin at http://localhost:5050
- Log in with credentials from your compose file.
- Check that disaster_insurance database and disaster table exist.

7. Run ETL Pipeline
python main.py
This extracts data from the API and inserts it into PostgreSQL.
Check the database to ensure records have been populated successfully.

8. Dashboard Visualization
Connect Power BI or Tableau to the PostgreSQL database.
Build KPIs such as claims processed, claims in progress, resolution time, and customer satisfaction.

Author
Okiemute Fortune Erhivwor
