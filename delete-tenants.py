from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
keystone = kclient.Client(username='admin', password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
predef_tenants = ['admin','demo','service','invisible_to_admin']
tenants = []
tenants_id = []
tenants_list = keystone.tenants.list()
if tenants_list:
	for i in range(len(tenants_list)):
		if tenants_list[i].name not in predef_tenants:
			tenants_list[i].delete()

