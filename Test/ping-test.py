import os

exit_code = os.system('ping www.baidu.com')
if exit_code:
    os.system('python fun-auth.py')
    
