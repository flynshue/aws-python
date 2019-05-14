import boto.ec2

#creds need to be in ~/.boto file
# [Credentials]
# aws_access_key_id = YOURACCESSKEY
# aws_secret_access_key = YOURSECRETKEY

# create connect class
conn = boto.ec2.connect_to_region('us-east-1')

def get_ec2_info(conn):
    #get list of instances
    title = "\nLIST OF EC2 INSTANCES"
    print title
    print "*" * len(title)
    ec2_instances = conn.get_only_instances()
    for e in ec2_instances:
        instance_id = e.id
        state = "State: {}".format(e.state)
        tags = "Name: {}".format(e.tags["Name"])
        public_dns_name = e.public_dns_name
        ip_address = e.ip_address
        private_ip_address = e.private_ip_address
        instance_type = e.instance_type
        launch_time = e.launch_time
        print tags + "\n"
        print state.upper()
        print "Instance Type: {}".format(instance_type)
        print "Private IP: {}".format(private_ip_address)
        print "Public IP: {}".format(ip_address)
        print "Public DNS: {}".format(public_dns_name)
        print "Launch Time: {}".format(launch_time)
        print "EC2_ID: {} \n".format(instance_id)
        print "*" * len(tags)

def main():
    get_ec2_info(conn)


if __name__ == '__main__':
    main()
