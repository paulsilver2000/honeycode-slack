# LAB4 - Create API call

## Create SAM installation on CLOUD9
We will setup a cloud9 environment and then run a SAM deployment into us-west-2. Note at the time of writing, there is only 1 region for Honeycode, but once this is opened choose your required region of choice. 

Open the AWS console, go to us-west-2 (Oregon) region, click the cloud9 environment. Keep all the defaults and use amazon-linux-2 for the machine type. 

On the cloud9 environment call it slack. Click next and then create the environment. Once it has installed, it will have the required SAM
 and AWS cli installed. 

Next we will create a SAM stack creating a API gateway, lambda function and connectivity to the honeycode API calls to get the data from the tables. 

The SAM details are located here: [SAM template](/api_calls/template.yaml), copy the sam template into the environment directory and edit it in the IDE. 

Open the template as we need to add some parameters here:
``` yaml
     Environment:
        Variables:
          workbookId: 'XXX'
          slackchannelToken: 'XXX'
          channel: 'XXX'
```

In order to get the ARN details, we need to setup the honeycode to talk to our AWS account. To do this, click on the teams ID, then click connect to an AWS account. 

![getArn](/images/accountaws.png)

Add your 12 digit account id here.

![consoleupdate](/images/gotoconsole.png)

On the console go to the AWS searchbar and type in Honeycode. 

![consoleupdate](/images/honey.png)

You can get this from your AWS console and look under your id you are logged into and see the Account details. 

Once approved you will be able to use the AWS services with honeycode. Cool. 

![consoleupdate](/images/accept.png)

Finally type in Approve and click approve.

To get the workbookId details, we do this by going to the honeycode builder and right click on any button and click on and it has an option - `Get Arn and IDs` - click here and 

![getArn](/images/getArn.png)


Copy the workbook-id and put it in the variables for the template.yaml file. 

### Webhook for slack channel
We will need to create a webhook in the slack channel to call our API.  

In the channel we created ealier, we called it 'honeycode' so put this in the environment variable. 



### Create slash command for Slack channel
On the slack website we need to create a webhook to now hit the API call and take the token from this channel to add into the lambda function. 

On the SLACK website, go to your channel, and click on settings and administration, and click on manage apps. Click on the Search app and click `slash command`. 

On the results, choose the slash command. 
![webhook](/images/webhooks.png)

Add to slack, and for the command type in /getcert
![addslack](/images/addslack.png) Now **Add Slash Command Integration**

At the bottom click on the Save Integration button. 

Once this has been added, it will provide details for the token. In the outgoing Data, there is a Token which we will copy and put into the lambda function SAM template.

### Run the SAM template on the cloud9 environment and take the details of the API call. 
Update the template.yaml file with the token details. 
template.yaml 
```yaml
          slackchannelToken: 'XXX'
```

We are now ready to create the SAM deployment.
Clone or copy this repo into the cloud9 environment and go to the api_calls/honeycode-slack directory. Overwrite the template.yaml with the one you created. 



Now run the sam deployment
```bash
cd api_calls/honeycode-slack
sam build
sam deploy --guided
Stack Name : honeycode
AWS region : us-west-2
Confirm changes before deploy : N
Allow SAM CLI IAM role creation : Y
SlackHoneyCodeFunction may not have authorization defined, Is this okay? : Y
Save arguments to configuration file [Y/n]: Y
SAM configuration file [samconfig.toml]:
SAM configuration environment [default]:
```

In the outputs, this will now have the API endpoints to test. 

Lets update the slash command URL with this URL from the outputs of SlackHoneyCodeApi, it will look something like `https://XXX.execute-api.us-west-2.amazonaws.com/Prod/honeycode_slack/`

Go back to your slack channel and click on settings and administration and then click on manage apps. Click on the Custom Integrations setting and notice there is one called Slash Commands. Click on this and fill in the details as below:

![addslack](/images/slack.png)

Click on the configuration tab 
![addslack](/images/configslack.png)

In the Integration Settings:
``` bash
Command: /getcert
URL: https://XXX.execute-api.us-west-2.amazonaws.com/Prod/honeycode_slack/
Method: POST
Token: leave default
Customize Name: leave default
Preview Message: leave default
Click tick box Show this command in the autocomplete list
Usage hint: <Name: XXX>

Save Integration

```
Test if this works, go to the honeycode channel, and type in /getcert

![getcert](/images/getcert.png)

Type in a name that is in the certification table and confirm it returns the certs in the list.

`/getcert Name: Paul Silver`

![output](/images/certname.png)

If there are any errors, look at the lambda function and test with the events json file changing the Id's: "body": "token=<Your token>"

To clean up:

Remove the cloud9 environment
Delete the cloudformation SAM stack you created
Delete the slack channel
Delete the honeycode account

Interested in the mentor or learning more, go here: 
![mentor](/images/DevAx.png)
