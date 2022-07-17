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
    from_list = []
    to_list = []
    year_list = []
    month_list = []
    day_list = []
    hour_list = []
    min_list = []

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

                    from_list.append(info[0])
                    to_list.append(info[1])
                    year_list.append(info[2])
                    month_list.append(info[3])
                    day_list.append(info[4])
                    hour_list.append(info[5])
                    min_list.append(info[6])
                    continue
                continue
            except:
                continue

    DATA = {"id" : id_list, "from_to" : from_to_list, "time" : time_list, "duration" : duration_list, "from" : from_list, "to" : to_list, "year" : year_list, "month" : month_list, "day" : day_list, "hour" : hour_list, "min" : min_list}
    return DATA

CW_PT_DATA = dict_maker(CW_PT_file_list)
PT_CW_DATA = dict_maker(PT_CW_file_list)
CW_PT_DF = pd.DataFrame(CW_PT_DATA)  #dict to dataframe
PT_CW_DF = pd.DataFrame(PT_CW_DATA)
# ddq = CW_PT_DF[['time', 'duration']]
# dq = ddq.loc[0:50,:]

cw_pt_month_groups = CW_PT_DF.groupby(['month', 'day'])
pt_pt_month_groups = PT_CW_DF.groupby(['month', 'day'])
for cw_pt in cw_pt_month_groups:
    plt.figure(figsize=(25,25))
    plt.rc('xtick', labelsize=5)
    plt.scatter(cw_pt[1]["time"], cw_pt[1]["duration"])
    plt.xticks(rotation=45)
    print(cw_pt[1]["time"])
plt.show()

# for pt_cw in pt_pt_month_groups:
#     plt.figure(figsize=(25,25))
#     plt.rc('xtick', labelsize=5)
#     plt.scatter(pt_cw[1]["time"], pt_cw[1]["duration"])
#     plt.xticks(rotation=45)
#     print(pt_cw[1]["time"])
# plt.show()

# result_month = dict(list(month_groups))
# month_list = list(result_month.keys())
# day_groups = CW_PT_DF.groupby('day')
# result_day = dict(list(day_groups))
# day_list = list(result_day.keys())

# ree = result_month["7", "10"]
# print(ree)
# for iiii in month_list:
#     for iii in day_list:
#         globals()[iiii + "_list_{}".format(iii)]
        # group_table_list.append("table_list_{}".format(id))
# doi = result["14"]
# print(doi)

# ap = CW_PT_DF[CW_PT_DF["day"] == "7"]
# print(ap)

##### regression #####
# x_minmax = np.array([min(x), max(x)]) # x축 최소값, 최대값

# fit_y = x_minmax * fit_line[0] + fit_line[1] # x축 최소, 최대값을 회귀식에 대입한 값

# plt.scatter(x, y, color = 'r', s = 20)
# plt.plot(x_minmax, fit_y, color = 'orange') # 회귀선 그래프 그리기
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

##### regression #####

# plt.figure(figsize=(20,20))
# plt.scatter(dq["time"], dq["duration"])
# plt.xticks(rotation=45)
# plt.rc('xtick', labelsize=1)
# plt.rc('axes', labelsize=2) 
# plt.grid(True)
# plt.show()


print('dd')