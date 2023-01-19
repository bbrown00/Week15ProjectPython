import boto3

sqs = boto3.resource('sqs')


#Creating a "Standard" SQS in Python Boto3
queue = sqs.create_queue(QueueName='Week15Messages')
print(queue.url)
print(queue.attributes)
