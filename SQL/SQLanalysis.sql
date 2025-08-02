USE titanic;

-- Number of records
SELECT COUNT(*) AS number_of_records FROM [dbo].[titanic_data];

-- Duplicates 
SELECT PassengerId, COUNT(PassengerId) AS count_passenger_id 
FROM [dbo].[titanic_data] 
GROUP BY PassengerId 
HAVING COUNT(PassengerId) > 1;   --brak

-- NULL values in each column
SELECT
	SUM(CASE WHEN PassengerId IS NULL THEN 1 ELSE 0 END) AS passengerid_null,
	SUM(CASE WHEN Survived IS NULL THEN 1 ELSE 0 END) AS survived_null,
	SUM(CASE WHEN Pclass IS NULL THEN 1 ELSE 0 END) AS pcalss_null,
	SUM(CASE WHEN [Name] IS NULL THEN 1 ELSE 0 END) AS name_null,
	SUM(CASE WHEN Sex IS NULL THEN 1 ELSE 0 END) AS sex_null,
	SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS age_null,
	SUM(CASE WHEN SibSp IS NULL THEN 1 ELSE 0 END) AS sibsip_null,
	SUM(CASE WHEN Parch IS NULL THEN 1 ELSE 0 END) AS parch_null,
	SUM(CASE WHEN Ticket IS NULL THEN 1 ELSE 0 END) AS ticket_null,
	SUM(CASE WHEN Fare IS NULL THEN 1 ELSE 0 END) AS fare_null,
	SUM(CASE WHEN Cabin IS NULL THEN 1 ELSE 0 END) AS cabin_null,
	SUM(CASE WHEN Embarked IS NULL THEN 1 ELSE 0 END) AS embarked_null
FROM [dbo].[titanic_data]; --we can see that age_null:2, cabin_numm: 687, embarked_null:2

-- data range within categorical data
SELECT sex, COUNT(*) AS sex_range
FROM [dbo].[titanic_data] 
GROUP BY sex;  --male: 577, female: 314

SELECT Pclass, COUNT(*) AS Pclass_range
FROM [dbo].[titanic_data] 
GROUP BY Pclass; --1: 216, 2: 184, 3:491

SELECT Embarked, COUNT(*) AS Embarked_range
FROM [dbo].[titanic_data] 
GROUP BY Embarked; -- s: 644, NULL:2, Q:77, C:168

-- age and fare stats
SELECT 
  MIN(Age) AS min_age,
  MAX(Age) AS max_age,
  ROUND(AVG(Age),2) AS avg_age
FROM [dbo].[titanic_data];

SELECT 
  MIN(Fare) AS min_fare,
  MAX(Fare) AS max_fare,
  ROUND(AVG(Fare),2) AS avg_fare
FROM [dbo].[titanic_data];

--Survival rate: 

