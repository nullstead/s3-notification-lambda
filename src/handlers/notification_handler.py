import json
import boto3
import os
import urllib.parse
from datetime import datetime

def lambda_handler(event, context):

    # Get environment variables
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']
    environment = os.environ['ENVIRONMENT']
    
    # Initialize SNS client
    sns = boto3.client('sns')
    
    try:
        # Extract bucket and object information from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        object_size = event['Records'][0]['s3']['object']['size']
        event_time = event['Records'][0]['eventTime']
        
        # Format the notification message
        message = f"""
        New file uploaded to S3 bucket:
        
        Environment: {environment}
        Bucket: {bucket_name}
        File: {object_key}
        Size: {object_size} bytes
        Timestamp: {event_time}
        """
        
        # Format the subject line
        subject = f"[{environment.upper()}] S3 File Upload Notification - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Publish message to SNS
        response = sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=subject
        )
        
        print(f"SNS Notification sent. MessageId: {response['MessageId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Notification sent successfully',
                'event': {
                    'bucket': bucket_name,
                    'object': object_key,
                    'timestamp': event_time
                }
            })
        }
        
    except Exception as e:
        print(f"Error processing S3 event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error: {str(e)}'
            })
        }