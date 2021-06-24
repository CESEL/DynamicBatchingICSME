from constant_batch_size import ConstantBatching
import pandas as pd
import os
projects=(os.listdir("./data/extracted_project_travis"))
print(projects)

project_names=['vagrant', 'rails', 'okhttp', 'gradle', 'cloudify', 'puppet', 'opal', 'ownlcloud', 'graylog2', 'ruby', 'metasploit', 'rspec']
savings_for_pejects=[]
colors_name=["green", "gold", "orange", "gray", "black", "pink", "lime", "tan", "red",  "blue","purple", "darksalmon"]
for i in range(0,len(projects)):
    savings_for_pejects.append([])

for i in range(2,21):
    print(i)
    for j in range(0,len(projects)):
        project_path = './data/extracted_project_travis/' + projects[j]
        data = pd.read_csv(project_path)
        if (projects[j] == 'ruby.csv'):
            data = data[data.git_branch == "trunk"]
        else:
            data = data[data.git_branch == "master"]
        data = data[100:]
        data = data.build_successful
        data = pd.Series.tolist(data)
        ws = ConstantBatching(data, i,'batch_bisect')
        test_number = (ws.run())
        savings_for_pejects[j].append(1 - (test_number / (len(data))))

print(savings_for_pejects)
for lis in savings_for_pejects:
    lis.insert(0, 0)
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
import matplotlib.pyplot as plt

yaxis = list(range(1, 20 + 1))
axes = plt.axes()

axes.set_xticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

print(len(savings_for_pejects[0]))
average=[]
for i in range(0,len(savings_for_pejects[0])):
    sum=0
    for lis in savings_for_pejects:
        sum+=lis[i]
    average.append(sum/len(savings_for_pejects))
for i in range(0,len(savings_for_pejects)):
    plt.plot(yaxis,savings_for_pejects[i],colors_name[i], label=project_names[i])
plt.xlabel('Batch Size')
plt.ylabel('Saving%')

plt.legend()
plt.show()
print(average)
