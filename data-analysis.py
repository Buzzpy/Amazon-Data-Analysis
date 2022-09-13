# Import Libraries
import pandas as pd

df = pd.read_csv('Amazon Dataset.csv') # read the file
pd.set_option('display.max_columns', None) # display all the columns
print(df) # print the dataframe created

# -------------------------------------

df.drop_duplicates() #remove duplicates
df = df.fillna(0) #fill cells with null values with 0
df["Item Total"] = df["Item Total"].str.replace('$','').astype(float) 
# remove dollar sign in 'Item Total' column and convert to float value.

# -------------------------------------

print(df["Item Total"].sum()) # find total of values in the column "Item Total"
print(df["Item Total"].max()) # find largest value of the values in the column "Item Total"
print(df["Item Total"].min()) # find least value of the values in the column "Item Total"
print(df["Item Total"].mean()) # find mean of the values in the column "Item Total"
print(df["Item Total"].median() # find median of the values in the column "Item Total"

# Awesome!

