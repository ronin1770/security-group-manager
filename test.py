from aws_security_group import *
import pprint
from aws_logging import *

if __name__ == "__main__":
	#Testing creating a new VPC
	_logging = aws_logging()
	pp = pprint.PrettyPrinter(indent=4)
	_logging.create_log("info", "Initializing the class");
	asg = aws_security_group()

	"""

	#Allow SSH from specific IP
	#Allow Web acccess globally

	rules = [ 
				{ 'FromPort':22, 'ToPort' : 22, 'IpProtocol':'tcp', 'IpRanges':[ {'CidrIp':'<YOUR-IP-ADDRESS>/32', 'Description':'SSH access from Home'}] },  
				{ 'FromPort':80, 'ToPort' : 80, 'IpProtocol':'tcp', 'IpRanges':[ {'CidrIp':'0.0.0.0/0', 'Description':'Global web access'}] }
			]



	# Create a new security group 
	
	new_sg_name 		= "Test_SG"	
	new_sg_description 	= "This is a test SG for testing this method"
	_logging.create_log("info", "\n\nCreating new Security Group: " + new_sg_name)

	new_sg 				= asg.create_security_group( new_sg_name, new_sg_description, rules)
	_logging.create_log("info", "\n\nNew SG created....")
	pp.pprint( new_sg )


	# Create a new VPC 

	vpc_name 	= "Test-VPC"
	cidr_block 	= "10.1.0.0/16"
	_logging.create_log("info", "\n\nCreating new VPC: " + vpc_name)
	created_vpc	= asg.create_VPC(vpc_name, cidr_block)

	pp.pprint(created_vpc)


	# Getting all of the VPC for AWS region specified in the configuration 

	_logging.create_log("info", "\n\nGetting the list of VPCs");
	vpcs = asg.get_VPCs()
	pp.pprint(vpcs)

	# Get the Security Group by name 
	_logging.create_log("info", "\n\nGetting the security group by name: " + new_sg_name );
	sg = asg.get_security_group_by_name(new_sg_name)

	_logging.create_log("info", "\n\nSecurity group information for : " +  new_sg_name + " has been retrieved")
	pp.pprint(sg)

	# Getting the DHCP Options 

	vpc_id = "<Enter your VPC-ID>"
	_logging.create_log("info", "\n\nGetting the dhcp_otions of vpc_id: " + vpc_id );
	dhcp_otions = asg.get_VPC_DHCP_options(vpc_id) 

	pp.pprint(dhcp_otions)
	"""