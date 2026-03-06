import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_marks.csv")

print("Student Data:")
print(data)

data["Average"] = data[["Maths","Science","English"]].mean(axis=1)

print("\nData with Average:")
print(data)

top_student = data.loc[data["Average"].idxmax()]

print("\nTop Student:")
print(top_student)

data.plot(x="Name", y=["Maths","Science","English"], kind="bar")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

data.to_csv("student_marks_output.csv", index=False)