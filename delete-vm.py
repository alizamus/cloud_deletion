from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
keystone = kclient.Client(username='admin', password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
predef_tenants = ['admin','demo','service','invisible_to_admin']
tenants = []
tenans_list = keystone.tenants.list()
for i in range(len(tenans_list)):
	if tenans_list[i].name not in predef_tenants:
		tenants.append(str(tenans_list[i].name))
#print tenants

for tenant in tenants:
	nova = nclient.Client(2,'admin','secret123', tenant , "http://127.0.0.1:5000/v2.0",service_type="compute")
	for i in range(len(nova.servers.list())):
		compute_list = nova.servers.list(i)
		#print compute_list
		#print compute_list[0].id
		nova.servers.delete(compute_list[i].id)
		#print compute_list
