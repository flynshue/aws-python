import boto.ec2
from ec2_info import get_ec2_info

#creds need to be in ~/.boto file
# [Credentials]
# aws_access_key_id = YOURACCESSKEY
# aws_secret_access_key = YOURSECRETKEY

# create connect class
conn = boto.ec2.connect_to_region('us-east-1')

def terminate_ec2(conn, ec2_ids):
    conn.terminate_instances(ec2_ids)

def main():
    get_ec2_info(conn)
    ec2_ids = []
    ec2 = raw_input("\nENTER THE EC2 ID TO TERMINATE: ")
    print "\nTERMINATING AN EC2 INSTANCE WILL ALSO REMOVE UNDERLYING COMPONENTS, INCLUDING EBS VOLUME"
    ans = raw_input("\nARE YOU SURE YOU WANT TO TERMINATE? (y/n) ")
    if ans == "y":
        ec2_ids.append(ec2)
        print ""
        print "TERMINATING EC2 INSTANCES: {}".format(ec2_ids)
        print ""
        terminate_ec2(conn, ec2_ids)
        get_ec2_info(conn)
    else:
        print "\nExiting..."

if __name__ == '__main__':
    main()
