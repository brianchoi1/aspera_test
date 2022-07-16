import os, multiprocessing, time
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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
    from_to_list = []
    time_list = []
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
                    from_to_list.append(info[0] + '_' + info[1])
                    time_list.append(info[2] + '_' + info[3] + '_' + info[4] + '_' + info[5] + '_' + info[6])
                    duration_list.append(float(dq[-2]))
                    continue
                continue
            except:
                continue

    DATA = {"id" : id_list, "from_to" : from_to_list, "time" : time_list, "duration" : duration_list}
    return DATA

CW_PT_DATA = dict_maker(CW_PT_file_list)
PT_CW_DATA = dict_maker(PT_CW_file_list)
CW_PT_DF = pd.DataFrame(CW_PT_DATA)  #dict to dataframe
PT_CW_DF = pd.DataFrame(PT_CW_DATA)
ddq = CW_PT_DF[['time', 'duration']]


plt.scatter(ddq["time"], ddq["duration"])
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


print(ddq)
print('dd')