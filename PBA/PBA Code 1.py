import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print(df.head())
print(df.info())

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

print("\nStudents scoring more than 75 marks:")
print(df[df["Marks"] > 75])

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Student Marks")
plt.show()

plt.scatter(df["Study Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()