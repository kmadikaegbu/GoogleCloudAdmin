#Create database and table for the staffing assistant

import mysql.connector

# Create a connection object
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pso_database"
)

# Create a cursor object
cursor = conn.cursor()

# Create the table
sql = """
CREATE TABLE PSOMasterTable (
    ldap VARCHAR(255),
    role VARCHAR(255),
    practice VARCHAR(255),
    skills VARCHAR(255),
    assignment1_startdate DATE,
    assignment1_enddate DATE,
    assignment2_startdate DATE,
    assignment2_enddate DATE,
    assignment_hours INT
)
"""

cursor.execute(sql)

# Commit the changes
conn.commit()

# Create a cursor object
cursor = conn.cursor()

# Get the table name
table_name = "PSOMasterTable"

# Create the dummy data
dummy_data = [
    ("hmaked", "AppMod Consultant", "AI", "Python, Java, SQL", "2023-05-01", "2023-05-17", "2023-06-01", "2023-06-17", 40),
    ("habdul", "Data SCE", "Data", "Selenium, JUnit, TestNG", "2023-05-02", "2023-05-18", "2023-06-02", "2023-06-18", 30),
    ("almad", "Data Consultant", "Data", "Python, R, SQL", "2023-05-03", "2023-05-19", "2023-06-03", "2023-06-19", 20),
    ("apdbef", "infra Consultant", "Infra", "GKE, Tableau, SQL", "2023-05-04", "2023-05-20", "2023-06-04", "2023-06-20", 10),
    ("tommyd", "Delivery Manager", "Delivery management", "PMI, PRINCE2, MS Project", "2023-05-05", "2023-05-21", "2023-06-05", "2023-06-21", 0)
]

# Insert the dummy data into the table
for row in dummy_data:
    sql = """
INSERT INTO {} (ldap, role, practice, skills, assignment1_startdate, assignment1_enddate, assignment2_startdate, assignment2_enddate, assignment_hours)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""".format(table_name)

    cursor.execute(sql, row)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Confirm the creation of the database and table
# Create a cursor object
cursor = conn.cursor()

# Get the table name
table_name = "PSOMasterTable"

# Get the data from the table
sql = """
SELECT * FROM {}
""".format(table_name)

cursor.execute(sql)

# Print the data
rows = cursor.fetchall()

for row in rows:
    print(row)
# Convert the data to JSON format
json_data = json.dumps([row for row in cursor.fetchall()], indent=4)

# Print the JSON data
print(json_data)

# Close the connection
conn.close()
print("Database and table created successfully!")
