import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("./weather_forecast.csv")
print(df.head())
df = pd.get_dummies(df, drop_first=True)

X = df.drop('Play_Yes', axis=1)  
y = df['Play_Yes']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf_id3 = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_id3.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
plot_tree(clf_id3, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
plt.show()

y_pred_id3 = clf_id3.predict(X_test)
accuracy_id3 = accuracy_score(y_test, y_pred_id3)
report_id3 = classification_report(y_test, y_pred_id3)

print("ID3 Algorithm Results:")
print(f"Accuracy: {accuracy_id3}")
print(f"Classification Report:\n{report_id3}")

y_test

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print('Accuracy: ',accuracy*100)
