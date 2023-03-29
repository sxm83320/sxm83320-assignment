import boto3


sqs = boto3.client('sqs')


response = sqs.create_queue(QueueName='my-queue')
from config import queue_name


def send_message(message_body):
   
    response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']
    
  
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
    return response
response = send_message('Hello, world!')
print(response)