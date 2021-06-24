
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


def run_simulation():
    global data
    projects = (os.listdir("./data/extracted_project_travis"))
    for project in projects:
        project_path = './data/extracted_project_travis/' + project
        data = pd.read_csv(project_path)

        if (project == 'ruby.csv'):
            data = data[data.git_branch == "trunk"]
        else:
            data = data[data.git_branch == "master"]

        data = data.build_successful
        data = pd.Series.tolist(data)
        data = data[100:]


        print(project, 1 - (assign_pooling(9, data) / len(data)))






run_simulation()