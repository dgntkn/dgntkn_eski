from jinja2 import FileSystemLoader, Environment
loader = FileSystemLoader('c:/Users/davutd/Documents/github/python temelleri/automation/dir1')
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

device_template = env.get_template('device_config.j2')
render_device = device_template.render(route='172.28.0.0/16',
                                       next_hop='10.13.106.1',
                                       name='ge-0/0/0',
                                       vlan='15',
                                       ip_address='10.13.106.2',
                                       hostname='qfx1')

print(str(render_device))