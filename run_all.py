from constant_batch_size import ConstantBatching
from weighted_smoothing import WeigtedSmoothing
import os

import pandas as pd
import os
projects=(os.listdir("./data/extracted_project_travis_all"))

def calc_failure_rate(result_list):
    failure_count=0
    for result in result_list:
        if(result==False):
            failure_count+=1
    return (failure_count/len(result_list))


for project in projects:
    project_path='./data/extracted_project_travis_all/'+project
    data = pd.read_csv(project_path)
    if(project=='ruby.csv'):
        data=data[data.git_branch=="trunk"]
    else:
        data = data[data.git_branch == "master"]
    data = data[100:]

    #     elif(data_file[i]=='sling.csv'):
    #         data=data[data.git_branch=="trunk"]
       #  else:
    data = data.build_successful
    data = pd.Series.tolist(data)
  #  print(calc_failure_rate(data))

  #  print(len(data))
    if(len(data)>2000):
        ws=WeigtedSmoothing(data)
        test_number_backto1=(ws.run())
        ws=WeigtedSmoothing(data,'batch_divide4')
        test_number_batchstop4=(ws.run())
        cb=ConstantBatching(data,4)
        test_number_constantbatching=(cb.run())

        print(project, "  ", len(data), " ", calc_failure_rate(data), " ",  1 - (test_number_backto1 / (len(data)-100))," ", 1 - (test_number_batchstop4 / (len(data)-100))," ", 1 - (test_number_constantbatching / (len(data))))

