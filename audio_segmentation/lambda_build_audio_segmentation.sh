#!/usr/bin/env bash
MAINDIR=$(pwd)
rm lambda_audio_segmentation.zip
cd lambda_venv/lib/python3.6/site-packages/
zip -r ${MAINDIR}/lambda_audio_segmentation.zip .
cd ${MAINDIR}
zip -g lambda_audio_segmentation.zip lambda_audio_segmentation_handler.py ffmpeg ffprobe
aws s3 cp lambda_audio_segmentation.zip s3://rifflo-server-lambda-functions/audio_segmentation/
