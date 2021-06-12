from decimal import Decimal

def decimal_to_int(obj):
    """
    Decimal型をint型に変換する。
    json形式に変換する際にDecimal型でエラーが出るため作成。
    主にDynamoDBの数値データに対して使用する。

    Parameters
    ----------
    obj : obj
        Decimal型の可能性があるオブジェクト

    Returns
    -------
    int, other
        Decimal型の場合int型で返す。
        その他の型の場合そのまま返す。
    """
    if isinstance(obj, Decimal):
        return int(obj)