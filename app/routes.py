from app import app
import os
import boto3

@app.route('/health')
def health():
    return {
        "status": "Healthy!",
        "container": os.environ.get('CONTAINER_IMAGE', 'khalilj/zesty-secret-retriever')
    }

@app.route('/secret')
def secret():
    code_name = os.environ.get('CODE_NAME')
    dynamodb = boto3.client('dynamodb', region_name='us-west-2',
        endpoint_url=os.environ.get('DYNAMO_ENDPOINT', 'http://localhost:8000'))
    response = dynamodb.get_item(
        TableName='devops-challenge',
        Key={
            'codeName': {'S': code_name}
        }
    )

    return {
        "codeName": code_name,
        "secretCode": response['Item']['secretCode']['S']
    }
