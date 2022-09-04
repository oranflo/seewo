# 希沃

## 介绍
没什么说的，dddd \
后面可能会把希沃管家的冰点还原密码也搞定

## 安装教程

把希沃管家目录下的uninstall_verify.exe替换为本仓库中的，点击uninstall.exe即可

## 后记

搞这玩意主要是帮群友在学校电子白板上装steam玩，本来也没啥技术含量，主要是怕有些人没有编译环境，所以开个仓库把编译好的程序放在这上面 \

### (2022/9/4)
#### 原先设想密码由6位纯数字组成，直接爆破即可，但是实际爆破中遇到3个困难：
1、验证程序无规律闪退 \
2、验证程序本身无标题 \
3、FindWindow函数在不指定窗口名，仅指定窗口类时有时无法正确返回窗口句柄，也主要是因为这个原因而使爆破程序经常以出人意料的状态运行 \
#### 同时在爆破时解决了一些基本问题：
1、uninstall_verify.exe直接启动无反应，因为需要启动参数-verify_pwd，加入启动参数即可正常使用 \
2、uninstall_verify.exe验证密码正确后会返回0供Uninstall.exe使用 \
3、uninstall_verify.exe在输错5次密码后会锁定按钮10分钟，此时找到按钮句柄，直接发送鼠标事件即可继续正常点击 \
4、uninstall_verify.exe对于发送的虚拟鼠标与键盘事件未作任何屏蔽，如果发送事件无反应，请提升至管理员再发送事件 \
#### 之后的思路：
1、直接对uninstall_verify.exe进行逆向，找到管理员密码 \
2、对爆破程序进行改进，改进后的爆破程序使用其它方式代替FindWindow函数，防止出现新bug \
有任何思路或者疑问，发我邮箱`oranflo@foxmail.com`或者发我b站私信或者发issue，因为众所周知的原因我不太用github而是用gitee，但是gitee我没法开源代码，因此代码只能放在github上 \
#### 已经做的测试都在./test_pwd/下
其中: \
.c和.py实现功能相同 c语言实现明显更快 但是python语言相对更易读一些，参考思路可以看py源代码 \
kill_prompt.c kill_prompt.py 是结束掉输错密码后的“密码错误”对话框 \
test_pwd.c 通过 `test_pwd.exe pwd1 pwd2 ...` 的形式启动 会验证所有控制台输入的密码 \
start_verify_v1.0.py 会开启多个test_pwd.exe子进程并管理密码池 \
test_pwd_single_proc.c 是尝试以纯c语言写一个单线程的破解程序，但是会卡在关闭“密码错误”对话框这一步

