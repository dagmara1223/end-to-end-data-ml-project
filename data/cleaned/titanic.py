import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

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

df['Age'] = df['Age'].astype(int)
print(df['Age'])

#feature engineering

# family size:
df['FamilySize'] = df['SibSp'] + df['Parch']

# if passenger was alone :
df['IsAlone'] = (df['FamilySize']==1).astype(int)

df.to_csv('data_cleaned2.csv')

#---------------------------EDA

# Survival by gender + class

sns.barplot(data=df, x='Sex',y='Survived',color='pink')
plt.title('Survival by gender')
plt.show()

survival_by_sex = df.groupby(['Sex','Survived']).size().unstack()

sns.barplot(data=df, x='Pclass',y='Survived', color='pink')
plt.title('Survival by class')
plt.show()

survival_by_class = df.groupby(['Pclass','Survived']).size().unstack()
print(survival_by_class)

#gender and class together 
sns.catplot(data=df, x='Pclass', hue='Sex',col='Survived', kind='count')
plt.show()

# age and survival 
sns.histplot(data=df, x='Age', hue='Survived',multiple='stack',bins=30,color='pink')
plt.title('Survival indicated by age')
plt.show()

df['AgeGroup'] = pd.cut(df['Age'], bins=[0,20,40,60,80],right=False)
age_counts = df['AgeGroup'].value_counts().sort_index()
print(age_counts)
survived_by_age = df[df['Survived'] == 1]['AgeGroup'].value_counts().sort_index()
print(survived_by_age)

#survival rates vs family size
sns.barplot(data=df, x='FamilySize', y='Survived', color='pink')
plt.title("Survival rate vs Family size")
plt.show()

# Passenger title
df['Title'] =  df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col',
 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Valued Profession')
df['Title'] = df['Title'].replace({'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'})

#title and survival rate
sns.barplot(data=df, x='Title', y='Survived', color='pink')
plt.title("Title vs Survival")
plt.show()

# final clean up
df.drop(columns=['Name', 'Ticket', 'PassengerId'], inplace=True)

# encoding categoricals
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=False, dtype=int)

# numerical correlation matrix
correlation_matrix = df.corr(numeric_only=True)
survival_corr = correlation_matrix['Survived'].sort_values(ascending=False)
print(survival_corr)

#heatmap
plt.figure(figsize=(8, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Matrix of Titanic Features")
plt.show()
