# import packages
import pandas as pd
import numpy as np

# load data
price = pd.read_csv('data/airbnb_price.csv')
room_type = pd.read_excel('data/airbnb_room_type.xlsx')
last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# CLEANING

# price is formatted as '[value] dollars'
# this strips off the trailing ' dollars' and changes type to int
price['price'] = price['price'].str.replace(' dollars', '').astype('int')

# room_type has case inconsistency
# so I'll just lowercase everything
room_type['room_type'] = room_type['room_type'].str.lower().astype('category')

# converting last_review to datetime
last_review['last_review'] = pd.to_datetime(last_review['last_review'])

# SOLUTION

# file to print to
filename = 'info.md'

# earliest and latest reviews
first_reviewed = last_review['last_review'].min()
last_reviewed = last_review['last_review'].max()

# number of private rooms
nb_private_rooms = room_type['room_type'].value_counts()['private room']

# average listing price
avg_price = round(price['price'].mean(), 2)

# output
with open(filename, 'w') as f:
    print('Earliest review: ' + str(first_reviewed), file=f)
    print('Latest review: ' + str(last_reviewed), file=f)
    print('Number of private rooms: ' + str(nb_private_rooms), file=f)
    print('Average price: ' + str(avg_price), file=f)
