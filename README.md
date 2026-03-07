# Boston Civic Data Analysis

Hello, my name is Murad Eyvazov, and this is a small data analysis project that I created using the 311 service request dataset provided by the Boston Open Data Portal.

The purpose of this project is to demonstrate the use of civic data to gain insights into the operations of the city and to identify patterns in the types of issues that are reported to the local government.

# Project Details

analysis.py            → Python script for analysis

charts/                → Generated visualizations

README.md              → Project description

Skills demonstrated: Python; Data Analysis; Data Visualization; Public Data

Dataset Source: Boston 311 Service Requests; Boston Open Data Portal  
https://data.boston.gov/

## How to Run

1. Install required libraries: pip install pandas matplotlib seaborn

2. Run the analysis script: python analysis.py

The script will generate charts showing patterns in Boston 311 service requests

## What I Did

In this project, I analyzed the open civic data provided by the city of Boston using Python programming to examine the service requests that are submitted to the local government by the people of Boston.

The patterns that are analyzed in this project are:

the most common types of service requests
the patterns in the volume of service requests over the course of the year
the departments that handle the most service requests

## Tools Used

Python

Pandas for data analysis

Matplotlib and Seaborn for data visualization

## Project Output and Observations

Using this dataset, I created several visualizations to gain insights into the patterns in the 311 service requests in the city of Boston.

### Top Complaint Topics (charts/top_topics.png)

This chart displays the most frequently reported issues that are submitted to the 311 system.
Based on the sample data, animal-related complaints and street light outages seem to be among the most common issues, as depicted in the graph below. This implies that a significant portion of the city’s population is concerned with how the city maintains its infrastructure and how animal-related issues are being addressed.

### Requests by Month (charts/monthly_requests.png)

The following visualization aims to reveal the changes in the number of requests over time, i.e., how the number of requests varies by month of the year.
The data implies that the number of requests is increasing towards the end of the year, and this may be due to some factors such as the weather, among others.

### Top Assigned Departments (charts/top_departments.png)

The following chart reveals the city department with the highest number of requests, i.e., the department with the highest number of requests assigned to it.
The data implies that animal-related issues and the public works department are responsible for handling a significant number of requests, and this implies that the department is playing a major role in the operation of the city.

### Department Response Times (charts/response_times.png)

This chart compares the average time different city departments take to close service requests. 
From the sample analyzed, Animal Care & Control and Parks & Recreation appear to have faster average response times than some other departments, while larger operational departments such as Public Works and the Boston Transportation Department handle requests with longer average closure times. This may reflect differences in case complexity, workload, or the type of issues each department manages.

## Why This Project

I created this project with the main aim of learning how data helps in decision-making for the city. Data related to 311 requests helps in creating insights into how city departments respond to issues related to the city’s residents.
