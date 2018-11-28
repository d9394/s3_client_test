import boto3
from botocore.client import Config
s3_client = boto3.client('s3', endpoint_url='https://58.253.xxx.xxx:8443',
                         aws_access_key_id='XOHcOE0zAlKxH0bq.......',
                         aws_secret_access_key='2PDy8poXSAZrrvnafIr3aWxwiC5eNGjJC.......',
 #                        region_name='cn-north-1',
                         verify=False,
                         config=Config(signature_version='s3'))
bucket_list = s3_client.list_buckets()
print bucket_list

bucket_info = s3_client.head_bucket(Bucket='backup')

object_list = s3_client.list_objects(Bucket='backup')

object_info=s3_client.get_object(Bucket='backup', Key='20181128_backup/20181127/70.0.3538.110_chrome_installer64.zip')

s3_client.download_file('backup','20181128_backup/20181127/70.0.3538.110_chrome_installer64.zip','/root/chrome.zip')

s3_client.upload_file("/root/oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm", "backup", "20181127_backup/oracle.rpm",
  ExtraArgs={'ACL': 'public-read'})

#参考文档
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
#http://www.bubuko.com/infodetail-2378686.html
#https://blog.csdn.net/m0_37263637/article/details/80697920
