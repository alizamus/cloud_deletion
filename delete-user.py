from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
keystone = kclient.Client(username='admin', password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
predef_tenants = ['admin','demo','service','invisible_to_admin']
tenants = []
tenans_list = keystone.tenants.list()
for i in range(len(tenans_list)):
	if tenans_list[i].name not in predef_tenants:
		tenants.append(str(tenans_list[i].name))

keystone_user = kclient.Client(username='admin', password='secret123', tenant_name='ali', auth_url="http://127.0.0.1:5000/v2.0")

tenants_list = keystone_user.users.list()
print tenants_list
