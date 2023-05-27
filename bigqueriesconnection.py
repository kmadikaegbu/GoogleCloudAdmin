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