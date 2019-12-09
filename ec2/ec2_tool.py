#!/usr/bin/env python3
import argparse, boto3

parser = argparse.ArgumentParser(description="AWS EC2 tool", prog="ec2_tool")
parser.add_argument("--list", help="List EC2 instances", action="store_true")
parser.add_argument("--start", help="InstanceId of EC2 instance to start")
parser.add_argument("--stop", help="InstanceId of EC2 instance to stop")
parser.add_argument("--term", help="InstanceId of EC2 instance to terminate")
args = parser.parse_args()

client = boto3.client('ec2')

def get_instances():
    response = client.describe_instances()
    instances = response['Reservations']
    title = "ec2 instances".upper()
    print(title)
    print(len(title) * "*")
    for i in instances:
        instance = i['Instances'][0]
        print("InstanceId: {}".format(instance['InstanceId']))
        for t in instance['Tags']:
            print("{}: {}".format(t['Key'], t['Value']))
        print("InstanceType: {}".format(instance['InstanceType']))
        print("AZ: {}".format(instance['Placement']['AvailabilityZone']))
        print("PublicDnsName: {}".format(instance['PublicDnsName']))
        for s in instance['SecurityGroups']:
            print("SecuirtyGroup: {}".format(s['GroupName']))
        print("State: {}".format(instance['State']['Name']))
        print("")

def get_ec2(ec2_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(ec2_id)
    print("InstanceId: {}".format(instance.instance_id))
    for t in instance.tags:
        print("{}: {}".format(t['Key'], t['Value']))
    print("Status: {}".format(instance.state['Name']))
    print("PublicDnsName: {}".format(instance.public_dns_name))
    print("PublicIpAddress: {}".format(instance.public_ip_address))
    print("AZ: {}".format(instance.placement['AvailabilityZone']))
    for s in instance.security_groups: 
        print("Security Group: {}".format(s['GroupName']))

def start_ec2(instance):
    response = client.start_instances(InstanceIds=[instance])

def stop_ec2(instance):
    response = client.stop_instances(InstanceIds=[instance])

def term_ec2():
    print("terminate some shit")


if args.list == True:
    get_instances()

if args.start != None:
    start_ec2(args.start)
    get_ec2(args.start)

if args.stop != None:
    stop_ec2(args.stop)
    get_ec2(args.stop)