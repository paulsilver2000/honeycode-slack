#!/usr/bin/python3 
import boto3
import sys
import os
import json
from urllib import parse as urlparse

honeycode_client = boto3.client('honeycode')
workbook_id = os.environ['workbookId']
token = os.environ['slackchannelToken']
channel = os.environ['channel']

def check_table():
  ''' get the tableId to be used later for the other executions of honeycode'''
  response = honeycode_client.list_tables(workbookId = workbook_id)
  for table in response['tables']:
    try:
        if table['tableName'] == 'certifications':
          certId = table['tableId']
          return certId
    except: 
        sys.exit("error: cannot find table certification")

def check_if_certified(id, tableId, check):
    ''' iterate through all the Y and name to check if certified and respond in string '''   
    cert_names = []
    for test in check:
        response = honeycode_client.query_table_rows(
            workbookId = workbook_id,
            tableId = tableId,
            filterFormula = { "formula": f'=Filter(certifications,"certifications[Name]=% AND certifications[{test}]=%", "{id}" ,"Y")'} 
        )
        
        if len(response['rows'])>0:
            cert_names.append(test)
    if cert_names == []:
        text = id + " has no certs "
    else:
        text = "The following cert details for " + id + " has the following certs " + str(cert_names)
        print(text)
    return(text)

def lambda_handler(event, context):
    '''Provide an event where sends a username and then gets the response sent back to the SLACK channel created previously 
    '''
    pay_load = str(event['body'])
    msg_map = dict(urlparse.parse_qsl(pay_load))
    
    text = msg_map['text']
    print(text)
    id = text.split(':', 1)[-1].lstrip()
    command = text.split(':', 1)[0].lstrip().lower()
    print(command)
    print(id)
    slack_channel_token = msg_map['token']
    channel_name = msg_map['channel_name']
    'check if the token and the channel are the required ones, just to confirm that the table can only be spoken to securely'
    if slack_channel_token != token or channel_name != channel:
        return {
            "body": 'you have not got the correct token details, and the token is not matching, so we are not going further with this request',
            "statusCode": 403,
        }
        
    slack_text = ''
    if command == "name":
        cert_id = check_table()
        check = {"Practitioner", "ArchAss", "DevAss", "SysOpsAss"}
        slacktext = check_if_certified(id, cert_id, check)

        return { 
            "statusCode": 200,
            "headers": {'Content-Type': 'application/json; charset=utf-8'},
            "body": slacktext
        }