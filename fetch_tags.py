import requests
import mysql.connector 

api_url = "https://api.stackexchange.com/2.3/tags"
params = {
    "site": "stackoverflow",
    "order": "desc",
    "sort": "popular",
    "pagesize": 10
}
# Data Processing
response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
  
else:
    print("Error occurred while fetching data from the API.")

for tag in data['items']:
    tag_name = tag['name']
    print(tag_name)

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    
   
    tags = data['items']
else:
    print("Error occurred while fetching data from the API.")

tag_names = [tag['name'] for tag in tags]
tag_statistics = [tag['count'] for tag in tags]

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()

    tags = data['items']

 
    tag_names = [tag['name'] for tag in tags]
    tag_statistics = [tag['count'] for tag in tags]

    
else:
    print("Error occurred while fetching data from the API.")
#data Storage


# Connect to the MySQL database
import mysql.connector

# Connect to the MySQL database
import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Swap@123',
    database='tagg'
)


cursor = connection.cursor()


processed_data = [
    {
        'name': 'tag1',
        'popularity': 10,
        'usage_count': 100,
        'timestamp': '2023-06-01 12:00:00'
    },
    {
        'name': 'tag2',
        'popularity': 5,
        'usage_count': 50,
        'timestamp': '2023-06-01 12:00:00'
    },
    {
        'name': 'tag3',
        'popularity': 15,
        'usage_count': 200,
        'timestamp': '2023-06-01 12:00:00'
    }
]

# Insert the processed data into the table
for tag in processed_data:
    query = "INSERT INTO tags (name, popularity, usage_count, timestamp) VALUES (%s, %s, %s, %s)"
    values = (tag['name'], tag['popularity'], tag['usage_count'], tag['timestamp'])
    cursor.execute(query, values)

# Commit the changes to the database
connection.commit()

# Close the cursor and database connection
cursor.close()
connection.close()
