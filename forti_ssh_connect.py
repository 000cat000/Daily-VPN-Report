import paramiko  #使用Paramiko進行SSH連接並執行命令

# SSH連接信息
hostname = "your-fortianalyzer-ip"
port = 22
username = "your-username"
password = "your-password"

def ssh_connect():
    try:
        # 建立SSH連接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        # 執行命令來獲取數據
        stdin, stdout, stderr = ssh.exec_command('show system status')
        output = stdout.read().decode()
        print(output)

        # 關閉連接
        ssh.close()

    except Exception as e:
        print(f"Failed to connect: {e}")

# 執行流程
ssh_connect()
