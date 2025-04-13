# Lab16_apisani-1
# Alex Pisani
# Aug 9 2024
# charts and plots ohio unemployment from 1973 to today using FRED data

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Define file path
file_path = 'C:\\Users\\Alex\\Desktop\\python code\\lab16\\OHUR.csv'

# Initialize lists to store data
dates = []
unemp_counts = []

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    
    # Read header
    header = next(reader)
    for i, column in enumerate(header):
        print(f"Column {i}: {column}")
    
    # Read data
    for row in reader:
        date_str = row[0]  
        fire_count = (row[1])
        
        # Convert date string to datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d') 
        
        dates.append(date)
        unemp_counts.append(fire_count)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(dates, unemp_counts, marker='o', linestyle='-')

plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.title('Ohio Unemployment from 1973 to 2024')
plt.grid(True)


plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator())
plt.gcf().autofmt_xdate()  # Rotate date labels for better readability

plt.tight_layout()
plt.show()