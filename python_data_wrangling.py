import pandas as pd

# df = pd.read_csv("housing.csv")
# print(df.head())
# print(df.info())

"""dropping duplicate rows"""

# df = pd.read_csv("housing.csv")
# print(df.head())
# print("after duplicates")
# df.drop_duplicates(inplace=True)
# print(df.head())

"""dropping duplicates based on only few columns"""
# df = pd.read_csv("housing.csv")
# print(df.head())
# print("after duplicates")
# df.drop_duplicates(subset=['households','median_income'], inplace=True)
# print(df.head())

"""transformation of data - Renaming Column"""

# df = pd.read_csv("housing.csv")
# print(df.head())
# df.rename(columns={"ocean_proximity":"Ocean_Boundary","longitude":"Long"}, inplace=True)
# print(df)

"""Group BY ------------------------"""

df = pd.read_csv("housing.csv")
print(df.head())
grouped_data = df.groupby("ocean_proximity")['median_house_value'].mean().reset_index()
print(grouped_data)


#Wait a 5 min guy ! i got injured.. taking medicine.. please wait...







































