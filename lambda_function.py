import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('genese-demo')

def lambda_handler(event, context):
    print (event)
    name = event['Name']
    email = event['Email']
    address = event['Address']
    description = event['Description']
    table.put_item(
            Item={
                'Name': name,
                'Address':address,
                'Description':description,
                'Email':email
            }
        )

    return 'added record successfully'
        
 


            
