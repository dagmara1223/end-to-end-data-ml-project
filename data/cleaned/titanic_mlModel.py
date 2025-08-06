import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\dagak\OneDrive\Pulpit\titanic\CSVforML.csv')
# last cleaning 
df.drop(columns=['AgeGroup'], inplace=True)
df = pd.get_dummies(df, columns=['Title'], drop_first=False, dtype=int)

# train and test set
from sklearn.model_selection import train_test_split

X = df.drop('Survived',axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Linear Regression
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)

y_lin_pred = lin_reg.predict(X_test)
#print(y_lin_pred)

y_pred_class = np.where(y_lin_pred >= 0.5, 1, 0)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

print("LinearRegress Accuracy:", accuracy_score(y_test, y_pred_class))
print("LinearRegress Precision:", precision_score(y_test, y_pred_class))
print("LinearRegress Recall:", recall_score(y_test, y_pred_class))
print("LinearRegress F1-score:", f1_score(y_test, y_pred_class))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_class))

cm = confusion_matrix(y_test, y_pred_class)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix – Linear Regression')
plt.show()

# Logistic Regression
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=10000, random_state=0)
clf.fit(X_train, y_train)

print("LogisticRegress Accuracy: ", accuracy_score(y_test, clf.predict(X_test)) )
print("LogisticRegress precision: ", precision_score(y_test, clf.predict(X_test)))
print("LogisticRegress recall: ", recall_score(y_test, clf.predict(X_test)))
print("LogisticRegress f1 score: ", f1_score(y_test, clf.predict(X_test)))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, clf.predict(X_test)))

cm_2 = confusion_matrix(y_test, clf.predict(X_test))
sns.heatmap(cm_2, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Logistic Regression')
plt.show()

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

params = {
    'min_samples_split':[2,5,10,20,50],
    'max_depth':[None, 3,5,10]
}
tree = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(tree, params, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print(f'Best params: {grid_search.best_params_}')
print(f'Best score: {grid_search.best_score_}')

best_tree = grid_search.best_estimator_
test_score = best_tree.score(X_test, y_test)
print(f'Test set accuracy: {test_score:.4f}')

cm_3 = confusion_matrix(y_test, best_tree.predict(X_test))
sns.heatmap(cm_3, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Decision Tree')
plt.show()

# Random Forest
from sklearn.ensemble import RandomForestClassifier

params = {
    'n_estimators': [50, 100, 200],         
    'max_depth': [None, 5, 10, 20],        
    'min_samples_split': [2, 5, 10],       
    'min_samples_leaf': [1, 2, 4],         
    'max_features': ['auto', 'sqrt', 'log2'] 
}
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(estimator=rf, param_grid=params, 
                           cv=5, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train, y_train)

best_rf = grid_search.best_estimator_
print("Best Parameters:", grid_search.best_params_)
print("Best CV Score:", grid_search.best_score_)
print("Test Accuracy:", best_rf.score(X_test, y_test))


