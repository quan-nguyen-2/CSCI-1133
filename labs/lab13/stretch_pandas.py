import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("titanic.csv")

youngest_df = df.sort_values(['Age'], ascending = True)
print("Youngest passanger: ", youngest_df[:1]['Name'])

fare_df = df.sort_values(['Fare'], ascending = True)
print("Lowest fare ", youngest_df[:1]['Name'])

first_class_df = df.sort_values(['Pclass'], ascending = True)
average_fare = first_class_df[:216]
print("Average fare of first class: ", average_fare['Fare'].mean())

third_class_df = df[df['Pclass'] == 3]
print("Average age of third class: ", third_class_df['Age'].mean())

plt.hist(df['Pclass'], 3)
plt.xlabel("class")
plt.ylabel("Number of Passengers")
plt.savefig("passengers_hist.png")
plt.clf()

plt.hist(df['Age'], 10)
plt.xlabel("class")
plt.ylabel("Age of Passengers")
plt.savefig("age_hist.png")
plt.clf()

plt.scatter(df['Age'], df['Fare'])
plt.xlabel("Age")
plt.ylabel("fare")
plt.savefig("fare_vs_age.png")
plt.clf()
