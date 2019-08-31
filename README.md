# rifflo-server-lambda-functions
Lambda functions used by the Rifflo Server.\
For better management of Lambda functions, instead of write Lambda function codes directly on the console,
we write code on the local machine, compress it in .zip file and upload it to S3 bucket to be used by the
Lambda function.

## audio_segmentation
* [audio_segmentation/lambda_build_audio_segmentation.sh](./audio_segmentation/lambda_build_audio_segmentation.sh)\
Zips all the files (dependencies and code) needed by the Lambda Function and uploads to S3.\
Need to be run every time the main handler file is modified.
* [audio_segmentation/lambda_create_audio_segmentation.py](./audio_segmentation/lambda_create_audio_segmentation.py)\
Creates the Lambda Function. Need to be run only once.
* [audio_segmentation/lambda_update_audio_segmentation.py](./audio_segmentation/lambda_update_audio_segmentation.py)\
Updates the Lambda Function. Need to be run every time Lambda Function needs to be modified.
* [audio_segmentation/lambda_audio_segmentation_handler](./audio_segmentation/lambda_audio_segmentation.zip)\
The file that is run when the Lambda Function is invoked.

### Setting up
*aws-cli* must be installed to create and update Lambda Functions from the client.\
Refer to this [documentation](https://docs.aws.amazon.com/cli/latest/userguide/install-linux-al2017.html) 
for aws-cli installation and this [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
for configuring aws-cli settings/authentication.
```bash
python3 -m venv lambda_env
source lambda_env/bin/activate
pip install -r requirements.txt
```

### Creating the Lambda Function
```bash
chmod a+x lambda_build_audio_segmentation.sh
./labmda_build_audio_segmentation.sh
python3 lambda_create_audio_segmentation.py
```

### Updating the Lambda Function
```bash
./labmda_build_audio_segmentation.sh
python3 lambda_update_audio_segmentation.py
```


### References
* ffmpeg and ffprobe binary files are from https://johnvansickle.com/ffmpeg/
