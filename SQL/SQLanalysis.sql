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
FROM [dbo].[titanic_data]; --we can see that age_null:177, cabin_null: 687, embarked_null:2

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

--------------------------------
--Survival rate: 
SELECT 
	Survived,
	COUNT(*) AS if_survived,  --0: not survived, 1:survived
	ROUND(COUNT(*) * 100.0 / CAST((SELECT COUNT(*) FROM [dbo].[titanic_data]) AS FLOAT), 2) AS percentage
FROM [dbo].[titanic_data]
GROUP BY Survived;  

-- survival rate by sex
SELECT 
  Sex,
  Survived,  --0:not survived, 1:survived
  COUNT(*) AS count
FROM [dbo].[titanic_data]
GROUP BY Sex, Survived ORDER BY Sex, Survived;

-- average age by sex
SELECT 
	Sex,
	ROUND(AVG(Age),2) AS avg_age
FROM [dbo].[titanic_data]
GROUP BY Sex;

-- average fare by Pclass and survival
SELECT 
	Pclass,
	Survived,
	AVG(Fare) AS avg_fare
FROM [dbo].[titanic_data]
GROUP BY Pclass, Survived ORDER BY Pclass, Survived;

-- Age binning
WITH AgeGroups AS (
	SELECT 
		CASE
			WHEN Age < 13 THEN 'Child'
			WHEN Age >= 13 AND Age <18 THEN 'Teenager'
			WHEN Age >=18 AND Age < 60 THEN 'Adult'
			WHEN Age >= 60 THEN 'Senior'
		END AS age_group
	FROM [dbo].[titanic_data]
)
SELECT COUNT(*), age_group FROM AgeGroups GROUP BY age_group;
-- Adult: 575, NULL: 177, Teenager: 44, Senior: 26, Child : 69

-- Outliers
SELECT * 
FROM titanic_data 
WHERE fare > 300;  -- 3 passengersId: 259, 680, 738

SELECT * 
FROM titanic_data 
WHERE age > 80;  --none

-- our NULL data
SELECT * FROM [dbo].[titanic_data] WHERE Age IS NULL OR Cabin IS NULL OR Embarked IS NULL;
SELECT COUNT(*) FROM [dbo].[titanic_data] WHERE Age IS NULL OR Cabin IS NULL OR Embarked IS NULL; --708

-- survival table
SELECT 
  pclass, sex,
  SUM(CASE WHEN survived = 1 THEN 1 ELSE 0 END) AS survived,
  SUM(CASE WHEN survived = 0 THEN 1 ELSE 0 END) AS died
FROM [dbo].[titanic_data]
GROUP BY pclass, sex ORDER BY pclass,sex; 

SELECT * FROM titanic_data WHERE Cabin IS NULL;

ALTER TABLE [dbo].[titanic_data]
DROP COLUMN Cabin;

DELETE FROM [dbo].[titanic_data]
WHERE Embarked IS NULL;

SELECT * FROM [dbo].[titanic_data]


