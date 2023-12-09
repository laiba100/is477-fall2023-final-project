import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

wine_data = 'data/wine/wine.data'
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
column_names = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
                "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
                "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
wine_df = pd.read_csv(url, names=column_names)

summary = wine_df.describe()
summary.to_csv('results/wine_data_summary_statistics.csv')

X = wine_df.drop('Class', axis=1)
y = wine_df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
with open('results/classification_report.txt', 'w') as f:
    f.write('Classification Accuracy: {}'.format(accuracy))

plt.figure(figsize=(10, 6))
plt.hist(wine_df['Alcohol'], bins=15, color='hotpink', alpha=0.7)
plt.title('Alcohol Content Distribution')
plt.xlabel('Alcohol')
plt.ylabel('Frequency')
plt.savefig('results/wine_data_analysis_histogram.png')
