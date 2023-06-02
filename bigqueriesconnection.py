import os
import io
from google.cloud import bigquery

# Get the project ID from the environment variable
project_id = os.environ["cloud-llm-preview1"]

# Create a BigQuery client
client = bigquery.Client()

# Set the dataset and table name
dataset_name = "darpans"
table_name = "staffing_assist_sample_data"

# Run a query
query = """
SELECT *
FROM `{dataset_name}`.`{table_name}`
""".format(dataset_name=dataset_name, table_name=table_name)

# Read the results of the query
results = client.query(query)

# Print the results
for row in results:
    print(row)

# Convert the data to JSON format
json_data = json.dumps([row for row in cursor.fetchall()], indent=4)

# Print the JSON data
print(json_data)

