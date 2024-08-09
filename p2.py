import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("./ToyotaCorolla.csv")
print(df.head())

#Scatter plot
Mfg_Year = df["Mfg_Year"]
KM = df["KM"]
plt.figure(figsize=(8, 6))
plt.scatter(Mfg_Year, KM)
plt.xlabel("Mfg Year")
plt.ylabel("KM")
plt.title("Scatter Plot")
# plt.grid(True)  # Add grid lines for better readability
plt.show()

# Box plot
plt.boxplot([df["Price"],df["HP"],df["KM"]])
plt.show()

# Heat map
sns.heatmap(df[["Price","KM","Doors", "Weight"]].corr(),cmap="jet")
plt.show()

# Contour plot
x=df["Price"]
y=df["Age_08_04"]
z=df["KM"]
plt.tricontourf(x,y,z)
plt.colorbar(label="Price")
plt.show()

# 3D surface plot
x = df["KM"]
y = df["Doors"]
z = df["Price"]
ax = plt.axes(projection="3d")
ax.plot_trisurf(x,y,z,cmap="jet")
# ax.set_title("3D Surface Plot")
plt.show()
