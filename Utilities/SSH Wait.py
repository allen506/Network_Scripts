import paramiko
import time


def wait_for_ssh_to_be_ready(host, port, timeout, retry_interval):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    retry_interval = float(retry_interval)
    timeout = int(timeout)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        time.sleep(retry_interval)
        try:
            client.connect(host, int(port), allow_agent=False,
                           look_for_keys=False)
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but not SSH service responded
            if e.message == 'Error reading SSH protocol banner':
                print(e)
                continue
            print('SSH transport is available!')
            break
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print('SSH transport is not ready...')
            continue


wait_for_ssh_to_be_ready('localhost', '8000', '20', '1')