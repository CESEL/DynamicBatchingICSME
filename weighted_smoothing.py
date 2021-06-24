from batching_techniques import batch_stop4,batch_divide4,batch_bisect,back_to_one,pool_testing
from math import log


class WeigtedSmoothing():

    def __init__(self,batch,batching_technique='back_to_one',smoothing_function='normal'):
        self.batch=batch
        self.batching_technique=batching_technique
        self.smoothing_function=smoothing_function
        self.disspatcher_batching_technique={'batch_stop4':batch_stop4,'batch_bisect':batch_bisect,'batch_divide4':batch_divide4,'back_to_one':back_to_one, 'pool_testing':pool_testing}




    def optimal_size_based_on_failure_rate(self,failure_rate):
        if (failure_rate < 0.003):
            return 20
        elif (failure_rate < 0.005):
            return 17
        elif (failure_rate < 0.01):
            return 16
        elif (failure_rate < 0.02):
            return 15
        elif (failure_rate < 0.03):
            return 12
        elif (failure_rate < 0.055):
            return 11
        elif (failure_rate < 0.07):
            return 7

        elif (failure_rate < 0.1):
            return 6
        elif (failure_rate < 0.15):
            return 5

        elif (failure_rate < 0.2):
            return 4
        elif (failure_rate < 0.4):
            return 3
        elif (failure_rate >= 0.4 and failure_rate < 0.5):
            return 2

        else:

            return 1



    def optimal_size_based_on_failure_rate_pooling(self,failure_rate):   #pool_testing
        if (failure_rate < 0.02):
            return 10
        elif (failure_rate < 0.03):
            return 8
        elif (failure_rate < 0.5):
            return 6
        elif (failure_rate < 0.07):
            return 5
        elif (failure_rate < 0.12):
            return 4
        elif (failure_rate < 0.30):
            return 3

        else:
            return 1



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
        if(self.batching_technique=='pool_testing'):
            return self.optimal_size_based_on_failure_rate_pooling(failure_rate)
        else:
            return self.optimal_size_based_on_failure_rate(failure_rate)

    def weighted_failure_rate_devide_to_log_location(self,sub_batch):
        failure_count = 0
        denom = 0
        number = 0
        #   print(sub_batch)

        for i in range(0, len(sub_batch)):
            denom = denom + log(i + 1)
            if (sub_batch[i] == False):
                number = number + log(i + 1)

        try:
            failure_rate = number / denom
        except:
            failure_rate = 0.07
        return self.optimal_size_based_on_failure_rate(failure_rate)


    @staticmethod
    def runbatch(batch):

        for test in batch:
            if (test == False):
                return False
        return True

    def run(self):
        test_number=0

        batch_size = 4
        counter = 100
        flag = True
        i = 0
        while (flag):
            i = i + 1

            test_number = test_number + 1
            slicebatch = self.batch[counter:(counter + batch_size)]
            counter = counter + batch_size

            if (self.runbatch(slicebatch) == False and batch_size != 1):
                test_number+=self.disspatcher_batching_technique[self.batching_technique](slicebatch)

            batch_size = self.weighted_failure_rate_devide_to_location(self.batch[counter - 100:(counter)])

            if (slicebatch[-1] == False):
                if (self.batching_technique== "back_to_one"):
                    batch_size = 1

            if (counter >= len(self.batch)):
                flag = False
        return test_number




