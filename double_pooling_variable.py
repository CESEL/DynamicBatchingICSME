

class WeigtedSmoothing():

    def __init__(self,batch):
        self.batch=batch





    def optimal_size_based_on_failure_rate(self,failure_rate):   #pool_testing
        if (failure_rate < 0.02):
            return 20
        elif (failure_rate < 0.03):
            return 17
        elif (failure_rate < 0.04):
            return 12
        elif (failure_rate < 0.05):
            return 10
        elif (failure_rate < 0.06):
            return 8
        elif (failure_rate < 0.12):
            return 6
        elif (failure_rate < 0.17):
            return 5
        elif (failure_rate < 0.3):
            return 4
        else:
            return 20


    def run_batch(self,batch):
        for element in batch:
            if element == False:
                return False
                break

        return True

    def double_pooling(self,batch_size, data):

        # create sub_batches
        test_numbers_in_sub_batch = 0
        double_batches = []

        for i in range(0, batch_size + 1):
            double_batches.append([])
        counter = 0
        for i in range(0, batch_size):
            j = i + 1
            while (len(double_batches[i]) < batch_size):
                double_batches[i].append(data[counter])
                double_batches[j].append(data[counter])
                counter = counter + 1
                j = j + 1
        # print(double_batches)

        test_numbers_in_sub_batch = test_numbers_in_sub_batch + batch_size + 1
        result = []
        for sub_double_batch in double_batches:
            result.append(self.run_batch(sub_double_batch))
        faild_builds = 0
        # print(result)
        for flag in result:
            if (flag == False):
                faild_builds = faild_builds + 1
        if (faild_builds <= 2):
            return test_numbers_in_sub_batch
        else:
            num = faild_builds - 1
            # print(num)
            addition = (num * (num + 1) / 2)
            return (test_numbers_in_sub_batch + addition)


    def weighted_failure_rate_devide_to_location(self,sub_batch):
        denom = 0
        number = 0
        sub_batch = sub_batch[::-1]

        for i in range(0, len(sub_batch)):
            denom = denom + (1 / (i + 1))
            if (sub_batch[i] == False):
                number = number + (1 / (i + 1))
            failure_rate = number / denom

        try:
            failure_rate = failure_rate
        except:
            failure_rate = 0.07

        return failure_rate


    @staticmethod
    def runbatch(batch):

        for test in batch:
            if (test == False):
                return False
        return True

    def run(self):
        test_number=0

        batch_size=9
        counter = 100
        i = 0
        sub_batch_size = int((batch_size * (batch_size + 1)) / 2)

        batch_size=9
        total_test = 0
        mode = "d"

        while(counter<len(self.batch)):
            a=1
            if(mode=="p"):
                upper_bound = (counter + sub_batch_size)
                sub_batch = self.batch[counter:upper_bound]
                if (len(sub_batch) < sub_batch_size):

                    return total_test
                if(self.runbatch(sub_batch)==True):
                    a=1
                else:
                    a=5
            elif(mode=="d"):


                upper_bound = (counter + sub_batch_size)
                sub_batch = self.batch[counter:upper_bound]
                if(len(sub_batch)<int((batch_size * (batch_size + 1)) / 2)):
                    return total_test

                a = self.double_pooling(batch_size, sub_batch)
            total_test = total_test + a
            counter = counter + sub_batch_size
            if(self.weighted_failure_rate_devide_to_location(self.batch[counter - 100:(counter)])<0.1):

                batch_size = self.optimal_size_based_on_failure_rate(self.weighted_failure_rate_devide_to_location(self.batch[counter - 100:(counter)]))
                sub_batch_size = int((batch_size * (batch_size + 1)) / 2)
                mode="d"

            else:
                batch_size=4
                sub_batch_size=4
                mode="p"



        return total_test


import pandas as pd
import os

projects=(os.listdir("./data/extracted_project_travis"))


def calc_failure_rate(result_list):
    failure_count=0
    for result in result_list:
        if(result==False):
            failure_count+=1
    return (failure_count/len(result_list))


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


    ws=WeigtedSmoothing(data)

    test_number=(ws.run())
    print(project,1 - (test_number / (len(data)-100)))


