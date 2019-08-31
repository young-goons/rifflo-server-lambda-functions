import os

import boto3

from pydub import AudioSegment
from werkzeug.utils import secure_filename

os.environ['PATH'] = os.environ['PATH'] + ':' + os.environ['LAMBDA_TASK_ROOT']

AudioSegment.converter = os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'ffmpeg')
AudioSegment.ffmpeg = os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'ffmpeg')
AudioSegment.ffprobe = os.path.join(os.environ['LAMBDA_TASK_ROOT'], 'ffprobe')

SONG_BUCKET = 'rifflo-song-storage'
CLIP_BUCKET = 'rifflo-clip-storage'

s3_client = boto3.client('s3')
s3_bucket = boto3.resource('s3').Bucket(CLIP_BUCKET)


def lambda_handler(event, context):
    song_key = os.path.join(event['user_id'], event['song_file'])

    song_download_path = '/tmp/{}'.format(event['song_file'])
    s3_client.download_file(SONG_BUCKET, song_key, song_download_path)

    # assume the song_file is in FILE_NAME.FILE_FORMAT format
    # assume the song_file format is valid
    assert len(event['song_file'].split('.')) > 1
    file_name = '.'.join(event['song_file'].split('.')[:-1])
    file_format = event['song_file'].split('.')[-1]

    full_song = AudioSegment.from_file(song_download_path, format=file_format)

    clip = full_song[int(float(event['start_time']) * 1000):int(float(event['end_time']) * 1000)]
    clip_name = file_name + "_" + str(event['start_time']) + "_" +\
                str(event['end_time']) + '.' + file_format
    clip_local_path = os.path.join('/tmp', secure_filename(clip_name))
    clip.export(clip_local_path, format=file_format)

    clip_s3_path = os.path.join(event['user_id'], clip_name)
    s3_bucket.upload_file(clip_local_path, clip_s3_path)
