import datetime
import shutil
import time

from game_reserv_dirrectory import from_dist, to_dist
print ('Import:OK')
def what_time () :    
    d_time = datetime.datetime.now()
    return d_time

print ('Im at work. To stop me close console window after gaming over.')
p=1
reserv_time = 900
while p != 0:    
    now_time = what_time() #2023-05-27 01:39:35.239285
    now_time_name= now_time.replace(microsecond=0) #2023-05-27 01:39:35
    now_time_name= str(now_time_name)
    now_time_name = now_time_name.replace(':','-')

    shutil.copytree(from_dist,to_dist+'//'+now_time_name)
    print('Copied ' + str(p) + ' times. Now Im wating ' + str(reserv_time) +' sec.')

    time.sleep(reserv_time)
       
    p+=1
