#!/usr/bin/python

from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
from neutronclient.neutron import client as neclient
keystone = kclient.Client(username='admin', password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
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
	neutron = neclient.Client('2.0',username='admin',password='secret123', tenant_id=tenant , auth_url="http://127.0.0.1:5000/v2.0")
	neutron_list = neutron.list_networks()
	if neutron_list['networks']:
		for i in range(len(neutron_list['networks'])):
			if neutron_list['networks'][i]['tenant_id']== tenant:
				neutron.delete_network(neutron_list['networks'][i]['id'])
