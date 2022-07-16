import matplotlib, os, multiprocessing, time

path = './dist/v2_data'
def sorted_ls(path):
    mtime=lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

full_list = sorted_ls(path)
CW_PT_file_list = []
PT_CW_file_list = []
CW_PT_DATA = {}
PT_CW_DATA = {}

[CW_PT_file_list.append(elem) for elem in full_list if elem[:5] == 'CW_PT']
[PT_CW_file_list.append(elem) for elem in full_list if elem[:5] == 'PT_CW']

def dict_maker(name):
    for i, file in enumerate(name):
        id = i + 1
        info = file.split('_')
        data = open(path + '/' + file).readlines()
        data = [line.rstrip('\n') for line in data]
        for ii in data:
            try:
                dq = ii.split(' ')
                if dq[-1] == 'seconds':
                    if file[:5] == 'CW_PT':
                        # globals()["CW_PT_DATA_{}".format(id)] = {"id" : id, "from" : info[0], "to" : info[1], "year" : info[2], "month" : info[3], "day" : info[4], "hour" : info[5], "min" : info[6], "duration" : float(dq[-2])}
                        globals()["CW_PT_DATA_{}".format(id)] = {"id" : id, "from" : info[0], "to" : info[1], "year" : info[2], "month" : info[3], "day" : info[4], "hour" : info[5], "min" : info[6], "duration" : float(dq[-2])}
                        continue
                    else:
                        globals()["PT_CW_DATA_{}".format(id)] = {"id" : id, "from" : info[0], "to" : info[1], "year" : info[2], "month" : info[3], "day" : info[4], "hour" : info[5], "min" : info[6], "duration" : float(dq[-2])}
                        continue
                continue
            except:
                continue

dict_maker(CW_PT_file_list)
dict_maker(PT_CW_file_list)

print('dd')