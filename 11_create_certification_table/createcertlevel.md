## Create other tables which will FILTER into the main Certification table

With the main table, there are a couple available. In this lab we will explain how we can ```FILTER``` to other tables which will pull in those values. 

As discussed earlier we want to show which certifications the employee has got, so we will now create 6 new tables all with the same details in them. 

We are going to now add 6 new tables each of them with the following columns in. Where Name is employee name, date is date of certification, and value is the unique value provided by the AWS testing centre. 

|Name   |Date   |Value  |

Name will be used as our primary filter.

As an alternative to this, a more scalable solution would be to  create 1 table and have an additional column called CertName and filter based off of this. This would scale better, but in this example we will just do the 6 tables for demonstration purposes. 

To create a new table click on the table bar and click the ```+```: 

![certification](/images/newtabcreate.png)

Click ```add a blank table```
 
![certification](/images/assarch.png)

Call the table AssArch, add in the columns ```Name Data Value```

![associate architect](/images/assarch.png)

Repeat so you now have a total of 6 new tables created with the table names below: 

- AssArch
- AssDev
- AssSysOps
- Practitioner




