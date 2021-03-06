#!/usr/bin/python

from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
from neutronclient.neutron import client as neclient
import sys
import os
import getopt


def main(argv):
	try:
	        opts, args = getopt.getopt(argv, "ha:", ["help", "admin_pass="])
	except getopt.GetoptError:                                
	        sys.exit(2)
	
	for opt, arg in opts:       
	        if opt in ("-h", "--help"):        
	                sys.exit()        
	        elif opt in ("-a", "--admin_pass"):
	                admin_pass = arg
	
	
	keystone = kclient.Client(username='admin', password=admin_pass, tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
	predef_tenants = ['admin','demo','service','invisible_to_admin']
	tenants = []
	tenants_id = []
	tenans_list = keystone.tenants.list()
	for i in range(len(tenans_list)):
		if tenans_list[i].name not in predef_tenants:
			tenants.append(str(tenans_list[i].name))
			tenants_id.append(str(tenans_list[i].id))
	
	
	for tenant in tenants_id:
		#print tenant
		neutron = neclient.Client('2.0',username='admin',password=admin_pass, tenant_id=tenant , auth_url="http://127.0.0.1:5000/v2.0")
		neutron_list = neutron.list_floatingips()
		#print neutron_list
		if neutron_list['floatingips']:
			for i in range(len(neutron_list['floatingips'])):
				if neutron_list['floatingips'][i]['tenant_id']== tenant:
					neutron.delete_floatingip(neutron_list['floatingips'][i]['id'])
	
if __name__ == "__main__":
    main(sys.argv[1:])
