# Create a filter from one table to another 

## Filter creation

To do this we will be using a function in the table which will filter out the required row.  This Filter  will be linked to the other tables based on the name. 

![table joins](/images/certs.png)

On the tables bar, click on the certification table. 

Highlight the full column for practioner right click and choose format - 

![format ](/images/format.png)

Put the following formula in the Format field - 
```=FILTER(Practitioner,"Practitioner[Name]=[Name]")```

![formula ](/images/practformula.png)

Continue this for all the other 6 columns : 
| ColumnName | TableName | Formula |  
|---|---|---|
|Practitioner| Practitioner | ```=FILTER(Practitioner,"Practitioner[Name]=[Name]")```
|ArchAss  |  AssArch | ```=FILTER(ProArch,"ProArch[Name]=[Name]")```
|DevAss      | AssDev |```=FILTER(AssDev,"AssDev[Name]=[Name]")```
|SysOpsAss   |  AssSysOps |```=FILTER(ProArch,"ProArch[Name]=[Name]")```


Lets now put in some Data to test that the filter is working. 

Go to the certification tables, and create a new row with your name