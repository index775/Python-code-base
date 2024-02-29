import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
#testing bot
# Create sample data
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

# Save data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Read data from the JSON file into a Pandas DataFrame
df = pd.read_json('data.json')

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Add a new column 'Salary' with random values using NumPy
df['Salary'] = np.random.randint(50000, 80000, size=len(df))

# Update the 'Age' column by adding 2 years
df['Age'] = df['Age'] + 2

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# Save the updated DataFrame to a new JSON file
df.to_json('updated_data.json', orient='records')

# Read data from the updated JSON file into a new Pandas DataFrame
updated_df = pd.read_json('updated_data.json')

# Display the new DataFrame
print("\nDataFrame from updated JSON file:")
print(updated_df)

# Plot a bar chart of 'Age' using matplotlib
plt.bar(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.show()
