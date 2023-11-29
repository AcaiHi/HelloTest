import subprocess
import schedule
import time

def run_php_script():
    # 替換 'your_script.php' 為您的 PHP 文件路徑
    subprocess.run(['php', 'C:\\Users\\軟體工程實驗室\\Desktop\\test.php'])

# 定時設置，這裡設置為每天的 10:00 執行
schedule.every().day.at("15:50").do(run_php_script)

# 保持腳本運行
while True:
    print('Waiting...')
    schedule.run_pending()
    time.sleep(1)