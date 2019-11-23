from jinja2 import Environment

interfaces = [{'interface': 'ge-0/0/0', 'ip_address': '192.168.1.1'},
              {'interface': 'ge-0/0/1', 'ip_address': '10.10.1.1'},
              {'interface': 'fxp0', 'ip_address': '172.16.1.1'}]

env = Environment(trim_blocks=True, lstrip_blocks=True)
ipaddr_template = env.from_string('''
{% for item in interfaces %}
{% if item.interface == 'fxp0' %}
interfaces {
    {{ item.interface }} {
        unit 0 {
            family inet {
                address {{item.ip_address}};
            }
        }
    }
}
{% endif %}
{% endfor %}''')

render_1 = ipaddr_template.render(interfaces=interfaces)
print(str(render_1))

set_template = '''{% set mgmt_interface = 'ge-0/0/0' %}
{% for item in interfaces %}
{% if item.interface == mgmt_interface %}
interfaces {
    {{ item.interface }} {
        unit 0 {
            family inet {
                address {{item.ip_address}};
            }
        }
    }
}
{% endif %}
{% endfor %}'''

int_template = env.from_string(set_template)
render_2 = int_template.render(interfaces=interfaces)

print(str(render_2))

