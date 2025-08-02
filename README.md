# end-to-end-data-ml-project
***"Not even God himself could sink this ship"** But could he?*   
This project is a personal data engineering and analytics pipeline built around the Titanic dataset from Kaggle. Step by step, it covers downloading the data, transforming it with Python, loading into MySQL, migrating to PostgreSQL, applying CDC logic, training a machine learning model, and presenting final insights in Power BI.  

## 📋 Background  
On April 15, 1912, the RMS Titanic sank in the North Atlantic after colliding with an iceberg. With only 20 lifeboats on board, over 1,500 lives were lost. This tragedy not only became a historical milestone but also left behind a dataset rich with social patterns.This project explores those patterns through an end-to-end data flow, answering one central question: ***"What kinds of people were more likely to survive?"***   
# 💻 Note! 
**Some steps might seem unnecessary, and that’s completely true. For example, moving data from CSV to PostgreSQL and then to Python isn’t strictly required. I included these just to demonstrate fun ways to learn new tools and how we can build simple ETL processes throughout our project.**    
  

## 🧪 Project Scope & Project Phases   
  
| Phase                       | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| 1. Dataset Selection      | Download Titanic dataset from Kaggle                 |
| 2. ETL (CSV → MySQL -> Python)   | Clean and load structured data into a relational DB  |
| 3.ETL (MySQL → PostgreSQL)    | Test cross-system migration and schema compatibility    |
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
  

### 2. ETL - Steps 2,3,4 are optional and added to demonstrate the concept       
Tools: Visual Studio 2022, SSMS, Visual Studio Code, SSIS    
- ☑️ Open and create a new database in SSMS named "titanic". 
- ☑️ Open Visual Studio and create a new Integration Services Project.
- ☑️ Select ***Data Flow Task*** from Search SSIS Toolbox and drop it into Control Float board.    
   <img width="312" height="150" alt="image" src="https://github.com/user-attachments/assets/8ea245e1-93d6-47c3-bc43-3c1c811e176b" />
- ☑️ Double-click on the **Data Flow Task** to open the **Data Flow** tab. Now select **Flat File Source** from Search SSIS Toolbox. Next, in Flat File Connection Manager create a new connection to your titanic.csv file. For example, my file path is: C:\Users\dagak\OneDrive\Pulpit\titanic\titanic.csv. Change CodePage to 1250.    
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
  We have successfully transferred data from the CSV file to the MS SQL database. If you want, you can analyze and clean your data here - in SSMS before loading it into Python. I will cover this process in Section 5, so if   you are not interested in SSIS, feel free to skip ahead to that section.  [read mysql --> python to be continued]

  

to be continued
-------
## ⛏️ Structure    
| Folder / File                  | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| `data/`                        | Raw and processed data files (CSV, JSON, etc.)                        |
| ├── `raw/`                     | Original, untouched data files downloaded from Kaggle                 |
| └── `processed/`               | Cleaned and transformed data ready for loading                        |

