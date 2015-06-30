from keystoneclient.v2_0 import client as kclient
from novaclient import client as nclient
keystone = kclient.Client(username='admin', password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
predef_tenants = ['admin','demo','service','invisible_to_admin']
tenants = []
tenants_id = []
tenans_list = keystone.tenants.list()
for i in range(len(tenans_list)):
	if tenans_list[i].name not in predef_tenants:
		tenants.append(str(tenans_list[i].name))
		tenants_id.append(str(tenans_list[i].id))

predef_users = ['admin','demo','nova','heat','glance','cinder','neutron']
for tenant in tenants_id:
	keystone_user = kclient.Client(username='admin', password='secret123', tenant_id=tenant, auth_url="http://127.0.0.1:5000/v2.0")
	#print keystone_user.users.list(tenant)
	users_list = keystone_user.users.list(tenant)
	if users_list:
                for i in range(len(users_list)):
			if users_list[i].username not in predef_users:
				users_list[i].delete()
