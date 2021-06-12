import logging
import os
from aws.dynamodb.base import DynamoDB

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TablePicture(DynamoDB):  # ()内のクラスを継承する
    """TablePicture操作用クラス"""
    __slots__ = ['_table']  # インスタンス側で定義されたメンバ以外のメンバは持てなくなる

    def __init__(self):
        """初期化メソッド"""
        table_name = os.environ.get("PICTURE_DB")
        # TODO ログ出力
        super().__init__()
        # 基底クラスのメソッドを使って初期化：テーブル名のセットとdynamodbリソースの生成
        self._table = self._db.Table(table_name)

    def get_item(self, line_id):
        """
        データ取得

        Parameters
        ----------
        line_id : Str
            lineーID

        Returns
        -------
        item : dict
            画像情報

        """

        try:
            item = self._query('lineId', line_id)
        except Exception as e:
            raise e

        logger.debug('item=%s', item)
        
        return item