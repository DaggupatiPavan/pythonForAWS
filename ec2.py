import boto3
from botocore.exceptions import NoValidUpdatesError

ec2 = boto3.resource('ec2')

# Define the EC2 instance details
instance_type = 't2.micro'
ami_id = 'ami-0c94855ba95c71c99'  # Replace with your desired AMI ID
key_name = 'my_key_pair'  # Replace with your key pair name

try:
    # Create an EC2 instance
    instance = ec2.create_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name
    )

    print(f"EC2 instance {instance[0].id} created successfully!")

except NoValidUpdatesError as e:
    print(f"Failed to create EC2 instance: {e}")

# creating ec2
