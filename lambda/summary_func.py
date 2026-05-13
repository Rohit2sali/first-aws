import json
import boto3

def lambda_handler(event, context):
    """
    Triggered via API Gateway or Boto3.
    Expects: {'chat_history': '...'}
    """
    chat_text = event.get('chat_history', '')
    
    # A simple 'logic-based' summary for demo purposes.
    # In production, you'd use a small model like Pegasus or an API call.
    summary = f"Summary of conversation: {chat_text[:50]}..."
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Summary generated successfully',
            'summary': summary
        })
    }