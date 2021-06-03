from decimal import Decimal
import json
import boto3

def _load_movies(menus, dynamodb=None):
    if not dynamodb:
        table_name = os.environ.get("ITEM_LIST_DB")
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    for menu in menus:
        #year = int(movie['categoryId'])
        #title = movie['categoryName']
        table.put_item(Item=menu)


def lambda_handler(event, context):
    with open("../test_data/menu_01.json") as json_file:
        menu_list = json.load(json_file, parse_float=Decimal)
    _load_movies(menu_list)
