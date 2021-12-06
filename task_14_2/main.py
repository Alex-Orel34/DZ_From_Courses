import argparse
from datetime import datetime
import time

p = argparse.ArgumentParser()
p.add_argument('-name', '--Name')
p.add_argument('-surname', '--Surname')
p.add_argument('-focusing_min', '--Focusing_time', default=25, type=int)
p.add_argument('-break', '--Break_time', default=5, type=int)
p.add_argument('-cycle', '--cycles', default=4, type=int)
p.add_argument('-task', '--Name_task', default=None, type=str)
l = p.parse_args()
with open('log.txt', 'a') as file:
    file.write(
        f'{datetime.now().strftime("%d/%m/%y %H:%M:%S")} - {l.Name} {l.Surname}, 'f'{l.Focusing_time} min, pause {l.Break_time} min, 'f'{l.cycles} cycles, {l.Name_task} \n')
work = l.Focusing_time
while l.cycles != 0 or work != 0:
    print(f'Until the end of the work left {work} minutes')
    time.sleep(1)
    work -= 1
    if work == 0 and l.cycles > 0:
        print(f'You have {l.Break_time} min of break')
        time.sleep(l.Break_time * 60)
        l.cycles -= 1
        work = l.Focusing_time
print('END!) go to bed')
