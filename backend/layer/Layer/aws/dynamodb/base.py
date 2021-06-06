import boto3

class DynamoDB:

    __slots__ = ['_db', '_table_name']

    def __init__(self, table_name):
        self._db = boto3.resource('dynamodb')
        self._table_name = table_name

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
        try:
            response = self._table.get_item(Key=key)
        except Exception as e:
            raise e

        return response.get('Item', {})