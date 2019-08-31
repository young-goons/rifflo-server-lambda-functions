import boto3

batch = boto3.client('lambda')

response = batch.update_function_code(
    FunctionName='audio_segmentation',
    S3Bucket='rifflo-server-lambda-functions',
    S3Key='audio_segmentation/lambda_audio_segmentation.zip',
    Publish=True
)

print(response)