import paramiko
import time
from jinja2 import Environment
import yaml
from pprint import pprint

def send_cmd(conn, command):
    conn.send(command + "\n")
    time.sleep(1.0)

def get_output(conn):
    return conn.recv(65535).decode("utf-8")


def main():
    yaml_file = open("c:/Users/davutd/Documents/github/pluralsight/device.yaml","r")
    all_devices = yaml.load(yaml_file, Loader=yaml.FullLoader)
    pprint(all_devices)

    devices = ['172.30.29.233', '172.30.29.232']
           
    host_dict = {
        "R1" : "show run | section vrf_definition",
        "R2" : "sh run vrf"
        }
    
    for device in devices:
        for hostname, vrf_cmd in host_dict.items():
            conn_params = paramiko.SSHClient()
            conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn_params.connect(
                hostname=device,
                port=22,
                username="davut",
                password="12345",
                look_for_keys=False,
                allow_agent=False,
                )

            conn = conn_params.invoke_shell()
            time.sleep(1.0)
            print(f"Logged into {get_output(conn).strip()} successfully")

            commands = [
                "terminal length 0",
                "show version | include Software",
                vrf_cmd,
            ]
            for command in commands:
                send_cmd(conn, command)
                print(get_output(conn))
        
            conn.close()

if __name__ == "__main__":
    main()
