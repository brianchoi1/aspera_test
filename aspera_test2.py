import time, paramiko, datetime

ssh = paramiko.SSHClient()           
default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
hpc_path_default = '/nas/users/HA'              
ip1 = 'cwhpc.lge.com'
ip2 = 'hpc.lge.com'
id = 'jaeyoung.choi'                                   
pw = '1111'

def txt_writing(msg, contents):
    f = open(msg, 'w', encoding='utf-8')
    for ii in contents:
        f.write(ii + '\n')
    f.close()

def aspera_cw_pt():
    # now = time.time()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    login_validation = ssh.connect(ip1, 22, id, pw)  
    dd = default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas' + ' gn46:' + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas'
    stdin, stdout, stderr = ssh.exec_command(dd)      # scratch 폴더 적용
    ddd = stdout.readlines()
    tt = datetime.datetime.now()
    ttt = str(tt.year) + '_' + str(tt.month) + '_' + str(tt.day) + '_' + str(tt.hour) + '_' + str(tt.minute) 
    txt_writing('CW_PT_' + ttt, ddd)
    exit_status = stdout.channel.recv_exit_status()
    time.sleep(1)
    ssh.close()

def aspera_pt_cw():
    # now = time.time()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    login_validation = ssh.connect(ip2, 22, id, pw)  
    dd = default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas' + ' gn21:' + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas'
    stdin, stdout, stderr = ssh.exec_command(dd)      # scratch 폴더 적용
    ddd = stdout.readlines()
    tt = datetime.datetime.now()
    ttt = str(tt.year) + '_' + str(tt.month) + '_' + str(tt.day) + '_' + str(tt.hour) + '_' + str(tt.minute) 
    txt_writing('PT_CW_' + ttt, ddd)
    exit_status = stdout.channel.recv_exit_status()
    time.sleep(1)
    ssh.close()

i = 1
while i > 0:
    aspera_cw_pt()
    time.sleep(60*15)
    aspera_pt_cw()
    time.sleep(60*15)