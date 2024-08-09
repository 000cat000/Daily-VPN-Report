import requests

# FortiAnalyzer的基本信息
base_url = "https://your-fortianalyzer-ip/api/v2/"
username = "your-username"
password = "your-password"

# 登錄FortiAnalyzer並獲取Token
def login():
    login_url = f"{base_url}monitor/system/logincheck"
    payload = {'username': username, 'secretkey': password}
    response = requests.post(login_url, data=payload, verify=False)
    if response.status_code == 200:
        print("Login successful")
        return response.cookies
    else:
        print("Login failed")
        return None

# 從FortiAnalyzer提取日誌數據
def get_logs(session_cookies):
    log_url = f"{base_url}log/report/adom/root/logsearch"
    payload = {
        'type': 'traffic',
        'filter': '',
        'sort_order': 'desc',
        'limit': 10,
        'offset': 0
    }
    response = requests.post(log_url, cookies=session_cookies, json=payload, verify=False)
    if response.status_code == 200:
        logs = response.json()
        print(logs)
    else:
        print("Failed to retrieve logs")

# 執行流程
session_cookies = login()
if session_cookies:
    get_logs(session_cookies)
