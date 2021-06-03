import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import os

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def _scan(key, value=None):
    table_name = os.environ.get("ITEM_LIST_DB")
    print('table_name='+table_name)
    table = boto3.resource('dynamodb').Table(table_name)

    scan_kwargs = {}
    if value:
        scan_kwargs['FilterExpression'] = Key(key).eq(value)

    try:
        response = table.scan(**scan_kwargs)
    except Exception as e:
        raise e 
        
    print(response)

    return response['Items']

def lambda_handler(event, context):
    key = 'category_id'
    category = _scan(key)

    return {
        "statusCode": 200,
        "body": json.dumps(category, default=decimal_default_proc),
    }