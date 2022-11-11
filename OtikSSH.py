import paramiko

hostname = sys.argv[1]
command = sys.argv[2]

username = "root"
port = 2222

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(hostname, port=port, username=username, key_filename=)
    stdin, stdout, stderr = client.exec_command(command)
    stdin.write("Neco napsano")
    print(stdout.read())
except Exception as e:
    print("Error happened: %s" % (e,))

ftp_client=ssh_client.open_sftp()
ftp_client.get(‘remotefilepath’,’localfilepath’)
ftp_client.close()

ftp_client=ssh.open_sftp()
ftp_client.put(‘localfilepath’,remotefilepath’)
ftp_client.close()