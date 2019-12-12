
# Python scripts that will interact with AWS EC2 instances

Will need to create ~/.aws/credentials file that contains the access key/secret

Example of the ~/.aws/credentials file

    `[Credentials]`
    `aws_access_key_id = YOURACCESSKEY`
    `aws_secret_access_key = YOURSECRETKEY`

## Will need to install boto


    pip install boto3 --user

    pip3 install boto3 --user

## ec2_tool.py usage

    ./ec2_tool.py --help
    usage: ec2_tool [-h] [--list] [--start START] [--stop STOP] [--term TERM]

    AWS EC2 tool

    optional arguments:
    -h, --help     show this help message and exit
    --list         List EC2 instances
    --start START  InstanceId of EC2 instance to start
    --stop STOP    InstanceId of EC2 instance to stop
    --term TERM    InstanceId of EC2 instance to terminate

## Getting Information on EC2 instances

    ./ec2_tool.py --list
    EC2 INSTANCES
    *************
    Name: Essentials-webserver-01b
    InstanceId: i-instanceId
    InstanceType: t2.micro
    Status: stopped
    PublicDnsName: 
    PublicIpAddress: None
    SecurityGroup: EssentialsSG
    AZ: us-east-1b

    Name: Essentials-webserver-01a
    InstanceId: i-instanceId
    InstanceType: t2.micro
    Status: stopped
    PublicDnsName: 
    PublicIpAddress: None
    SecurityGroup: EssentialsSG
    AZ: us-east-1e

    Name: Openshift-Master
    Application: Openshift-Origin
    InstanceId: i-instanceId
    InstanceType: t2.medium
    Status: stopped
    PublicDnsName: 
    PublicIpAddress: None
    SecurityGroup: aws-WebSever
    AZ: us-east-1d

## Shutting down EC2 instance

    ./ec2_tool.py --stop i-instanceId
    Name: Essentials-webserver-01a
    InstanceId: i-instanceId
    Status: stopping
    PublicDnsName: ec2-x-x-x-x.compute-1.amazonaws.com
    PublicIpAddress: x.x.x.x
    AZ: us-east-1e
    Security Group: EssentialsSG

## Starting up EC2 instance
    ./ec2_tool.py --start i-instanceId
    Name: Essentials-webserver-01a
    InstanceId: i-instanceId
    Status: pending
    PublicDnsName: 
    PublicIpAddress: None
    AZ: us-east-1e
    Security Group: EssentialsSG

## Terminating EC2 instance

***This Will DESTROY components associated with EC2 instance, including the EBS Volume***

    This is work in progress.
