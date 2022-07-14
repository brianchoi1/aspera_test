import time, paramiko

ssh = paramiko.SSHClient()           
default_cmd = '. /etc/profile;. ~/.bash_profile;. ~/.bashrc; aspera '                                              
hpc_path_default = '/nas/users/HA'              
ip1 = 'hpc.lge.com'
id = 'jaeyoung.choi'                                   
pw = '1111'

def txt_writing(msg, contents):
    f = open(msg, 'w', encoding='utf-8')
    for ii in contents:
        f.write(ii + '\n')
    f.close()

def aspera_():
    now = time.time()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    login_validation = ssh.connect(ip1, 22, id, pw)  
    dd = default_cmd + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas' + ' gn21:' + hpc_path_default + '/' + id + '/scratch/' + 'mesh_poly_bc_1.cas'
    stdin, stdout, stderr = ssh.exec_command(dd)      # scratch 폴더 적용
    ddd = stdout.readlines()
    txt_writing(str(now), ddd)
    exit_status = stdout.channel.recv_exit_status()
    time.sleep(1)
    ssh.close()

i = 1
while i > 0:
    aspera_()
    time.sleep(60*30)