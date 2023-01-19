import boto3

sqs = boto3.resource('sqs')


#Creating a "Standard" SQS in Python Boto3
queue = sqs.create_queue(QueueName='Week15Messages')
print(queue.url)
print(queue.attributes)


#Created lambda function and message in AWS console

import json 
import boto3 
import datetime as datetime

#lambda function with datetime

def lambda_handler(event, context): 
    current_datetime = datetime.datetime.now()
    string_date = current_datetime.strftime("%A, %B %d, %Y %H:%M:%S")
    
#SQS Fuction with URL link

    sqs = boto3.client('sqs')
    response = sqs.send_message(
    QueueUrl ="https://sqs.us-east-2.amazonaws.com/135662092194/Week15Messages",
    MessageBody=string_date)
    return {
    'statusCode': 200,
    'body': json.dumps('Lambda Function is for SQS!')
}
