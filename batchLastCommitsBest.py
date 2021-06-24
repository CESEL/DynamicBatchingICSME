import numpy as np
import pandas as pd
import math
import random
from math import log
import os

from matplotlib import pyplot as plt

testNumber=4
brokenBatches=0







def simple_batching(batch_size,maximum):
    return maximum

def constant_batching(batch_size,maximum):
    return maximum



TestForEvalNUmber=0






def GeneralBatchStop41(batch):
    global TestForEvalNUmber



    if(len(batch)==12):
        sub_batch_1=batch[0:3]
        sub_batch_2=batch[3:6]
        sub_batch_3=batch[6:9]
        sub_batch_4=batch[9:12]
        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4


    elif(len(batch)==13):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:7]
        sub_batch_3=batch[7:10]
        sub_batch_4=batch[10:13]
        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4

    elif (len(batch) == 14):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:7]
        sub_batch_3 = batch[7:11]
        sub_batch_4 = batch[11:14]
        if (runbatch(sub_batch_1) == False):
            batchstop41(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            batchstop41(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            batchstop41(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber = TestForEvalNUmber + 4




    elif(len(batch)==15):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:15]
        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4



    elif(len(batch)==16):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:16]

        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4
    elif(len(batch)==17):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:17]

        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4

    elif(len(batch)==18):
        sub_batch_1=batch[0:5]
        sub_batch_2=batch[5:9]
        sub_batch_3=batch[9:14]
        sub_batch_4=batch[14:18]

        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4

    elif(len(batch)==19):
        sub_batch_1=batch[0:5]
        sub_batch_2=batch[5:9]
        sub_batch_3=batch[9:14]
        sub_batch_4=batch[14:19]

        if(runbatch(sub_batch_1)==False):
            batchstop41(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop41(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop41(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop41(sub_batch_4)
        TestForEvalNUmber=TestForEvalNUmber+4




    elif (len(batch)<=4):
        TestForEvalNUmber=TestForEvalNUmber+len(batch)
    else:

        sub_batch_right=batch[0:(int)(len(batch)/2)]
        sub_batch_left=batch[(int)(len(batch)/2):len(batch)]
        if(runbatch(sub_batch_right)==False):
            batchstop41(sub_batch_right)
        if(runbatch(sub_batch_left)==False):
            batchstop41(sub_batch_left)
        TestForEvalNUmber=TestForEvalNUmber+2






def batchstop41(batch):
    global TestForEvalNUmber

    if (len(batch)<=4):
        TestForEvalNUmber=TestForEvalNUmber+len(batch)
    else:
        sub_batch_right=batch[0:(int)(len(batch)/2)]
        sub_batch_left=batch[(int)(len(batch)/2):len(batch)]
        if(runbatch(sub_batch_right)==False):
            batchstop41(sub_batch_right)
        if(runbatch(sub_batch_left)==False):
            batchstop41(sub_batch_left)
        TestForEvalNUmber=TestForEvalNUmber+2





def calc_batch(batch):

    max=0
    max_i=1
    for i in range(1,20):
        batch_size1 = i
        global TestForEvalNUmber
        counter = 0
        flag = True
        while (flag):

            TestForEvalNUmber = TestForEvalNUmber + 1

            slicebatch = batch[counter:(counter + batch_size1)]

            counter = counter + batch_size1
            if (runbatch(slicebatch) == False and batch_size1 != 1):
                GeneralBatchStop41(slicebatch)
                #batchstop41(slicebatch)

            new_batchsize1=i

            batch_size1 = new_batchsize1
            if ((counter) >= len(batch)):
                flag = False
        if(1-(TestForEvalNUmber/len(batch))>max):
            max=1-(TestForEvalNUmber/len(batch))
            max_i=i
        TestForEvalNUmber=0

    return max_i



def weighted_average_bathing(sub_batch):
    if(len(sub_batch)==0):
        return 4
    else:
        a=calc_batch(sub_batch)
        return a





batch_size=1

def variablebatching(batch,b,func):
    batchsizes=[]
    global batch_size
    batch_size=4
    global testNumber
    global brokenBatches
    counter=100
    flag=True
    i=0
    while(flag):
        i=i+1

        testNumber=testNumber+1
        slicebatch=batch[counter:(counter+batch_size)]
        counter=counter+batch_size
        if(runbatch(slicebatch)==False and batch_size!=1):
        #    GeneralBatchStop4(slicebatch)
        #    batchstop4(slicebatch)
            batch_bisect(slicebatch)

        new_batchsize = weighted_average_bathing(batch[0:(counter)])

     #   new_batchsize=4

    #    if( slicebatch[-1]==False ):
    #        if(func.__name__=="constant_batching"):
    #            pass
    #        else:
    #            new_batchsize=1


        batch_size=new_batchsize
        batchsizes.append(batch_size)
    #    print(batch_size)
        if(counter>=len(batch)):
            flag=False
    print(batchsizes)
    plt.title("salam")
    plt.plot(batchsizes)
    plt.legend()

    plt.show()



def GeneralBatchStop4(batch):
    global testNumber



    if(len(batch)==12):
        sub_batch_1=batch[0:3]
        sub_batch_2=batch[3:6]
        sub_batch_3=batch[6:9]
        sub_batch_4=batch[9:12]
        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4


    elif(len(batch)==13):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:7]
        sub_batch_3=batch[7:10]
        sub_batch_4=batch[10:13]
        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4

    elif (len(batch) == 14):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:7]
        sub_batch_3 = batch[7:11]
        sub_batch_4 = batch[11:14]
        if (runbatch(sub_batch_1) == False):
            batchstop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            batchstop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            batchstop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            batchstop4(sub_batch_4)
        testNumber = testNumber + 4




    elif(len(batch)==15):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:15]
        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4



    elif(len(batch)==16):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:16]

        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4



    elif(len(batch)==17):
        sub_batch_1=batch[0:4]
        sub_batch_2=batch[4:8]
        sub_batch_3=batch[8:12]
        sub_batch_4=batch[12:17]

        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4

    elif(len(batch)==18):
        sub_batch_1=batch[0:5]
        sub_batch_2=batch[5:9]
        sub_batch_3=batch[9:14]
        sub_batch_4=batch[14:18]

        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4

    elif(len(batch)==19):
        sub_batch_1=batch[0:5]
        sub_batch_2=batch[5:9]
        sub_batch_3=batch[9:14]
        sub_batch_4=batch[14:19]

        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)
        testNumber=testNumber+4








    elif(len(batch)==20):
        sub_batch_1=batch[0:5]
        sub_batch_2=batch[5:10]
        sub_batch_3=batch[10:15]
        sub_batch_4=batch[15:20]

        if(runbatch(sub_batch_1)==False):
            batchstop4(sub_batch_1)
        if(runbatch(sub_batch_2)==False):
            batchstop4(sub_batch_2)
        if(runbatch(sub_batch_3)==False):
            batchstop4(sub_batch_3)
        if(runbatch(sub_batch_4)==False):
            batchstop4(sub_batch_4)



    elif (len(batch)<=5):
        testNumber=testNumber+len(batch)
    else:

        sub_batch_right=batch[0:(int)(len(batch)/2)]
        sub_batch_left=batch[(int)(len(batch)/2):len(batch)]
        if(runbatch(sub_batch_right)==False):
            batchstop4(sub_batch_right)
        if(runbatch(sub_batch_left)==False):
            batchstop4(sub_batch_left)
        testNumber=testNumber+2



def batchstop4(batch):
    global testNumber

    if (len(batch)<=4):
        testNumber=testNumber+len(batch)
    else:
        sub_batch_right=batch[0:(int)(len(batch)/2)]
        sub_batch_left=batch[(int)(len(batch)/2):len(batch)]
        if(runbatch(sub_batch_right)==False):
            batchstop4(sub_batch_right)
        if(runbatch(sub_batch_left)==False):
            batchstop4(sub_batch_left)
        testNumber=testNumber+2


def batch_bisect(batch):
    global testNumber



    if (len(batch) <= 2):
        testNumber=testNumber+len(batch)
    else:
        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            rc= batch_bisect(sub_batch_right)

        if (runbatch(sub_batch_left) == False):
            lc= batch_bisect(sub_batch_left)

        testNumber=testNumber+2



def runbatch(batch):

    for test in batch:
        if(test==False):
            return False
    return True


li=[]





def runfunction():
    global testNumber
    global brokenBatches
  #  functions = [constant_batching,simple_batching]
    functions = [simple_batching]

    for func in functions:
        li = []

        for i in range(1,2):
            testNumber = 0
            brokenBatches=0

            variablebatching(data, i,func)

            li.append(1 - (testNumber / (len(data)-100)))
            #print(brokenBatches,"broken")
        print(sorted(li)[-1], func.__name__)



def run_Project():
    global data
  #  data_file=["ruby--ruby.csv",'rapid7--metasploit-framework.csv',"Graylog2--graylog2-server.csv","owncloud--android.csv","mitchellh--vagrant.csv","gradle--gradle.csv","puppetlabs--puppet.csv","opal--opal.csv","rspec--rspec-core.csv","sonarqube.csv","okhttp.csv"]

 #   data_file=['Achilles.csv','buck.csv','cloudify.csv','deeplearning4j.csv','DSpace.csv','dynjs.csv','graylog2-server.csv','HikariCP.csv','jade4j.csv','jcabi-github.csv','jetty.project.csv','jOOQ.csv','jsprit.csv',
 #              'LittleProxy.csv','okhttp.csv','optiq.csv','sling.csv','sonarqube.csv','titan.csv','wicket-bootstrap.csv']

  #  data_file=['buck.csv','cloudify.csv','DSpace.csv','graylog2-server.csv','jcabi-github.csv','jOOQ.csv',
   #               'okhttp.csv','sling.csv','sonarqube.csv','deeplearning4j.csv']

  #  data_file=["rspec--rspec-core.csv"]
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
        print(len(data))
        if (len(data) > 500, ):

            data=data[100:]
            print(len(data),"ths is length of the data", project)
            runfunction()





run_Project()
#run_simulation()




