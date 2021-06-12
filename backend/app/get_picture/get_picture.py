import logging
import json
from common import utils
from table.table_picture import TablePicture

# テーブルの操作クラスの初期化
picture_table_controller = TablePicture()
# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def _get_item_list(params):
    if 'lineId' in params:
        line_id = params['lineId']
    else:
        return

    items = picture_table_controller.get_item(line_id)
    logger.debug('items=%s', items)
    return items

def lambda_handler(event, context):
    try:
        items = _get_item_list(event['queryStringParameters'])
    except Exception as e:
        raise e
    
    reposeJson = {
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': json.dumps(items, default=utils.decimal_to_int, ensure_ascii=False)
        }

    logger.debug('reposeJson=%s', reposeJson)
    return reposeJson