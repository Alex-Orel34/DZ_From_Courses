import time
from datetime import datetime

import argparse

p = argparse.ArgumentParser()
p.add_argument('-family', '--fam')
p.add_argument('-hours', '--h', default=0, type=int)
p.add_argument('-minutes', '--min', default=0, type=int)
p.add_argument('-seconds', '--sec', default=30, type=int)
l = p.parse_args()
print(l)

with open('log.txt', 'a') as file:
    file.write(f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - {l.fam} \n')
while l.h or l.min or l.sec:
    time_now = ''
    if l.h <= 9:
        time_now += f'0{l.h}'
    else:
        time_now += f'{l.h}'

    if l.min <= 9:
        time_now += f':0{l.min}'
    else:
        time_now += f':{l.min}'

    if l.sec <= 9:
        time_now += f':0{l.sec}'
    else:
        time_now += f':{l.sec}'
    print(time_now)
    time.sleep(1)
    if l.sec == 0 and l.min > 0:
        l.min -= 1
        l.sec += 59
    elif l.sec == 0 and l.min == 0 and l.h > 0:
        l.h -= 1
        l.min += 59
        l.sec += 59
    else:
        l.sec -= 1
else:
    print('ALARM!!!!')
