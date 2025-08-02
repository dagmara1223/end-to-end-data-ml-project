import pandas as pd

data_frame = pd.read_csv(r"C:\Users\dagak\OneDrive\Pulpit\titanic\titanic_cleaned.csv")
df = data_frame.copy()

# extract basic informations
print(df.info())
print(df.describe())

# we can see that we still have 177 missing values in "Age" column. 
# I will use RandomForestRegressor to predict age values. 

from sklearn.ensemble import RandomForestRegressor

known_age = df[df['Age'].notnull()]
unknown_age = df[df['Age'].isnull()]

X_train = known_age[['Pclass', 'SibSp', 'Parch', 'Fare']]
y_train = known_age['Age']
X_pred = unknown_age[['Pclass', 'SibSp', 'Parch', 'Fare']]

rfr = RandomForestRegressor()
rfr.fit(X_train, y_train)
predicted_ages = rfr.predict(X_pred)

df.loc[df['Age'].isnull(), 'Age'] = predicted_ages 

print(df.Age.isna().sum()) #check if random forest worked as expected

#feature engineering

# family size:
df['FamilySize'] = df['SibSp'] + df['Parch']

# if passenger was alone :
df['IsAlone'] = (df['FamilySize']==1).astype(int)

