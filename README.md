# Honeycode certification app and data
Honeycode is a AWS service to create websites from spreadsheets. It allows upto 20 people on the application for free, who need ids to consume it. It can also be integrated with SSO for larger companies, and can then be shared internally. 
This lab is to demonstrate how to create a certification website using honeycode, and create a API gateway to send data from a lambda function to a Slack channel, and using tokens to make sure only your slack channel can get response back from the table. 
The key here is that once you get the application to send to lambda, then you can use any services inside of AWS. 

## Experiment: 

You have been asked to provide a way to track all your employees from a manager level to show how many have been certified. Your organisation has just decided to invest in your technical teams and are providing training courses, you want to allow anyone in your slack channel to be able to check who has which certifications and also send details for updates to your channel if someone does get certified. 

## Setup instructions:

### Pre-requirements
[00_create_honeycode_account](00_create_honeycode_account/README.md)

[01_create_slack_account](01_create_slack_channel/README.md)

### Lab 1 - Create HoneyCode workbook and certification table
[10_create_workbook](10_create_workbook/README.md)

[11_create_certification_table](11_create_certification_table/README.md)

[12_upload_sample_data_into_tables](12_upload_sample_data_into_tables/README.md)

### Lab 2 - Build application screens and connect them to the datasource ( tables )
[20_build_application](20_build_application/README.md)

### Lab 3 - Using functions, hidden fields and buttons
[30_create_functions](30_create_functions/README.md)

### Lab 4 - Intergtrating Slack via a Python API built and deployed by SAM [Serverless applicaiton Model](https://aws.amazon.com/serverless/sam/)
[40_create_SAM_API](40_create_SAM_API/README.md)
