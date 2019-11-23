from jinja2 import Environment
import yaml
from pprint import pprint

yaml_file = open("c:/Users/davutd/Documents/github/python temelleri/automation/part4.yml","r")
all_devices = yaml.load(yaml_file, Loader=yaml.FullLoader)
#pprint(all_devices)

env = Environment(trim_blocks=True, lstrip_blocks=True)
config_temp = env.from_string('''
conf t
hostname {{ device.hostname }}
{% for item  in device.interface %}
interface {{ item.name }}
ip address {{ item.ip_address }}
{% endfor %}
''')

for dev_number, device in enumerate(all_devices, 1):
    render_1 = config_temp.render(device=device)
    print('\nConfiguration for Device %s' % (dev_number))
    print('-'*30)
    print(str(render_1))