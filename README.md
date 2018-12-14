# FuckXixunyun

基于Python的习讯云命令行客户端（签到）

# Usage 使用

1.下载 `FuckXXY.py`

2.用你喜爱的编辑器（如VIM、Sublime、Code）打开

3.编辑配置区块：
```
# 配置开始

account = "" # 账号
password = "" # 密码

school_id = "" # 学校ID
# 关于学校ID
# 可以前往 https://api.xixunyun.com/login/schoolmap 查询，比如山东商务职业学院ID为222（截止20181215）

remark_name = "在家" # 签到类型（现已只需填写汉字类型）
# 关于签到类型
# 请注意此类型可能会变更
# 0：上班 1：外出 2：假期 3：请假 4：轮岗 5：回校 6：外宿 7：在家 8：下班

sign_gps = [] # 签到坐标（注意小数点取后6位）
# 关于如何获取坐标
# 例如[0.123456,0.123456]，先经度后纬度，可以去 https://lbs.amap.com/console/show/picker 高德取坐标，直接把结果复制到[]里即可
# 每家坐标拾取器标准不同，本脚本采用XY轴坐标格式。例如北京[116.000000,40.000000]

# 配置结束
```

4.保存

4-1.安装Python3.x（如果你还没安装Python3.x的话）

如果你是萌新，想要在Linux系统（比如树莓派或者路由器）上使用可以用以下方法安装Python3 :)

Deban/Ubuntu:

```
sudo apt install python3
```

Centos/RHEL/Fedora:

```
sudo yum install python3
```

Fedora:

```
sudo dnf install python3
```

Arch:

```
sudo pacman -S python3
```

OpenWRT:

```
sudo opkg install python3
```

4-2.配置Python环境变量（如果安装时忘记设置的话）

5.打开命令行（Bash、PowerShell、CMD等）

6.运行`python {你的目录}\FuckXXY.py`（Windows）或`python3 {你的目录}/FuckXXY.py`（\*nux）

7.Enjoy it~
