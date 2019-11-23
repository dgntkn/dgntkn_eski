from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader('c:/Users/davutd/Documents/github/python temelleri/automation/dir1')
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

route_template = env.get_template('static_route.j2')
render_route = route_template.render(route='172.28.0.0/16', next_hop='10.13.106.1')

print(str(render_route))


