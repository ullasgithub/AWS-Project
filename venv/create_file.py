import boto3
s3 = boto3.client('s3')

with open('testfile.txt', 'rb') as data:
    s3.upload_fileobj(data, 'practice-test1', 'testfile')