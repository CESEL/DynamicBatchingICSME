from constant_batch_size import ConstantBatching
from weighted_smoothing import WeigtedSmoothing
from weighted_smoothing import WeigtedSmoothing

import random

optimum_batch_sizes=[]
results=[]
for i in range(0,50):
    results.append([])
for i in range(1,50):
    min=100000000
    min_size=1
    print(i)
    p=i/100
    data=[]
    for k in range(0,100000):
        a=random.uniform(0, 1)
        if(a<p):
            data.append(False)
        else:
            data.append(True)
    for k in range(1,21):
        ws = ConstantBatching(data, k,method='pool_testing')
        test_number = (ws.run())
        results[i-1].append(test_number)
        if(test_number<min):
            min=test_number
            min_size=k

    optimum_batch_sizes.append(min_size)

print(optimum_batch_sizes)





print(results)





