import sys
import time
import paramiko
import os
import cmd
import datetime

now = datetime.datetime.now()
user = "admin"
password = "admin"
project = "pimco-wan"
user = input("Enter username:")
password = input("Enter Paswd:")
enable_password = input("Enter enable pswd:")
routerlist = input("Enter router inventory file: ")
port = 22
f0 = open(routerlist)
for devices in f0.readlines():
    devices = devices.split()
    deviceip = devices[0]
    hostname = devices[1]
    filename_prefix = '/Users/allen/PycharmProjects/Cisco Stuff/backups/'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(deviceip, port, user, password, look_for_keys=False)
    chan = ssh.invoke_shell()
    time.sleep(2)
    # chan.send('enable\n')
    # chan.send(enable_password +'\n')
    # time.sleep(1)
    chan.send('term len 0\n')
    time.sleep(1)
    chan.send('sh run\n')
    time.sleep(5)
    output = chan.recv(999999)
    filename = filename_prefix + project + "-" + hostname + "_%s_%.2i%.2i%i_%.2i%.2i%.2i.txt" % (deviceip, now.year, now.month, now.day, now.hour, now.minute, now.second)
    f1 = open(filename, 'a')
    f1.write(output.decode("utf-8"))
    f1.close()
    ssh.close()
    f0.close()

    print(deviceip)
f0.close()

