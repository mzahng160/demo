import psutil,time,os
import re

def getAllProcessID():
    with open('pid_file_id.txt', mode='w', encoding='UTF-8') as f:
        for id in psutil.pids():
            #process = psutil.Process(id)
            f.write(str(id)+'\n');

def getAllProcessName():
    with open('pid_file_name.txt', mode='w', encoding='UTF-8') as f:
        for id in psutil.pids():
            process = psutil.Process(id)
            f.write(process.name()+'\n');


def getAllProcessIDName():
    with open('pid_file_and_name.txt', mode='w', encoding='UTF-8') as f:
        for id in psutil.pids():
            process = psutil.Process(id)
            f.write(str(id)+'\n');
            f.write(process.name() + '\n');

def walkDir(dir_path):
    file_lists = []
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            path = str(os.path.join(root, f))
            file_lists.append(path)
    return file_lists

def rundir():
    all_title = []
    file_lists = walkDir('/proc/')
    with open('pid_file_process.txt', mode='w', encoding='UTF-8') as f:
        for file in file_lists:
            title = re.findall(r'\/proc\/\d+', file)
            title = str(title)[8:-2]
            if len(title) > 0:
                if title not in all_title:
                    all_title.append(title)
                    all_title.append('|')
                    #print(title)
                    f.write(title + '\n');
        #print((all_title))

def get_cpu_percent():
    content = "27 (migration/4) S 2 0 0 0 -1 69247040 0 0 0 0 0 4707 0 0 -100 0 1 0 11 0 0 18446744073709551615 0 0 0 0 0 0 0 2147483647 0 18446744071579610085 0 0 17 4 99 1 0 0 0 0 0 0 0 0 0 0 0"
    list = content.split(' ')
    for i in range(len(list)):
        print("{}-{}".format(i, list[i]))

def py_get_cpu_percent():
    for id in psutil.pids():
        process = psutil.Process(id)
        print("id:{} name: {} cpu:{}% ".format(id, process.name() ,process.cpu_percent(3)))

def get_totoal_cpu_usg():
    with open('/proc/stat', mode='r', encoding='UTF-8') as readfile:
        content = readfile.read()
        cpustr = content.split('\n')[0]
        cpudatalist = cpustr.split(' ')
        cputotal = 0
        for data in cpudatalist[2:]:
            cputotal = cputotal+int(data)

        cpuidle = int(cpudatalist[5])
    return cputotal, cpuidle


def travelstat():
    file_lists = walkDir('/proc/')
    index = 0
    for file in file_lists:

        title = re.findall(r'\/proc\/\d+\/stat$', file)
        if title:

            cputotal1 = get_totoal_cpu_usg()
            usecpu1 = 0
            with open(str(title[0]), mode='r', encoding='UTF-8') as readfile1:
                content1 = readfile1.read()
                for data1 in content1.split(' ')[12:16]:
                    usecpu1 = usecpu1 + int(data1)

            time.sleep(8)


            cputotal2 = get_totoal_cpu_usg()
            usecpu2 = 0
            with open(str(title[0]), mode='r', encoding='UTF-8') as readfile2:
                content2 = readfile2.read()
                for data in content2.split(' ')[12:16]:
                    usecpu2 = usecpu2 + int(data)

            print("id:{} name:{}  {}/{}={}".format(content2.split(' ')[0],content2.split(' ')[1],(usecpu2-usecpu1),(cputotal2-cputotal1),(usecpu2-usecpu1)/(cputotal2-cputotal1)))

def get_all_cpu_useage():
    cputoal1, cpuidle1 = get_totoal_cpu_usg()
    time.sleep(5)
    cputoal2, cpuidle2 = get_totoal_cpu_usg()
    total = cputoal2 - cputoal1
    idle = cpuidle2 - cpuidle1
    print("{} ".format(100*(total-idle)/total))

def travelcmdline():
    file_lists = walkDir('/proc/')
    index = 0
    with open('cmdline_ret.txt', mode='w', encoding='UTF-8') as wfile:
        for file in file_lists:
            title = re.findall(r'\/proc\/\d+\/cmdline$', file)
            if title:
                with open(str(title[0]), mode='r', encoding='UTF-8') as readfile:
                    wfile.write(readfile.read()+'\n')

def cpu_cal():
    i = 0
    while(True):
        i = i+1
#getAllProcessID()
#getAllProcessName()
#getAllProcessIDName()
#rundir()
#travelstat()
#py_get_cpu_percent()

#get_all_cpu_useage()

travelcmdline()

#cpu_cal()
