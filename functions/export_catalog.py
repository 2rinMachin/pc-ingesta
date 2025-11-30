import boto3

from common import resource_name, to_json

dynamodb = boto3.resource("dynamodb")
s3 = boto3.resource("s3")

products = dynamodb.Table(resource_name("products"))

ingesta = s3.Bucket(resource_name("ingesta"))


def handler(event, context):
    products_resp = products.scan()
    body = "\n".join([to_json(product) for product in products_resp["Items"]])
    ingesta.put_object(Key="products/products.json", Body=body)
