gcloud sql create pso-master-db
gcloud sql connect pso-master-db --user=root --quiet

CREATE DATABASE PSOMasterTable;

USE PSOMasterTable;

CREATE TABLE PSOMasterTable (
  ldap VARCHAR(255),
  role VARCHAR(255),
  practice VARCHAR(255),
  skills VARCHAR(255),
  assignment1Startdate DATE,
  assignment1Enddate DATE,
  assignment2Startdate DATE,
  assignment2Enddate DATE,
  assignmentHours INT
);