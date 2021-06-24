from batching_techniques import batch_stop4,batch_divide4,batch_bisect,back_to_one,pool_testing

class ConstantBatching():

    def __init__(self,batch,batch_size=4,method='batch_stop4'):

        self.batch=batch
        self.batch_size=batch_size
        self.method=method
        self.disspatcher_batching_technique={'batch_stop4':batch_stop4,'batch_bisect':batch_bisect,'batch_divide4':batch_divide4,'back_to_one':back_to_one, 'pool_testing':pool_testing}






    @staticmethod
    def runbatch(batch):

        for test in batch:
            if (test == False):
                return False
        return True


    def run(self):
        test_number=0
        batch_size=self.batch_size
        counter = 0
        flag = True
        i = 0
        while (flag):
            i = i + 1

            test_number = test_number + 1
            slicebatch = self.batch[counter:(counter + batch_size)]
            counter = counter + batch_size

            if (self.runbatch(slicebatch) == False and batch_size != 1):
                test_number+=self.disspatcher_batching_technique[self.method](slicebatch)

     #           test_number+=self.disspatcher[self.method](slicebatch)
    #        if (slicebatch[-1] == False):
    #            if (self.method== "back_to_one"):
    #                batch_size = 1

#              else:
#                    batch_size = self.batch_size

            if (counter >= len(self.batch)):
                flag = False
        return test_number







