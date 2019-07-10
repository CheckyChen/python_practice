# author:checky

# Python内置的os模块可以直接调用操作系统提供的接口函数：

import os

# 1.操作系统的类型
print(os.name)
# nt
# posix，说明系统是Linux、Unix或Mac OS X，
# nt，就是Windows系统

# 2.环境变量
print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\CHECKY\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'CHECKY', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'CONFIGSETROOT': 'C:\\WINDOWS\\ConfigSetRoot', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'GOLAND': 'D:\\install\\GoLand 2019.1.1\\bin;', 'GOPATH': 'C:\\Users\\CHECKY\\go', 'GOROOT': 'D:\\install\\Go\\', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\CHECKY', 'LOCALAPPDATA': 'C:\\Users\\CHECKY\\AppData\\Local', 'LOGONSERVER': '\\\\CHECKY', 'MOZ_PLUGIN_PATH': 'D:\\install\\PDFReader\\Foxit Reader\\plugins\\', 'MYSQLCONNECTOR_ASSEMBLIESPATH': 'C:\\Program Files (x86)\\MySQL\\Connector NET 8.0\\Assemblies\\v4.5.2', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\CHECKY\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'E:\\python\\working\\Django\\restframework\\homework\\Library\\bin;E:\\python\\working\\Django\\restframework\\homework\\Scripts;C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\Docker\\Docker\\Resources\\bin;D:\\install\\Anaconda;D:\\install\\Anaconda\\Library\\mingw-w64\\bin;D:\\install\\Anaconda\\Library\\usr\\bin;D:\\install\\Anaconda\\Library\\bin;D:\\install\\Anaconda\\Scripts;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files\\nodejs\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\110\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\ManagementStudio\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\DTS\\Binn\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;D:\\install\\Anaconda3\\Scripts\\;C:\\WINDOWS\\system32\\config\\systemprofile\\.dnx\\bin;C:\\Program Files\\Microsoft DNX\\Dnvm\\;D:\\install\\Anaconda3;D:\\install\\Git\\cmd;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\install\\Redis\\;D:\\install\\Go\\bin;D:\\install\\python3.7\\Scripts\\;D:\\install\\python3.7\\;C:\\Users\\CHECKY\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\CHECKY\\AppData\\Roaming\\npm;D:\\install\\Microsoft VS Code\\bin;D:\\install\\pycharm_professional\\PyCharm 2018.3.1\\bin;;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\install\\geckodriver-v0.24.0-win64;C:\\Users\\CHECKY\\go\\bin;D:\\install\\GoLand 2019.1.1\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(homework) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\PowerShell\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\install\\pycharm_professional\\PyCharm 2018.3.1\\bin;', 'PYCHARM_DISPLAY_PORT': '53565', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'E:\\python\\working\\homework;D:\\install\\pycharm_professional\\PyCharm 2018.3.1\\helpers\\pycharm_matplotlib_backend;D:\\install\\pycharm_professional\\PyCharm 2018.3.1\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\CHECKY\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\CHECKY\\AppData\\Local\\Temp', 'USERDOMAIN': 'CHECKY', 'USERDOMAIN_ROAMINGPROFILE': 'CHECKY', 'USERNAME': 'CHECKY', 'USERPROFILE': 'C:\\Users\\CHECKY', 'VIRTUAL_ENV': 'E:\\python\\working\\Django\\restframework\\homework', 'VS120COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\Tools\\', 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\', 'VS150COMCOMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\Tools\\', 'WINDIR': 'C:\\WINDOWS', '_OLD_VIRTUAL_PATH': 'C:\\ProgramData\\DockerDesktop\\version-bin;C:\\Program Files\\Docker\\Docker\\Resources\\bin;D:\\install\\Anaconda;D:\\install\\Anaconda\\Library\\mingw-w64\\bin;D:\\install\\Anaconda\\Library\\usr\\bin;D:\\install\\Anaconda\\Library\\bin;D:\\install\\Anaconda\\Scripts;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files\\nodejs\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\110\\DTS\\Binn\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\ManagementStudio\\;C:\\Program Files (x86)\\Microsoft SQL Server\\110\\DTS\\Binn\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;D:\\install\\Anaconda3\\Scripts\\;C:\\WINDOWS\\system32\\config\\systemprofile\\.dnx\\bin;C:\\Program Files\\Microsoft DNX\\Dnvm\\;D:\\install\\Anaconda3;D:\\install\\Git\\cmd;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\install\\Redis\\;D:\\install\\Go\\bin;D:\\install\\python3.7\\Scripts\\;D:\\install\\python3.7\\;C:\\Users\\CHECKY\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\CHECKY\\AppData\\Roaming\\npm;D:\\install\\Microsoft VS Code\\bin;D:\\install\\pycharm_professional\\PyCharm 2018.3.1\\bin;;C:\\Program Files (x86)\\Google\\Chrome\\Application;D:\\install\\geckodriver-v0.24.0-win64;C:\\Users\\CHECKY\\go\\bin;D:\\install\\GoLand 2019.1.1\\bin;', '_OLD_VIRTUAL_PROMPT': '$P$G'})

# 获取环境变量的值
print(os.environ.get("APPDATA"))
# C:\Users\CHECKY\AppData\Roaming

# 3.操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 当前目录的绝对路径
print(os.path.abspath("."))
# E:\python\working\homework\10.IO编程

# 创建一个新目录
# os.mkdir(os.path.join(os.path.abspath("."), "newdir"))

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
# 而Windows下会返回这样的字符串：
print(os.path.join("dir1","dir2"))
# dir1\dir2

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split("'/Users/michael/testdir/file.txt"))
# ("'/Users/michael/testdir", 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext("'/Users/michael/testdir/file.txt"))
# ("'/Users/michael/testdir/file", '.txt')

# 4.重命名
# os.rename("test.txt","test_new.txt")

# 5.删除文件
# os.remove("test_new.txt")

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
li = [x for x in os.listdir(".") if os.path.isdir(x)]
print(li)

# 列出所有的.py文件
li1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(li1)
