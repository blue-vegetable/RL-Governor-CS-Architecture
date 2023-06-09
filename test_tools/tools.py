import argparse
import sys
sys.path.append('/home/blues/Desktop/networkTrans/test_tools/modules')
from modules.commandExec import execute
from modules.fpsGet import FPSGet
from modules.cpuControl import CPUControl
from modules.config import *


parser = argparse.ArgumentParser()
parser.add_argument("option")
args = parser.parse_args()

option = args.option

if option=='watch':
    print(option)
    print(execute('cat /sys/devices/system/cpu/cpufreq/policy0/scaling_governor'))
    print(execute('cat /sys/devices/system/cpu/cpufreq/policy4/scaling_governor'))

if option=='watch_cpu':
    print(option)
    from modules.cpuControl import CPUControl
    a = CPUControl(2)
    print(a.get_cpu_util_time())

if option=='fps':
    print(option)
    fps = FPSGet(view=view)
    frame = fps.get_fps()

if option=='start_service':
    print(option)
    execute('am start-foreground-service -n "com.example.networktrans/com.example.networktrans.MyService"')

if option=='start_app': #启动抖音
    print(option)
    execute('monkey -p com.ss.android.ugc.aweme -c android.intent.category.LAUNCHER 1')

if option =='kill_app':
    print(option)
    execute('am kill-all')  # 清除所有后台应用
    execute('am force-stop com.example.networktrans')  #我知道的app
    execute('am force-stop com.example.anomalyapp') 

if option=='init':
    print(option)
    execute('echo "schedutil" >  /sys/devices/system/cpu/cpufreq/policy0/scaling_governor')  # 恢复为自带调频
    execute('echo "schedutil" >  /sys/devices/system/cpu/cpufreq/policy4/scaling_governor')
    execute('am force-stop com.example.networktrans')  #我知道的app
    execute('am force-stop com.example.anomalyapp') 
    execute('am kill-all')  # 清除所有后台应用
    execute('am stopservice -n "com.example.anomalyapp/com.example.anomalyapp.ComputeService"')
    execute('am stopservice -n "com.example.anomalyapp/com.example.anomalyapp.DownloadService"')
    execute('am stopservice -n "com.example.anomalyapp/com.example.anomalyapp.LoadImageService"')
    execute('am stopservice -n "com.example.networktrans/com.example.networktrans.MyService"')
    execute('am stopservice -n "com.example.networktrans/com.example.networktrans.MyService"') # 不知为何这个要清理两次

    execute('dumpsys batterystats --enable full-wake-history')  # 清除之前的电源信息
    execute('dumpsys batterystats --reset')

if option=='vis':
    import modules.visual