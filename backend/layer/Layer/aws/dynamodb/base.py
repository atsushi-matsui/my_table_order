import boto3
import logging

from boto3.dynamodb.conditions import Key

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class DynamoDB:

    __slots__ = ['_db']

    def __init__(self):
        self._db = boto3.resource('dynamodb')

    def _get_item(self, key):
        """
        アイテムを取得する

        Parameters
        ----------
        key : dict
            取得するアイテムのキー

        Returns
        -------
        response : dict
            レスポンス情報

        """
        logger.debug('key=%s', key)

        try:
            response = self._table.get_item(Key=key)
        except Exception as e:
            raise e
        
        return response.get('Item', {})

    def _query(self, keyName, keyValue):
        '''
        クエリを使用してItemを取得
        Parameters
        ----------
        keyName : Str
        キーの名前
        keyValue : Str
        キーの値
        Returns
        -------
        items : list
            対象アイテムのリスト
        '''
        logger.debug('keyName=%s', keyName)
        logger.debug('keyValue=%s', keyValue)

        try:
            response = self._table.query(
                KeyConditionExpression=Key(keyName).eq(keyValue)
            )
        except Exception as e:
            raise e
        
        return response['Items']