import json

def lambda_handler(event, context):
    print("sending hello world back")
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
