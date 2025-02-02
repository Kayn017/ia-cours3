import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


raw_data = pd.read_csv("Datasets/customer_train.csv")

scaler = StandardScaler()
features_scaled = scaler.fit_transform(raw_data)

data = pd.DataFrame(features_scaled, columns=raw_data.columns)

k = 4
model = KMeans(n_clusters=k, random_state=42)


data["cluster"] = model.fit_predict(data)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(data["annual_income"], data["spending_score"], c=data["cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")

plt.subplot(1, 3, 2)
plt.scatter(data["age"], data["spending_score"], c=data["cluster"])
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Age vs Spending Score")

plt.subplot(1, 3, 3)
plt.scatter(data["age"], data["annual_income"], c=data["cluster"])
plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.title("Age vs Annual Income")

plt.show()
