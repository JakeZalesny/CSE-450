import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
# Each column is a "Series"

print(df)
print(df["Age"].max())
print(df.describe())

# Reading CSV files example. 

titanic = pd.read_csv("data/titanic.csv")

#See the first 8 rows of a file.
# By default the first 5 and Last 5 are shown 
titanic.head(8)

# How did pandas interpret the data: 
titanic.dtypes()

# Convert sheet to an Excel
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

# Shape call
# Shape contains the number of attributes, rows and columns
titanic.shape()

#Filtering
above_35 = titanic[titanic["Age"] > 35]
above_35.head()
# This checks the attribute rather than calling the method. 
above_35.shape

class_two_and_three = titanic[titanic["Pclass"].isin([2, 3])]
class_two_and_three.head()

# Work with passenger data that's not known 
age_no_na = titanic[titanic["Age"].notna()]

# Select specific rows and columns from a dataframe 
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Rows 10-25 and columns 3-5
titanic.iloc[9:25, 2:5]

# Create Plots 
titanic.plot() 
plt.show() 

# you can specify the axis labels as well. 
titanic.plot.scatter(x="Age", y="Name", alpha=0.5)

