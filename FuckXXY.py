# coding:utf-8
from urllib import request
from urllib import parse
import json
import time
import sys

# By TGSAN (h@lolimy.cn)

# 配置开始

account = "" # 账号
password = "" # 密码

school_id = "222" # 学校ID
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

no_wait = 0 # 是否不等待直接完成（将取消获取真实位置信息功能），0：等待，1：不等待

system = "4.4.4" # 模拟Android版本号
model = "FuckXixunyun" # 模拟机型
app_version = "4.1.4" # 模拟App版本号
uuid = "00:00:00:00:00:00" # 模拟UUID

# 配置结束

longitude = (str)(sign_gps[0]) # 经度
latitude = (str)(sign_gps[1]) # 纬度

def isset(v): 
    try : 
        type (eval(v)) 
    except : 
        return  0 
    else : 
        return  1

def get_remark(var):
    return {
        0: "上班",
        1: "外出",
        2: "假期",
        3: "请假",
        4: "轮岗",
        5: "回校",
        6: "外宿",
        7: "在家",
        8: "下班",
    }.get(var,"未知类型")

print("嘀~嘀~")
print("这是一个由TGSAN编写的Python命令行版“习讯云”客户端(=ﾟωﾟ)ﾉ")
print("因为官方的辣鸡客户端兼容性太差（Android 9 不兼容，而且反馈官方修了一个多星期都没修好）所以写了个这个呢~_(:3」∠)_")
print("配合crontab(Linux)或者Windows计划任务就能实现自动签到了，是不是很厉害呢！(｀・ω・´)")
print("让我来看看~(。´･ω･)?")

if account=="" or account=="" or school_id=="" or len(sign_gps)!=2:
    print("诶呀？好像你还没有配置好账号信息和签到设置呢！(>_<)")
    print("(｀・ω・´)萌新提示：在Linux上（比如路由器）可以在Shell使用 vi ./FuckXXY.py 来编辑配置区域哦~")
    exit(1)

print("嗯嗯。")
print("我来看一下~")

if no_wait==0:
    for i in range(1,100):
        try:
            # 获取位置信息
            req = request.Request("https://restapi.amap.com/v3/geocode/regeo?key=8325164e247e15eea68b59e89200988b&location=116.985693,36.708199&radius=2800")  # GET方法
            regeopage = request.urlopen(req, timeout=10).read()
            regeopage = regeopage.decode('utf-8')
            regeopage = json.loads(regeopage)
            # print(regeopage["regeocode"]["formatted_address"])
            # exit()
            break
        except Exception as e:
            print("出现异常-->"+str(e))

    print("你将会用账号",account,"在",regeopage["regeocode"]["formatted_address"],"（经度：",longitude,"，纬度"+latitude+"）以",remark_name,"进行签到。(｀・ω・´)")
    print("请确认一下哦~")
    for i in range(6):
        sys.stdout.write('\r')
        sys.stdout.write("你可以在 %s 秒之内按 Ctrl+C 组合键退出~ " %(int(5-i)))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\n')
else:
    print("你将会用账号",account,"在经度：",longitude,"，纬度"+latitude+"以",remark_name,"进行签到。(｀・ω・´)")
print("我们来登录吧！")

headers = {
    # 'User-Agent':'FuckXixunyun/h@lolimy.cn'
}

for i in range(1,100):
    try:
        # 登录
        loginurl = "https://api.xixunyun.com/login/api?from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0"
        logindata = {"registration_id":"1104a8979285e976298","platform":2,"system":system,"model":model,"app_version":app_version,"account":account,"app_id":"cn.vanber.xixunyun.saas","uuid":uuid,"password":password,"key":"","request_source":"3","school_id":school_id}
        logindata = parse.urlencode(logindata).encode('utf-8')
        req = request.Request(loginurl, headers=headers, data=logindata)  #POST方法
        accountpage = request.urlopen(req, timeout=10).read()
        accountpage = accountpage.decode('utf-8')
        accountpage = json.loads(accountpage)
        # print(accountpage)
        break
    except Exception as e:
        print("出现异常-->"+str(e))

print("登录状态码：",accountpage["code"])
print("登录状态：",accountpage["message"])
print("服务器返回响应时间：",accountpage["run_execute_time"])
if accountpage["code"]==20000: # 成功
    print("内部账户编号：",accountpage["data"]["user_id"])
    print("你好",accountpage["data"]["user_name"],"！(/・ω・)/")
    print("目前你的积分为",accountpage["data"]["point"],"分，全校排名第",accountpage["data"]["point_rank"],"位")
    print("姓名：",accountpage["data"]["user_name"])
    print("学号：",accountpage["data"]["user_number"])
    print("班级：",accountpage["data"]["class_name"])
    print("入学年份：",accountpage["data"]["entrance_year"])
    print("绑定手机号：",accountpage["data"]["bind_phone"])
    print("登录令牌：",accountpage["data"]["token"])
    if no_wait==0:
        print("请确认账户没错哦~")
        for i in range(6):
            sys.stdout.write('\r')
            sys.stdout.write("你可以在 %s 秒之内按 Ctrl+C 组合键取消哦~ " %(int(5-i)))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\n')
    print("正在进入签到页面~")

    for i in range(1,100):
        try:
            # 获取签到信息(原始信息：month_date=2018-12)
            req = request.Request("https://api.xixunyun.com/signin40/homepage?month_date=&token="+accountpage["data"]["token"]+"&from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0")  # GET方法
            signhomepage = request.urlopen(req, timeout=10).read()
            signhomepage = signhomepage.decode('utf-8')
            signhomepage = json.loads(signhomepage)
            break
        except Exception as e:
            print("出现异常-->"+str(e))

    print("登录状态码：",signhomepage["code"])
    print("登录状态：",signhomepage["message"])
    print("服务器返回响应时间：",signhomepage["run_execute_time"])
    if signhomepage["code"]==20000: # 成功
        # print(signhomepage["data"])
        print("连续签到次数：",signhomepage["data"]["continuous_sign_in"])
        print("服务器返回签到类型数据：",signhomepage["data"]["mark_list"])
        print("开始匹配签到类型数据")
        for i in signhomepage["data"]["mark_list"]:
            # print(i)
            # if i["value"] == remark_name:
            if i["value"] == remark_name:
                print("找到对应数据了！类型名称",i["value"],"对应Key为",i["key"])
                remark = i["key"]
                break
        if(isset('remark')==0):
            print("没有找到类型数据，请确认是否配置正确（可以参考输出日志中的“服务器返回签到类型数据”部分）")
            exit()
        signactdata = {"change_sign_resource":"0","longitude":longitude,"latitude":latitude,"comment":"","remark":remark,"address":"","address_name":""}
        # 下面for循环里其实还需要重新组合
        print("开始组合数据包：",signactdata)
        if no_wait==0:
            print("数据包没错哦~（其实只是让开发者确认啦）")
            for i in range(6):
                sys.stdout.write('\r')
                sys.stdout.write("你可以在 %s 秒之内按 Ctrl+C 组合键取消哦~ " %(int(5-i)))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write('\n')
        print("Biu~那么我们就开始吧！")
        for i in range(1,100):
            try:
                # 登录
                signacturl = "https://api.xixunyun.com/signin?token="+accountpage["data"]["token"]+"&from=app&version="+app_version+"&platform=android&entrance_year=0&graduate_year=0"
                signactdata = {"change_sign_resource":"0","longitude":longitude,"latitude":latitude,"comment":"","remark":remark,"address":"","address_name":""}
                signactdata = parse.urlencode(signactdata).encode('utf-8')
                req = request.Request(signacturl, headers=headers, data=signactdata)  #POST方法
                signactpage = request.urlopen(req, timeout=10).read()
                signactpage = signactpage.decode('utf-8')
                signactpage = json.loads(signactpage)
                # print(signactpage)
                """ 
                数据样例（20181215）
                {
                    "code": 20000,
                    "message": "成功",
                    "run_execute_time": "0.0689s",
                    "data": {
                        "point": 2,
                        "continuous": 4,
                        "message_string": "太棒了！+2积分，您已签到4天。"
                }
                """
                break
            except Exception as e:
                print("出现异常-->"+str(e))
        # print("原始信息：",signactpage)
        print("登录状态码：",signactpage["code"])
        print("登录状态：",signactpage["message"])
        print("服务器返回响应时间：",signactpage["run_execute_time"])
        if signactpage["code"]==20000: # 成功
            print("\r\n\r\n",signactpage["data"]["message_string"])
        else:
            print("\r\n\r\n好像签到失败了QAQ")
            print("原因：",signactpage["message"])
            exit()
    else:
        print("\r\n\r\n好像正在进入签到页面失败了QAQ")
        exit()
else:
    print("\r\n\r\n好像登录失败了QAQ")
    exit()

# By TGSAN (h@lolimy.cn)
