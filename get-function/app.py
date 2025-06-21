import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

# import requests


def lambda_handler(event, context):
    """Lambda function to get the current visitor count from DynamoDB."""
    try:
        response = table.get_item(Key={'ID': '1'})
        item = response.get('Item')
        if not item or 'visitors' not in item:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item or visitors field not found'})
            }
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            },
            'body': json.dumps({'visitors': int(item['visitors'])})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }