# end-to-end-data-ml-project
***"Not even God himself could sink this ship"** But could he?*   
This project is a personal data engineering and analytics pipeline built around the Titanic dataset from Kaggle. Step by step, it covers downloading the data, transforming it with Python, loading into PostgreSQL, migrating to MySQL, applying CDC logic, training a machine learning model, and presenting final insights in Power BI.  

## 📋 Background  
On April 15, 1912, the RMS Titanic sank in the North Atlantic after colliding with an iceberg. With only 20 lifeboats on board, over 1,500 lives were lost. This tragedy not only became a historical milestone but also left behind a dataset rich with social patterns.This project explores those patterns through an end-to-end data flow, answering one central question: ***"What kinds of people were more likely to survive?"***   

## 🧪 Project Scope & Project Phases   
  
| Phase                       | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| 1. Dataset Selection      | Download Titanic dataset from Kaggle                 |
| 2. ETL (CSV → PostgreSQL)   | Clean and load structured data into a relational DB  |
| 3. Data Cleaning            | Handle missing values, types, feature engineering    |
| 4. EDA                      | Explore patterns visually & statistically            |
| 5. ETL (PostgreSQL → MySQL) | Test cross-system migration and schema compatibility |
| 6. CDC                      | Capture and sync incremental changes between DBs     |
| 7. Machine Learning         | Train classifier to predict survival likelihood      |
| 8. Reporting (Power BI)     | Build dashboards to communicate insights             |


## 🆙 Project Phases - Details    
# 1. Dataset Selection ✅    
Source: https://www.kaggle.com/datasets/yasserh/titanic-dataset   
Format: CSV     

to be continued
-------
## ⛏️ Structure    
| Folder / File                  | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| `data/`                        | Raw and processed data files (CSV, JSON, etc.)                        |
| ├── `raw/`                     | Original, untouched data files downloaded from Kaggle                 |
| └── `processed/`               | Cleaned and transformed data ready for loading                        |
| `notebooks/`                   | Jupyter notebooks for experiments and data analysis (EDA, ML)         |
| `scripts/`                     | Python scripts for ETL, model training, CDC, and other pipeline steps |
| ├── `etl_csv_to_postgres.py`   | Script to load CSV data into PostgreSQL                               |
| ├── `etl_postgres_to_mysql.py` | Script to migrate data from PostgreSQL to MySQL                       |
| ├── `cdc_sync.py`              | Script to perform Change Data Capture and synchronize databases       |
| └── `train_model.py`           | Script to train machine learning models                               |
| `sql/`                         | SQL scripts for creating schemas, views, and stored procedures        |
| ├── `postgres_schema.sql`      | PostgreSQL database schema creation script                            |
| └── `mysql_schema.sql`         | MySQL database schema creation script                                 |
| `reports/`                     | Generated reports and analysis outputs (CSV, PDF, etc.)               |
| `power_bi/`                    | Power BI project files (`.pbix`)                                      |
| `requirements.txt`             | Python package dependencies                                           |
| `README.md`                    | Project documentation (this file)                                     |
| `.gitignore`                   | Git ignore file specifying untracked files                            |
