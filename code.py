# --------------
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 

# Load the data. Data is already given to you in variable `path` 
with open(path) as f:
    adm = csv.reader(f,delimiter=',')
    adm = list(adm)

# Remove the header
adm.remove(adm[0])

# Convert the data into a numpy array and store it in sales_data
sales_data=np.array(adm)

# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter
print(np.unique(sales_data[:,1]))
Counter(sales_data[:,1])

# What are the age groups that were targeted through these ad campaigns?
age = sales_data[:,3]

# Age groups are categorized as bins. So get a unique count of the bin
age_groups = np.unique(age)

print("The age groups targeted are ",age_groups)

# What was the average, minimum and maximum amount spent on the ads?
max_amt = sales_data[:,8].astype(float).max()
min_amt = sales_data[:,8].astype(float).min()
avg_amt = sales_data[:,8].astype(float).mean()

print('Minimum amt spent on ads was ',min_amt)
print('Maximum amt spent on ads was ',max_amt)
print('Average amt spent on ads was ',avg_amt)

# What is the id of the ad having the maximum number of clicks ?
# What were the maximum number of clicks
clicks = sales_data[:,7].astype(int).max()
print('The maximum number of clicks were ',clicks)
print()

# Which was the ad having the maximum number of clicks
max_clicks_ad = sales_data[:,0][sales_data[:,7].astype(int)==clicks]
print('The advertisement with the maximum number of clicks was the one with id ',max_clicks_ad)

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
 
max_sales = int(sales_data[:,-1][sales_data[:,0]==max_clicks_ad])
print('Number of people who bought the product having maximum ad clicks is ',max_sales)

print()

# Max value of the Approved_Conversion column
max_purchases = sales_data[:,-1].astype(int).max()

if (max_sales >= max_purchases):
    print("The maximum sales were on this product")
elif (max_sales <= max_purchases):
    print('The maximum number of purchases was ',max_purchases)

# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases

max_purchases = sales_data[:,0][sales_data[:,-1].astype(int) == sales_data[:,-1].astype(int).max()]

print("The ad id for the product having maximum number of purchases is: ",max_purchases)
print()
print('The record for this product is as shown below')
sales_data[sales_data[:,-1].astype(int)==sales_data[:,-1].astype(int).max()]

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 

# Create a new numpy array to calculate CTR
CTR = np.array((sales_data[:,7].astype(float)/sales_data[:,6].astype(float))*100)

# Note the shapes of CTR and the original array are different
print(sales_data.shape)
print('The original shape of CTR is ',CTR.shape)

# Convert CTR to the same shape as that of the original array
CTR = CTR.reshape(-1,1)
print('New shape of CTR is ',CTR.shape)

# Concatenate CTR to the original array
sales_data = np.concatenate((sales_data, CTR),axis=1)
sales_data

# Create a new column that represents Cost Per Mille (CPM) 


# Create a new numpy array to calculate CPM
CPM = (sales_data[:,8].astype(float)/sales_data[:,6].astype(float))*1000

# Note the shapes of CPM and the original array are different
print(sales_data.shape)
print('The original shape of CPM is ',CPM.shape)

# Convert CTR to the same shape as that of the original array
CPM = CPM.reshape(-1,1)
print('New shape of CTR is ',CPM.shape)

# Concatenate CTR to the original array
sales_data = np.concatenate((sales_data, CPM),axis=1)
print(sales_data)



