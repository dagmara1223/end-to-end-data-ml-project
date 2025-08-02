# end-to-end-data-ml-project
***"Not even God himself could sink this ship"** But could he?*   
This project is a personal data engineering and analytics pipeline built around the Titanic dataset from Kaggle. Step by step, it covers downloading the data, transforming it with Python, loading into MySQL, applying CDC logic, training a machine learning model, and presenting final insights in Power BI.  

## 📋 Background  
On April 15, 1912, the RMS Titanic sank in the North Atlantic after colliding with an iceberg. With only 20 lifeboats on board, over 1,500 lives were lost. This tragedy not only became a historical milestone but also left behind a dataset rich with social patterns.This project explores those patterns through an end-to-end data flow, answering one central question: ***"What kinds of people were more likely to survive?"***     
## 🧪 Project Scope & Project Phases   
  
| Phase                          | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| 1. Dataset Selection           | Download Titanic dataset from Kaggle                    |
| 2. ETL (CSV → MySQL)           | Load structured data into a relational database (MySQL)  |
| 3. Pre-Analysis in MySQL       | Run initial queries to check data quality and structure |
| 4. ETL (MySQL -> CSV)          | Load analyzed data from MySQL to CSV file               |
| 5. Data Cleaning               | Handle missing values, types, feature engineering        |
| 6. EDA                         | Explore patterns visually & statistically                |
| 7. Machine Learning            | Train classifier to predict survival likelihood          |
| 8. Reporting (Power BI)        | Build dashboards to communicate insights                 |


## 🆙 Project Phases - Details    
### 1. Dataset Selection ✅    
Source: https://www.kaggle.com/datasets/yasserh/titanic-dataset   
Tools: Kaggle, Excel, Visual Studio Code    
🧩 Steps:
- ☑️ Visit Kaggle and download the Titanic dataset (titanic.csv)    
- ☑️ Place the csv file into your Visual Studio Code and also create (for now- empty) python file : titanic.py   
  <img width="266" height="51" alt="image" src="https://github.com/user-attachments/assets/65412cf8-0736-4ccb-9729-8c4eb0f7c73c" />
- ☑️ Don't forget to save your csv file in Excel.   
  <img width="557" height="36" alt="image" src="https://github.com/user-attachments/assets/6ea3a765-bb23-433a-a120-bde0a0209328" />     
- ‼️ Important step: Using Excel select whole "Name" column, click on "Ctrl + h". In Replace column type "," (comma) in **Find what** bar, and " " (space) in **Replace with**. Next click on **Replace All**. This step is super important before step 2.
***RESULTS PATH*** : data/raw/titanic.csv  

### 2. ETL CSV -> MySQL ✅    
Tools: Visual Studio 2022, SSMS, SSIS    
- ☑️ Open and create a new database in SSMS named "titanic". 
- ☑️ Open Visual Studio and create a new Integration Services Project.
- ☑️ Select ***Data Flow Task*** from Search SSIS Toolbox and drop it into Control Float board.    
   <img width="312" height="150" alt="image" src="https://github.com/user-attachments/assets/8ea245e1-93d6-47c3-bc43-3c1c811e176b" />
- ☑️ Double-click on the **Data Flow Task** to open the **Data Flow** tab. Now select **Flat File Source** from Search SSIS Toolbox. ‼️‼️Make sure to mark "Retain null values from the source as null values in the data flow". Next, in Flat File Connection Manager create a new connection to your titanic.csv file. For example, my file path is: C:\Users\dagak\OneDrive\Pulpit\titanic\titanic.csv. Change CodePage to 1250.    
  <img width="400" height="332" alt="image" src="https://github.com/user-attachments/assets/b1e94515-6201-48e6-8cbe-fdd5ae5147c7" />
- ☑️ Now, in the Advanced tab, we need to change the data types of our columns. The following pattern should be applied:     
  PassengerId -> DataType: numeric          
  Survived -> DataType: numeric           
  Pclass -> DataType: numeric                        
  Name -> DataType: string, OutputColumnWidth: 200        
  Sex -> DataType: string, OutputColumnWidth: 50       
  Age -> DataType: float        
  SibSp -> DataType: numeric        
  Parch -> DataType: numeric            
  Ticket -> DataType: string, OutputColumnWidth: 50      
  Fare -> DataType: float                          
  Cabin -> DataType: string, OutputColumnWidth: 50          
  Embarked -> DataType: string, OutputColumnWidth: 50
- ☑️ From Search SSIS Toolbox choose **OLE DB Destination** and using blue arrow connect **Flat File Source** with **OLE DB Destination**. In OLE DB Destination Manager create a new connection to your titanic database in SSMS.
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/7c0d515e-4f9d-4023-918d-8d2ef10d124b" />
- ☑️ In SSMS create following table:    
  use titanic;     
CREATE TABLE [titanic_data] (
    [PassengerId] numeric(18,0),
    [Survived] numeric(18,0),
    [Pclass] numeric(18,0),
    [Name] varchar(200),
    [Sex] varchar(50),
    [Age] real,
    [SibSp] numeric(18,0),
    [Parch] numeric(18,0),
    [Ticket] varchar(50),
    [Fare] real,
    [Cabin] varchar(50),
    [Embarked] varchar(50)
)          
- ☑️ The configuration in SSIS should be as follows : <img width="300" height="222" alt="image" src="https://github.com/user-attachments/assets/bdb8ea4d-6e66-4c6b-a7a3-6d84f3f77727" />
- ☑️ Click on start. The final configuration without errors should produce the following results:           
  In SSIS :<img width="300" height="252" alt="image" src="https://github.com/user-attachments/assets/95b6e77e-b885-49f2-80a4-55bee38f510a" />                    
  In SSMS: <img width="500" height="502" alt="image" src="https://github.com/user-attachments/assets/61d4cf88-f31e-412f-865a-319fc73ddfb9" />                 
  We have successfully transferred data from the CSV file to the MS SQL database.

***RESULTS PATH***: etl_all/CSVtoMYSQL  
### 3. Pre-Analysis in MySQL ✅
tools: SSMS   
| Column        | Description                                                          |
| ------------- | -------------------------------------------------------------------- |
| `PassengerId` | Unique identifier for each passenger                                 |
| `Survived`    | Survival status (0 = No, 1 = Yes)                                    |
| `Pclass`      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)                             |
| `Name`        | Full name of the passenger                                           |
| `Sex`         | Gender of the passenger                                              |
| `Age`         | Age of the passenger in years                                        |
| `SibSp`       | Number of siblings or spouses aboard the Titanic                     |
| `Parch`       | Number of parents or children aboard the Titanic                     |
| `Ticket`      | Ticket number                                                        |
| `Fare`        | Fare paid for the ticket                                             |
| `Cabin`       | Cabin number (if available)                                          |
| `Embarked`    | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |     

Before jumping into data cleaning or machine learning, I ran initial analysis directly in SQL to better understand the dataset and spot potential issues early. This step included:      
- ☑️ Checking for missing values and NULLs     
- ☑️ Identifying duplicate records (by PassengerId or full row comparison)     
- ☑️ Exploring distribution of categorical variables, like Survived, Sex, Pclass, Embarked etc        
- ☑️ Calculating basic statistics (AVG, MIN, MAX, STD) for numerical columns       
- ☑️ Detecting outliers and unusual values, such as passengers with age > 80 or fare > 300      
- ☑️ Creating basic group-based insights, like survival rate by gender and class

During the initial data analysis, I identified several data quality issues and made following cleaning decisions:    
- Removed the Cabin column due to nearly 80% missing values. This feature also showed no significant impact on the target variable (Survival).
- Dropped 2 rows with missing values in the Embarked column. Given the small number of missing entries and their potential importance for modeling, these rows were removed to simplify preprocessing.
- The problem with column age, with 177 missing values will be solved in Python Analysis part. 

***RESULTS PATH(directory in my repo)***: SQL/SQLanalysis.sql     

### 4. ETL (MySQL -> CSV) ✅  
Tools: SSIS, SSMS    
Before moving forward with advanced analysis and machine learning, I extracted the cleaned dataset from MySQL and saved it as a CSV file.      
- ☑️ Create new Integration Services Project in SSIS.    
- ☑️ Choose **Data Flow Task** from Search SSIS Toolbox and Double Click on it.
- ☑️ In the Data Flow section, select **OLE DB Source** and establish a stable connection to your MySQL Server. If you completed step 3, the connection should already be available in the Configure OLE DB Connection Manager window :            
<img width="300" height="347" alt="image" src="https://github.com/user-attachments/assets/dd5053f2-5d16-4ec1-8738-3a950e2ee066" />    <br>
Choose the titanic_data table (one that we analyzed in SSMS).  
- ☑️ Now choose **Flat File Destination** from Search SSIS Toolbox and connect it with **OLE DB Source** using blue arrow. Flat file format should be "Delimited".       
- ☑️ In your desired destination the new csv file will be created. Don't forget to change "Code Page" to 1250 in "Flat File Connection Manager Editor".                
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/65384a3e-971f-4ad2-960e-d28c7c336d6e" />   <br>
<img width="300" height="335" alt="image" src="https://github.com/user-attachments/assets/adeb6bec-fae3-4948-a09b-6aed8ef7c4e3" />   <br>
- ☑️ Click on start. The final configuration without errors should produce the following results:    
In SSMS: <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/dccbec81-db01-47e7-afe3-c387cc77c84d" />  
In chosen Folder: <img width="200" height="218" alt="image" src="https://github.com/user-attachments/assets/e6d32c7b-7ed3-4aef-88e7-57f1fc746bb2" />  
In newly created csv file: <img width="350" height="383" alt="image" src="https://github.com/user-attachments/assets/2c803959-0135-4f5e-b39b-464851b93064" />

***RESULTS PATH 1***: data/cleaned/titanic_cleaned.csv
***RESULTS PATH 2***: etl_all/mysqlTOcsv

### 5. Data Cleaning 
Tools: Visual Studio Code  
Before building any predictive models, the dataset needed to be cleaned and enhanced. This step included:  
- ☑️ Handling missing values in Age:  
Instead of dropping 177 rows with missing ages (too many to safely discard), use a Random Forest Regressor to estimate them. The model was trained on features like Pclass, SibSp, Parch, and Fare, and then used to fill in the missing age values.  
- ☑️ Creating new features:  
FamilySize: total number of family members onboard (SibSp + Parch)  
IsAlone: binary feature indicating whether a passenger was traveling alone (1) or not (0)  

***RESULTS PATH***: data/cleaned/titanic.py

to be continued
-------
## ⛏️ Structure    
| Folder / File                  | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| `data/`                        | Raw and processed data files (CSV, JSON, etc.)                        |
| ├── `raw/`                     | Original, untouched data files downloaded from Kaggle                 |
| └── `processed/`               | Cleaned and transformed data ready for loading                        |
| `etl_all/`                     | ETL scripts and logic used to transform and load data                 |
| └── `CSVtoMYSQL/`              | Project or script for loading CSV files into a MySQL database         |
| └── `mysqlTOcsv/`              | Script or tool for exporting data from MySQL to CSV       
| `SQL/`                         | Folder containing SQL scripts and database analysis                   |
| └── `SQLanalysis.sql`          | SQL script with data exploration or transformation logic              |
| `README.md`                    | Description of the project and instructions                           |


