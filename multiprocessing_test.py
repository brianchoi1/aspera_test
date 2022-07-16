import multiprocessing
import time
import random

# 시작시간
ncpu = multiprocessing.cpu_count()
start_time = time.time()

def count(name):
    print('Start ' + name, " : ")
    time.sleep(random.randrange(1,10))
    print('End ' + name, " : ")

work_list = []
for i in range(1, 11):
    work_list.append('item' + str(i))

if __name__ == '__main__':
    # 멀티 쓰레딩 Pool 사용
    pool = multiprocessing.Pool(processes=4)  # 현재 시스템에서 사용 할 프로세스 개수
    pool.map(count, work_list)
    pool.close()
    pool.join()

    print("--- %s seconds ---" % (round(time.time() - start_time, 4)))