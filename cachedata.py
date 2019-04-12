import time
import random
picked = []
table = {}
t1 = time.time()
for i in range(1000):
    
    v = random.randint(1,20)
    print('i = {}, picked {}'.format(i, v))
    picked.append(v)
    if v not in table:
        table[v] = [[round((time.time()-t1)/10000,5)]]
    else:
        table[v].append([round((time.time()-t1)/10000,5)])
    time.sleep(1)
    
table_data = open('table_data.py', 'w')
data = 'table = {} \nseq = {}'.format(table, picked)
table_data.write(data)
table_data.close()


