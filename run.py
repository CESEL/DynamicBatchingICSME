from constant_batch_size import ConstantBatching
from weighted_smoothing import WeigtedSmoothing

import pandas as pd
import os
projects=(os.listdir("./data/extracted_project_travis"))
#data = data[data.git_branch == "trunk"]



def calc_failure_rate(result_list):
    failure_count=0
    for result in result_list:
        if(result==False):
            failure_count+=1
    return (failure_count/len(result_list))

option = int(input("""Please choose an option (1-9):
1- batchBisect8
2- batch4
3- Dorfman4
4- constant batching double pool testing
5- DynamicBatching pooling
6- DynamicBatching double pooling
7- DynamicBatching BatchBisect
8- DynamicBatching BatchStop4
9- DynamicBatching BatchDivide4
"""))


for project in projects:
    project_path='./data/extracted_project_travis/'+project
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

    a = option

    if (a == 1):  # batchBisect8
        ws = ConstantBatching(data, 8, 'batch_bisect')

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data) - 100)))

    elif (a == 2):  # batch4
        ws = ConstantBatching(data, 4)

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data))))

    elif (a == 3):  # Dorfman4
        ws = ConstantBatching(data, 4)

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data))))

    elif (a ==4):  # constant batching double pool testing
        import double_pooling



    elif (a == 5):  # dynamic batching pooling

        ws = WeigtedSmoothing(data, 'pool_testing')

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data) - 100)))


    elif (a == 6):  # dynamic batching  double pooling
        import double_pooling_variable





    elif (a == 7):  # dynamicBatching BatchBisect
        ws = WeigtedSmoothing(data, 'batch_bisect')

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data) - 100)))

    elif (a == 8):  # dynamicBatching BatchStop4
        ws = WeigtedSmoothing(data, 'batch_stop4')

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data) - 100)))

    elif (a == 9):  # dynamicBatching BatchDivide4
        ws = WeigtedSmoothing(data, 'batch_divide4')

        test_number = (ws.run())
        print(project, 1 - (test_number / (len(data) - 100)))




