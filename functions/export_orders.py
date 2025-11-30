import boto3

from common import resource_name, to_json

dynamodb = boto3.resource("dynamodb")
s3 = boto3.resource("s3")

orders = dynamodb.Table(resource_name("orders"))
ws_subscriptions = dynamodb.Table(resource_name("ws-order-subscriptions"))

ingesta = s3.Bucket(resource_name("ingesta"))


def handler(event, context):
    orders_resp = orders.scan()
    body = "\n".join([to_json(order) for order in orders_resp["Items"]])
    ingesta.put_object(Key="orders/orders.json", Body=body)

    subs_resp = ws_subscriptions.scan()
    body = "\n".join([to_json(sub) for sub in subs_resp["Items"]])
    ingesta.put_object(
        Key="ws-order-subscriptions/ws-order-subscriptions.json", Body=body
    )
