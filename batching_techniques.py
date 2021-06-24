


def runbatch(batch):

    for test in batch:
        if (test == False):
            return False
    return True


def batch_bisect(batch):
    rc =0
    lc =0


    if (len(batch) <= 2):
        return len(batch)
    else:
        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            rc= batch_bisect(sub_batch_right)

        if (runbatch(sub_batch_left) == False):
            lc= batch_bisect(sub_batch_left)

        return (rc +lc +2)


def pool_testing(batch):
    return len(batch)


def batch_stop4(batch):
    rc =0
    lc =0


    if (len(batch) <= 4):
        return len(batch)
    else:
        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            rc= batch_stop4(sub_batch_right)

        if (runbatch(sub_batch_left) == False):
            lc= batch_stop4(sub_batch_left)

        return (rc +lc +2)





def batch_divide4(batch):
    test_number =0
    global testNumber

    if (len(batch) == 12):
        sub_batch_1 = batch[0:3]
        sub_batch_2 = batch[3:6]
        sub_batch_3 = batch[6:9]
        sub_batch_4 = batch[9:12]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4


    elif (len(batch) == 11):
        sub_batch_1 = batch[0:3]
        sub_batch_2 = batch[3:6]
        sub_batch_3 = batch[6:9]
        sub_batch_4 = batch[9:11]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) == 13):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:7]
        sub_batch_3 = batch[7:10]
        sub_batch_4 = batch[10:13]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4


    elif (len(batch) == 14):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:7]
        sub_batch_3 = batch[7:11]
        sub_batch_4 = batch[11:14]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) == 15):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:8]
        sub_batch_3 = batch[8:12]
        sub_batch_4 = batch[12:15]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) == 16):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:8]
        sub_batch_3 = batch[8:12]
        sub_batch_4 = batch[12:16]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4




    elif (len(batch) == 17):
        sub_batch_1 = batch[0:4]
        sub_batch_2 = batch[4:8]
        sub_batch_3 = batch[8:12]
        sub_batch_4 = batch[12:17]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) == 18):
        sub_batch_1 = batch[0:5]
        sub_batch_2 = batch[5:9]
        sub_batch_3 = batch[9:14]
        sub_batch_4 = batch[14:18]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) == 19):
        sub_batch_1 = batch[0:5]
        sub_batch_2 = batch[5:9]
        sub_batch_3 = batch[9:14]
        sub_batch_4 = batch[14:19]
        if (runbatch(sub_batch_1) == False):
            test_number += batch_stop4(sub_batch_1)
        if (runbatch(sub_batch_2) == False):
            test_number += batch_stop4(sub_batch_2)
        if (runbatch(sub_batch_3) == False):
            test_number += batch_stop4(sub_batch_3)
        if (runbatch(sub_batch_4) == False):
            test_number += batch_stop4(sub_batch_4)
        test_number += 4



    elif (len(batch) <= 5):
        test_number = test_number + len(batch)
    else:

        sub_batch_right = batch[0:(int)(len(batch) / 2)]
        sub_batch_left = batch[(int)(len(batch) / 2):len(batch)]
        if (runbatch(sub_batch_right) == False):
            test_number+=batch_stop4(sub_batch_right)
        if (runbatch(sub_batch_left) == False):
            test_number+=batch_stop4(sub_batch_left)
        test_number+=2

    return test_number



def back_to_one(batch):
    return batch_divide4(batch)

