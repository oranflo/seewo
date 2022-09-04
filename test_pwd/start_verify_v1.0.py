# coding: utf-8
import time
from subprocess import Popen, PIPE
import random

### 生成6个长度的密码
def get_six_len_pwd(x: int):
    x = str(x)
    y = len(x)
    y = 6 - y
    x = "0" * y + x
    return x 
    
# ### 启动关对话框的进程
# Popen("kill_prompt.exe")

### 指派进程破解
processes_num = 5 # 进程数
pwd_for_every_proc = 1000 # 每个进程分配的密码数量
pool = dict() # 进程池
# 进程id: 进程对象, 进程正在破解的密码
pwd_ = [i for i in range(0, 1000000)] # 创建密码列表
# pwd = []
# for i in range(0, 1000000):
#     pwd.append(random.choice(pwd_))
pwd = pwd_
del(pwd_)

will_del = [] # 字典不能在遍历时改变

while len(pwd) != 0:
    while len(pool.keys()) < processes_num: # 进程数不够 创建新进程
        print(pool.keys())
        proc_id = time.time() # 生成主键
        proc_pwd = [get_six_len_pwd(i) for i in pwd[-pwd_for_every_proc:]] # 生成需要的密码
        pwd = pwd[:-pwd_for_every_proc] # 剩余密码列表

        Popen(["uninstall_verify.exe", "-verify_pwd"]) # 启动新的窗口
        time.sleep(2) # 等待3秒 防止没有找到窗口
        proc = Popen(["test_pwd.exe"] + proc_pwd, stdout=PIPE, shell=True) # 将密码传入
        time.sleep(2) # 初始化时间与密码长度有关
        pool[proc_id] = (proc, tuple(proc_pwd)) # 放入进程池
    # 管理进程状态
    # print(pool.keys())
    for key in pool.keys():
        if time.time() - key > 60: # 超时
            pwd += [int(i) for i in pool[key][1]] # 将密码返回密码池
            will_del.append(key)
        elif pool[key][0].poll():
            status = pool[key][0].returncode
            if status == -1: # 执行失败 重试
                pwd += [int(i) for i in pool[key][1]] # 将密码返回密码池
                will_del.append(key)
            elif status == 1: # 未找到密码
                will_del.append(key)
            elif status == 2: # 找到密码
                print("find!")
                print(pool[key][0].stdout.read())
                for i in pool.keys():
                    pool[i][0].kill()
                exit(0)
    # 正式删除主键
    for key in will_del:
        try:
            del pool[key]
        except KeyError:
            pass
