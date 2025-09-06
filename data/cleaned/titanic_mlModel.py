import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# function for Confusion Matrix charts 
def chart(cm, title):
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'Confusion Matrix – {title}')
    plt.show()

#function for metrics
def report_metrics(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"\n{name} Results:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    return acc

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
y_pred_class = np.where(y_lin_pred >= 0.5, 1, 0)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# print("LinearRegress Accuracy:", accuracy_score(y_test, y_pred_class))
# print("LinearRegress Precision:", precision_score(y_test, y_pred_class))
# print("LinearRegress Recall:", recall_score(y_test, y_pred_class))
# print("LinearRegress F1-score:", f1_score(y_test, y_pred_class))
# print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_class))

cm = confusion_matrix(y_test, y_pred_class)
#chart(cm, 'Linear Regression')  


# Logistic Regression 
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=10000, random_state=0)
clf.fit(X_train, y_train)

report_metrics(clf, X_test, y_test, "Logistic Regression")

cm2 = confusion_matrix(y_test, clf.predict(X_test))
#chart(cm2, 'Logistic Regression')

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

best_tree = grid_search.best_estimator_
test_score = best_tree.score(X_test, y_test)
report_metrics(best_tree, X_test, y_test, "Decision Tree")

cm3 = confusion_matrix(y_test, best_tree.predict(X_test))
#chart(cm3, 'Decision Tree')

# Random Forest
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
report_metrics(best_rf, X_test, y_test, "Random Forest")

cm4 = confusion_matrix(y_test, best_rf.predict(X_test))
#chart(cm4, 'Random Forest')

from sklearn.ensemble import GradientBoostingClassifier

params_gb = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.05, 0.1, 0.2],
    'max_depth': [3, 5],
    'subsample': [0.8, 1.0]
}

gb = GradientBoostingClassifier(random_state=42)

grid_search_gb = GridSearchCV(estimator=gb, param_grid=params_gb,
                              cv=5, scoring='accuracy', n_jobs=-1)

grid_search_gb.fit(X_train, y_train)

best_gb = grid_search_gb.best_estimator_
report_metrics(best_gb, X_test, y_test, "Gradient Boosting")

cm5 = confusion_matrix(y_test, best_gb.predict(X_test))
#chart(cm5, 'Gradient Boosting')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

params_knn = {
    'knn__n_neighbors': [3, 5, 7, 11],
    'knn__weights': ['uniform', 'distance'],
    'knn__metric': ['euclidean', 'manhattan']
}

knn_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])
grid_search_knn = GridSearchCV(estimator=knn_pipeline, param_grid=params_knn,
                               cv=5, scoring='accuracy', n_jobs=-1)

grid_search_knn.fit(X_train, y_train)

best_knn = grid_search_knn.best_estimator_
report_metrics(best_knn, X_test, y_test, "KNN")

cm6 = confusion_matrix(y_test, best_knn.predict(X_test))
#chart(cm6, 'KNN')
