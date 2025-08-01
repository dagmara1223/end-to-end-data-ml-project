# end-to-end-data-ml-project
***"Not even God himself could sink this ship"** But could he?*   
This project is a personal data engineering and analytics pipeline built around the Titanic dataset from Kaggle. Step by step, it covers downloading the data, transforming it with Python, loading into PostgreSQL, migrating to MySQL, applying CDC logic, training a machine learning model, and presenting final insights in Power BI.  

## 📋 Background  
On April 15, 1912, the RMS Titanic sank in the North Atlantic after colliding with an iceberg. With only 20 lifeboats on board, over 1,500 lives were lost. This tragedy not only became a historical milestone but also left behind a dataset rich with social patterns.This project explores those patterns through an end-to-end data flow, answering one central question: ***"What kinds of people were more likely to survive?"***   
# 💻 Note! 
**Some steps might seem unnecessary, and that’s completely true. For example, moving data from CSV to PostgreSQL and then to Python isn’t strictly required. I included these just to demonstrate fun ways to learn new tools and how we can build simple ETL processes throughout our project.**    
  

## 🧪 Project Scope & Project Phases   
  
| Phase                       | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| 1. Dataset Selection      | Download Titanic dataset from Kaggle                 |
| 2. ETL (CSV → PostgreSQL -> Python)   | Clean and load structured data into a relational DB  |
| 3.ETL (PostgreSQL → MySQL)    | Test cross-system migration and schema compatibility    |
| 4. CDC                     | Capture and sync incremental changes between DBs       |
| 5. Data Cleaning            | Handle missing values, types, feature engineering  |
| 6. EDA             | Explore patterns visually & statistically    |
| 7. Machine Learning         | Train classifier to predict survival likelihood      |
| 8. Reporting (Power BI)     | Build dashboards to communicate insights             |


## 🆙 Project Phases - Details    
### 1. Dataset Selection ✅    
Source: https://www.kaggle.com/datasets/yasserh/titanic-dataset   
Format: CSV     
🧩 Steps:
- ☑️ Visit Kaggle and download the Titanic dataset (titanic.csv)    
- ☑️ Place the file into your Visual Studio Code and also create (for now- empty) python file : titanic.py   
  <img width="266" height="51" alt="image" src="https://github.com/user-attachments/assets/65412cf8-0736-4ccb-9729-8c4eb0f7c73c" />
- ☑️ Load csv file into the /data/raw directory on git
- ☑️ Don't forget to save csv file to Excel.   
  <img width="557" height="36" alt="image" src="https://github.com/user-attachments/assets/6ea3a765-bb23-433a-a120-bde0a0209328" />     
- ‼️ Important step: Please select whole "Name" column, click on "Ctrl + h". In Replace column type **,** into **Find what** bar, and ** ** into **Replace with**. Next click on **Replace All**. This step is super important before step 2.
  

### 2. ETL - This step is optional and added to demonstrate the concept       
Tools: Visual Studio 2022, pgAdmin 4, Visual Studio Code    
- ☑️ Open Visual Studio and create a new Integration Services Project.
- ☑️ To connect to pgAdmin (PostgreSQL), make sure to install the necessary drivers beforehand.
- ☑️ Select ***Data Flow Task*** from Search SSIS Toolbox and drop it into Control Float board.
- <img width="312" height="150" alt="image" src="https://github.com/user-attachments/assets/8ea245e1-93d6-47c3-bc43-3c1c811e176b" />
- ☑️ Double Click on it. You are now inside Data Flow board.
- ☑️ Select ***FLat File Source*** from Search SSIS Toolbox. Click on NEW in "Flat File connection manager" bar. Browse and select your Titanic data csv file path to establish the connection.
  For me it's: C:\Users\dagak\OneDrive\Pulpit\titanic\titanic.csv         
  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/9d38fe7d-c842-430f-bb76-f05098ee0e26" />
- ☑️ From Search SSIS Toolbox choose "Data Conversion" and use the **BLUE** arrow to connect with "Flat File Source". Do necessary mappings:    
  <img width="500" height="198" alt="image" src="https://github.com/user-attachments/assets/37af20a9-ee0e-4bd7-a2c3-6c65311fd9a3" />     
- ☑️ From Search SSIS Toolbox choose "ADO NET Destination" and use the **BLUE** arrow to connect with "Data Conversion".
- ☑️ Double click on ADO NET Destination. Once again choose NEW OLE DB Connection manager. NEW inside "Configure OLE DB Connection Window". Remember to choose the right Provider. Then simply click on OK.          
  <img width="350" height="447" alt="image" src="https://github.com/user-attachments/assets/72fc7b73-a1cd-4774-a30d-a71167cffe80" />
- ☑️ Next, I created a new database in **pgAdmin** with a table structure that aligns with the columns of the Titanic dataset (CSV file). We can do it manually using SQLStatement directly in pgAdmin using :     
CREATE SCHEMA IF NOT EXISTS titanic;      
SET search_path TO titanic;    
CREATE TABLE titanic.titanic_data(     
	  PassengerId INT PRIMARY KEY,     
    Survived INT,     
    Pclass INT,      
    Name VARCHAR(200),      
    Sex VARCHAR(50),     
    Age VARCHAR(50),      
    SibSp INT,     
    Parch INT,     
    Ticket VARCHAR(50),     
    Fare VARCHAR(50),     
    Cabin VARCHAR(50),     
    Embarked VARCHAR(50)     
);

Now back in SSIS we simply choose this table in "Use a table or view" bar. Remember to check mappings.  


to be continued
-------
## ⛏️ Structure    
| Folder / File                  | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| `data/`                        | Raw and processed data files (CSV, JSON, etc.)                        |
| ├── `raw/`                     | Original, untouched data files downloaded from Kaggle                 |
| └── `processed/`               | Cleaned and transformed data ready for loading                        |

