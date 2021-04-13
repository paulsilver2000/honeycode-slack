# Create a table function and load sample data

### Create a date format
As spreadsheets, you can create date functions and formats. Highlight the PractDate value, right click and press the format.

![formatdate](/images/formats.png)

On the right of the screen, click down to the Date option as we want this to be a date field, and set preferences to your requirements, e.g. 1/12/20. 

![formatdate](/images/setdatepract.png)

### Create a sum function for the total number of certs a person has. 

There are two ways to implement formula's on the app, one is to make a formula on the table and one we can make a formula on the app builder. This is an example the table, make note that you do not want to have to many formula's on the table as it means each update for a row or insert into the table will slow down for writes. You will need to work out what sort is best fit for the application. 

Find the `totalcerts` column we created, highlight it and put this formula in. 

```=SUM(IF([Practitioner]="Y",1,0)+IF([SysOpsAss]="Y",1,0)+IF([ArchAss]="Y",1,0)+IF([DevAss]="Y",1,0))```

This is using functions that can be used in your formula. In this example we have two functions being used. 

=SUM will add all the items in the brackets, and =IF will provide an output based off of the response. So ```=IF([DevAss])="Y",1,0)``` means that if there is a Y in DevAss column, then set this to 1, and the =SUM adds all the 1 valuse together to get the totalcerts value. We will use this later in the app builder. 

![totalcerts](/images/totalcerts.png)

## Load up Sample Data
There are a two of ways to load sample data:
1. Manual input of data
2. Upload bulk data

## 1. Manual input of data
Go to the ```certification``` table and click on the plus to create a new row, and fill in the fields "Name", "Manager", "Practitioner", PractDate,  and "Status". This is ideal for a couple of rows and for some testing.

![certification](/images/certaddrow.png)

There may be requirements to upload many new rows in the file, this is done by creating a csv file. You can chose to have the header or not, and you when you upload you can choose which one you would like to consume. 

To upload many rows, you can import a CSV file. 
An Example of this is below: 

``` bash
Name,Manager,Practitioner,PractDate,PractValue,ArchAss,ArchAssDate,ArchAssValue,DevAss,DevAssDate,DevAssValue,SysOpsAss,SysOpsAssDate,SysOpsAssValue,status,totalcerts
Fred Flinstone,Barny Rubble,N,,,N,,,,,,N,,,Permanent,
```

As you can see in this example, the header is included. 

Action an upload using the csv file located here [csv](12_upload_sample_data_into_tables/csv/certification.csv)

Click on the certication table, and the ![threebutton](/images/threebuttons.png) button and import data into this table. 

Use the certification.csv file to import the data into the table. 

![certification](/images/columns.png)

As you can see the header will provide you the option on which header on the csv file matches the header to the certification table. As the csv aligns exactly to the table columns we can click import. 

Your table should now have imported the sample data to be used in the next section. 
Notice at the end of the table, the formula created ealier has been applied on the new rows. 

![total](/images/total.png)

That is the completion of implementing the sample data and formulas.

We are now ready to build some application screens and login [Click here to continue](20_build_application/README.md)
