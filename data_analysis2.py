import matplotlib, os, multiprocessing, time
import pandas as pd

path = './dist/v2_data'
def sorted_ls(path):
    mtime=lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

full_list = sorted_ls(path)
CW_PT_file_list = []
PT_CW_file_list = []

[CW_PT_file_list.append(elem) for elem in full_list if elem[:5] == 'CW_PT']
[PT_CW_file_list.append(elem) for elem in full_list if elem[:5] == 'PT_CW']

def dict_maker(name):
    id_list = []
    from_list = []
    to_list = []
    year_list = []
    month_list = []
    day_list = []
    hour_list = []
    min_list = []
    duration_list = []

    for i, file in enumerate(name):
        id = i + 1
        info = file.split('_')
        data = open(path + '/' + file).readlines()
        data = [line.rstrip('\n') for line in data]
        for ii in data:
            try:
                dq = ii.split(' ')
                if dq[-1] == 'seconds':
                    id_list.append(id)
                    from_list.append(info[0])
                    to_list.append(info[1])
                    year_list.append(info[2])
                    month_list.append(info[3])
                    day_list.append(info[4])
                    hour_list.append(info[5])
                    min_list.append(info[6])
                    duration_list.append(float(dq[-2]))
                    continue
                continue
            except:
                continue

    if from_list[0] == 'CW':
        DATA = {"id" : id_list, "from" : from_list, "to" : to_list, "year" : year_list, "month" : month_list, "day" : day_list, "hour" : hour_list, "min" : min_list, "duration" : duration_list}
    else:
        DATA = {"id" : id_list, "from" : from_list, "to" : to_list, "year" : year_list, "month" : month_list, "day" : day_list, "hour" : hour_list, "min" : min_list, "duration" : duration_list}
    return DATA

CW_PT_DATA = dict_maker(CW_PT_file_list)
PT_CW_DATA = dict_maker(PT_CW_file_list)
CW_PT_DF = pd.DataFrame(CW_PT_DATA)
PT_CW_DF = pd.DataFrame(PT_CW_DATA)
ddq = CW_PT_DF[['month', 'day', 'hour', 'min']]
print(ddq)
print('dd')