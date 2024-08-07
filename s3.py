import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the name and region for the new bucket
bucket_name = 'my-new-bucket'
region = 'us-west-2'

# Create the bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    'LocationConstraint': region
})

print(f'Created S3 bucket {bucket_name} in {region}')
