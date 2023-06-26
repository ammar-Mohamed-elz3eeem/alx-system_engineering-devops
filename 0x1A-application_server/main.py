#!/usr/bin/python3
"""
Verifies that Nginx is proxying requests from port 80 to port 5002
"""
import re
import sys
import json

from fabric import Connection
from invoke import run
from io import StringIO
from paramiko import RSAKey
from time import sleep

host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]
route = sys.argv[4]

rsa_key = RSAKey.from_private_key(open(rsa_key_file), 'betty')
output = StringIO()

def curl_server(ip, route):
    """ Sends request to student's server and returns response. """
    output = run('curl -s '+str(ip)+str(route), hide=True, warn=True)
    return output.stdout

def parse_curl_output(output):
    """ Search curled HTML for sought after output. """
    try:
        o_json = json.loads(output)
        if len(o_json.keys()) != 1 or list(o_json.keys())[0] != 'status':
            return "Wrong JSON key: {}".format(output)
        print(type(o_json))
        if o_json.get('status', "").lower() != 'ok':
            return "Wrong status value: {}".format(output)
        return "OK"
    except:
        print("Bad JSON: {}".format(output))

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("netstat -na | grep '5002.* LISTEN'", shell="/bin/bash", out_stream=output, warn=True)
    if output.getvalue():
        curl_output = curl_server(host, route)
        print(curl_output)
        print(type(curl_output))
        print(parse_curl_output(curl_output), end="")
        exit(0)
    else:
        c.run("cd AirBnB_clone_v3 && bash -lc \"tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 -p /tmp/gunginx2.pid api.v1.app:app'\"", shell="/bin/bash", warn=True)
        for i in range(5):
            curl_output = curl_server(host, route)
            parsed_output = parse_curl_output(curl_output)
            if parsed_output == "OK":
                print(parsed_output, end="")
                c.run("sudo kill -9 `cat /tmp/gunginx2.pid` > /dev/null 2>&1", shell="/bin/bash", warn=True)
                exit(0)
        print(parsed_output, end="")
        c.run("sudo kill -9 `cat /tmp/gunginx2.pid` > /dev/null 2>&1", shell="/bin/bash", warn=True)
        exit(0)