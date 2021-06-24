
import random




def double_pooling(batch_size,data):

    # create sub_batches
    test_numbers_in_sub_batch=0
    double_batches=[]

    for i in range(0,batch_size+1):
        double_batches.append([])
    counter=0
    for i in range(0,batch_size):
        j=i+1
        while(len(double_batches[i])<batch_size):
            double_batches[i].append(data[counter])
            double_batches[j].append(data[counter])
            counter=counter+1
            j=j+1
    #print(double_batches)

    test_numbers_in_sub_batch=test_numbers_in_sub_batch+batch_size+1
    result=[]
    for sub_double_batch in double_batches:
        result.append(run_batch(sub_double_batch))
    faild_builds=0
    #print(result)
    for flag in result:
        if(flag==False):
            faild_builds=faild_builds+1
    if(faild_builds<=2):
        return test_numbers_in_sub_batch
    else:
        num=faild_builds-1
        #print(num)
        addition=(num*(num+1)/2)
        return (test_numbers_in_sub_batch+addition)







def run_batch(batch):
    for element in batch:
        if element==False:
            return False
            break

    return True

def assign_pooling(batch_size,data):
    total_test=0
    sub_batch_size=int((batch_size*(batch_size+1))/2)
    batch_numbers=(int)(len(data)/sub_batch_size)
    counter=0
    for i in range(0,batch_numbers):
        upper_bound=(counter+sub_batch_size)
        sub_batch=data[counter:upper_bound]
        a=double_pooling(batch_size,sub_batch)
        total_test=total_test+a
        #print(a,"salam")
        counter=counter+sub_batch_size
    return total_test









import numpy as np
import pandas as pd
import math
import random
import os

#data=data[236:]     #ruby--ruby.csv
#data=data[6:]      #puppetlabs--puppet.csv
#data=data[7:]     #rspec--rspec-core.csv
#data=data[94:]     #opal--opal.csv


#print(1-(assign_pooling(7,data)/len(data)))

def run_simulation():
    project_names = ['vagrant', 'rails', 'okhttp', 'gradle', 'cloudify', 'puppet', 'opal', 'ownlcloud', 'graylog2',
                     'ruby', 'metasploit', 'rspec']

    savings_for_pejects = []
    projects = (os.listdir("./data/extracted_project_travis"))

    colors_name = ["green", "gold", "orange", "gray", "black", "pink", "lime", "tan", "red", "blue", "purple",
                   "darksalmon"]
    for i in range(0, len(projects)):
        savings_for_pejects.append([])

    global data
    projects = (os.listdir("./data/extracted_project_travis"))
    for size in range(2, 21):
        print(size)
        for j in range(0,len(projects)):
            project_path = './data/extracted_project_travis/' + projects[j]
            data = pd.read_csv(project_path)

            if (projects[j] == 'ruby.csv'):
                data = data[data.git_branch == "trunk"]
            else:
                data = data[data.git_branch == "master"]

            data = data.build_successful
            data = pd.Series.tolist(data)
            data = data[100:]
         #   test_number=1 - (assign_pooling(size, data) / len(data))
            savings_for_pejects[j].append(1 - (assign_pooling(size, data) / len(data)))
    print(savings_for_pejects)
    for lis in savings_for_pejects:
        lis.insert(0, 0)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    import matplotlib.pyplot as plt

    yaxis = list(range(1, 20 + 1))
    axes = plt.axes()

    axes.set_xticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    print(len(savings_for_pejects[0]))
    average = []
    for i in range(0, len(savings_for_pejects[0])):
        sum = 0
        for lis in savings_for_pejects:
            sum += lis[i]
        average.append(sum / len(savings_for_pejects))
    for i in range(0, len(savings_for_pejects)):
        plt.plot(yaxis, savings_for_pejects[i], colors_name[i], label=project_names[i])
    plt.xlabel('Batch Size')
    plt.ylabel('Saving%')

    plt.legend()
    plt.show()
    print(average)


run_simulation()