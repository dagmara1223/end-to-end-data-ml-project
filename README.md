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

