#!/usr/bin/env python3

import argparse, boto3

parser = argparse.ArgumentParser(description='AWS EC2 Auto Scale Tool', prog="auto_scale", usage="%(prog)s [options]")
parser.add_argument('--desired_capacity', help="Desired capacity for the auto scaling group")
parser.add_argument('--list', action='store_true', help="List Autoscaling groups")
parser.add_argument('--as_group', help="Auto Scale group Name")
args = parser.parse_args()

#creds need to be in ~/.aws/credentials file
# [Credentials]
# aws_access_key_id = YOURACCESSKEY
# aws_secret_access_key = YOURSECRETKEY

client = boto3.client('autoscaling')

def get_auto_scale_groups():
    auto_scale_groups = client.describe_auto_scaling_groups()

    for group in auto_scale_groups['AutoScalingGroups']:
        print("AutoScalingGroupName: {0}".format(group['AutoScalingGroupName']))
        print("DesiredCapacity: {}".format(group['DesiredCapacity']))
        print("MinSize: {}".format(group['MinSize']))
        print("MaxSize: {}".format(group["MaxSize"]))
        print("Instances: ")
        for i in group['Instances']:
            print("\tInstanceId: {}".format(i['InstanceId']))
            print("\tInstanceType: {}".format(i['InstanceType']))
            print("\tAvailabilityZone: {}".format(i['AvailabilityZone']))
            print("\tStatus: {}, {}".format(i['LifecycleState'], i['HealthStatus']))
            print(" ")

def update_capacity(capacity, group_name):
    capacity = int(capacity)
    response = client.update_auto_scaling_group(AutoScalingGroupName=group_name, MinSize=capacity, DesiredCapacity=capacity)


if args.list == True:
    get_auto_scale_groups()

if args.desired_capacity != None:
    get_auto_scale_groups()
    update_capacity(args.desired_capacity, args.as_group)
    get_auto_scale_groups()