from keystoneclient.v2_0 import client
keystone = client.Client(username='admin';, password='secret123', tenant_name='admin', auth_url="http://127.0.0.1:5000/v2.0")
predef_tenants = ['admin','demo','service','invisible_to_admin']
tenants = []
tenans_list = keystone.tenants.list()
for i in range(tenans_list):
	if tenans_list[i] not in:
		tenants.append(tenans_list[i])

print tenants
