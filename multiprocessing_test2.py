import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
import multiprocessing

def doWork(file_name):
    print('Start ' + file_name + ' : ')

    file = open(dir_path + file_name, 'r', encoding="UTF-8")
    file = file.read().strip()
    file_soup = BeautifulSoup(file, 'html5lib')

    columns = {'id': [], 'title': [], 'text': []}
    tmp_df = pd.DataFrame(data=columns)

    for doc in file_soup.find_all('doc'):
        tmp_df = tmp_df.append({'id': doc['id'], 'title': doc['title'], 'text': doc.text}, ignore_index=True)

    # 각 작업에 해당하는 결과물
    # 대량의 데이터를 다룰 시 중간 데이터를 저장해두는 것이 좋음
    tmp_df.to_excel(dir_path + '{0}'.format(file_name + '.xlsx'), index=False)

    print('End ' + file_name + ' : ')


# 작업 리스트를 반환
def getWorkList():
    work_list = []

    for i in tqdm(range(0, 17)):
        work_list.append('file_' + str(i))

    return work_list

dir_path = 'C:\\Users\\jihun.park\\Desktop\\data\\'

if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=3) # 3개의 processes 사용
    pool.map(doWork, getWorkList())
    pool.close()
    pool.join()