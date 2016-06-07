'''
Created on 13/05/2016

@author: caio
'''

if __name__ == '__main__':
    pass

import scp_time
import sys

target_ip = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
scp_file_source = sys.argv[4]
scp_file_destiny = sys.argv[5]

fsttime = scp_time.get_time()
result = scp_time.scp(target_ip, user, password, scp_file_source , scp_file_destiny, 1 )

if result is -1:
    sys.exit(1)

scdtime = scp_time.get_time()

print str( scdtime - fsttime ) 