
# Python scripts that will interact with AWS EC2 instances

Will need to create a ~/.boto file that contains the access key/secret

Example of the ~/.boto file

    `[Credentials]`
    `aws_access_key_id = YOURACCESSKEY`
    `aws_secret_access_key = YOURSECRETKEY`

## Will need to install boto


    pip install boto

## Getting Information on EC2 instances

    python ec2_info.py

## Shutting down EC2 instance

    python ec2_shutdown.py

## Starting up EC2 instance

    python ec2_startup.py

## Terminating EC2 instance

***This Will DESTROY components associated with EC2 instance, including the EBS Volume***

    python ec2_terminate.py
