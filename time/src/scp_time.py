'''
Created on 13/05/2016

@author: caio
'''

import os,errno
import datetime
import paramiko
from scp import SCPClient

'''

get machine time

'''

def get_time():
    return datetime.datetime.now()

'''

create a list of file in a directory

'''

def list_directory( directory ):
      
    try:
        names = os.listdir( directory )
    except OSError, err:
        if err.errno is errno.ENOENT:
            print "\nThere is no directory '{0}'" .format( directory )
            return -1
    
    return names
      
'''

transfer data through scp

'''


def scp( target_ip, user , password , scp_file , destiny , is_directory ):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    ssh.connect( target_ip , username = user , password = password )
   
    if is_directory is 0:
        with SCPClient( ssh.get_transport() ) as scp_connection:
            scp_connection.put( scp_file , destiny )   
            scp_connection.close()
        
    else:
        names = list_directory( scp_file ) 
        
        if names is -1:
            return names
        
        for i in range( 0, (len(names))):
            with SCPClient( ssh.get_transport() ) as scp_connection:
                scp_connection.put( (scp_file + names[i] )  , destiny )   
                
        scp_connection.close()
        return 0