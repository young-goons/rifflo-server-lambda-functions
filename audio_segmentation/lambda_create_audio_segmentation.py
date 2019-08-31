import boto3

batch = boto3.client('lambda')

response = batch.create_function(
    FunctionName='audio_segmentation',
    Runtime='python3.7',
    Role='arn:aws:iam::149421292640:role/lambda_full',
    Handler='lambda_audio_segmentation_handler.lambda_handler',
    Code={
            'S3Bucket': 'rifflo-server-lambda-functions',
            'S3Key': 'audio_segmentation/lambda_audio_segmentation.zip'
    },
    Description='Lambda function used for audio segmentation',
    Timeout=60,
    MemorySize=1024,
    Publish=True
)

print(response)