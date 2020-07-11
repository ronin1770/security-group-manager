from aws_security_group import *
import pprint
from aws_logging import *

if __name__ == "__main__":
	#Allow SSH from specific IP
	#Allow Web acccess globally
	rules = [ 
				{ 'FromPort':22, 'ToPort' : 22, 'IpProtocol':'tcp', 'IpRanges':[ {'CidrIp':'202.47.32.55/32', 'Description':'SSH access from Home'}] },  
				{ 'FromPort':80, 'ToPort' : 80, 'IpProtocol':'tcp', 'IpRanges':[ {'CidrIp':'0.0.0.0/0', 'Description':'Global web access'}] }
			]

	_logging = aws_logging()
	pp = pprint.PrettyPrinter(indent=4)

	_logging.create_log("info", "Initializing the class");
	asg = aws_security_group()

	new_sg_name = "Test_SG"	
	new_sg_description = "This is a test SG for testing this method"
	_logging.create_log("info", "Creating new Security Group: " + new_sg_name)
	new_sg = asg.create_security_group( new_sg_name, new_sg_description, rules)
	_logging.create_log("info", "New SG created....")
	pp.pprint( new_sg )

	
	_logging.create_log("info", "Getting the list of VPCs");
	vpcs = asg.get_VPCs()

	#Region is selected in the configuration.py
	_logging.create_log("info", "Total VPCS found for the selected region: " + str(len(vpcs)) );

	
	pp.pprint(vpcs)
	

	_logging.create_log("info", "Get the Subnet ID. Please note this method needs to revised to take vpc_id as an arugment");	
	subnets = asg.get_subnet_id()

	_logging.create_log("info", "Total subnets found: " + str(len(subnets)) )
	pp.pprint(subnets)

	_logging.create_log("info", "Getting Security Group by name....")
	sg = asg.get_security_group_by_name(new_sg_name)

	_logging.create_log("info", "Security group information for : " +  new_sg_name + " has been retrieved")
	pp.pprint(sg)