import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g.; 'us-east-1'
region = 'ap-southeast-2'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = 'dbinstancename'

def lambda_handler(event, context):
    rds = boto3.client('rds', region_name=region)
    rds.start_db_instance(DBInstanceIdentifier=instances)
    print 'stopped your instances: ' + str(instances)
