import datetime, subprocess, time

# hpc_path_default = '/nas/users/HA'              
ip1 = 'cwhpc.lge.com'
ip2 = 'hpc.lge.com'
id = 'jaeyoung.choi'                                   
pw = '1111'                                         

def uploading_func():

    t = open('upload_cmd', 'w', encoding='utf-8')
    t.write('put mesh_poly_bc_1.cas')
    t.close()
    cmd = "psftp.exe"
    subprocess.run([cmd, ip2, '-l', id, '-pw', pw, '-b', 'upload_cmd'],  shell=True) 

def txt_writing(msg, contents):
    f = open(msg, 'w', encoding='utf-8')
    f.write(contents)
    f.close()

i = 1
while i > 0:
    time_1 = time.time()
    uploading_func()
    time_2 = time.time()
    time_interval = time_2 - time_1
    ntime_interval = format(time_interval, ".2f")
    tt = datetime.datetime.now()
    ttt = str(tt.year) + '_' + str(tt.month) + '_' + str(tt.day) + '_' + str(tt.hour) + '_' + str(tt.minute) 
    txt_writing(ttt, ntime_interval)
    time.sleep(60*60)
