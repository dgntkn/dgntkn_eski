from jinja2 import Template, Environment

#ipaddr_template = Template('{{interface}} has IP address {{ip_address}}')

#interface1 = ipaddr_template.render(interface='Gi0/2/0', ip_address='10.1.1.1')

#print(str(interface1))

interfaces = [{'interface': 'ge-0/0/2', 'ip_address': '10.1.1.9'}, ##############################
              {'interface': 'ge-0/0/1', 'ip_address': '10.10.1.1'}, ### dictionary creating ##
              {'interface': 'fxp0', 'ip_address': '172.16.1.1'}] ################################

env = Environment(trim_blocks=True, lstrip_blocks=True) ## We are first declaring an instance of Environment called env. #####
ipaddr_template = env.from_string('''                    
{% for item in interfaces %}
{{ item.interface }} has IP address {{ item.ip_address }}
{% endfor %}''')

render_1 = ipaddr_template.render(interfaces=interfaces)
print(str(render_1))

vlans = [{'vlan': 'VLAN10', 'vlan_id': 10},
         {'vlan': 'VLAN20', 'vlan_id': 20},
         {'vlan': 'VLAN30', 'vlan_id': 20}]

vlan_config = env.from_string('''
{% for item in vlans %}
    interface {{ item.vlan }} 
        no shut
        description {{ item.vlan }}
        encapsulation dot1q {{ item.vlan_id }}
{% endfor %}
}''')

vlan_config = str(vlan_config.render(vlans=vlans))
print(vlan_config)