#1/usr/bin/env python
import random
# Step 1: Create a list of 15 unique cities
cities_list = [
    "New York", "London", "Paris", "Tokyo", "Berlin",
    "Sydney", "Dubai", "Moscow", "Beijing", "Rome",
    "Istanbul", "Toronto", "Mumbai", "Cape Town", "Kuala Lumpur"
]

# Step 2: Generate a list of 45 cities allowing duplicates
cities = [random.choice(cities_list) for _ in range(45)]

# Step 3: Assign random sales data to each city
sales_data = [[city, random.randint(1000, 5000)] for city in cities]

# Step 4: Aggregate sales data
aggregated_sales = []
for city, sales in sales_data:
    for entry in aggregated_sales:
        if entry[0] == city:
            entry[1] += sales
            break
    else:
        aggregated_sales.append([city, sales])

# Step 5: Sort the aggregated sales data in descending order
sorted_sales = sorted(aggregated_sales, key=lambda x: x[1], reverse=True)

# Step 6: Output the results
print("City-wise Total Sales:")
for city, total_sales in sorted_sales:
    print(f"{city}: {total_sales}")
