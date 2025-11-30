import boto3

from common import resource_name, to_json

dynamodb = boto3.resource("dynamodb")
s3 = boto3.resource("s3")

users = dynamodb.Table(resource_name("users"))

ingesta = s3.Bucket(resource_name("ingesta"))


def handler(event, context):
    users_resp = users.scan()
    body = "\n".join([to_json(user) for user in users_resp["Items"]])
    ingesta.put_object(Key="users/users.json", Body=body)
