import boto3
import json

lambda_client = boto3.client("lambda")


def invoke_summary_lambda(text: str):

    payload = {
        "text": text,
    }

    response = lambda_client.invoke(
        FunctionName="summary-function",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    return response