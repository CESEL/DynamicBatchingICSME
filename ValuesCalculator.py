import pandas as pd
import os
projects=(os.listdir("./data/extracted_project_travis"))



def failure_rate():
    for project in projects:
        project_path = './data/extracted_project_travis/' + project
        data = pd.read_csv(project_path)
        counter=0

        if(project=='ruby--ruby.csv'):
            data=data[data.git_branch=="trunk"]
        elif(project[i]=='sling.csv'):
            data=data[data.git_branch=="trunk"]

        else:
            data=data[data.git_branch=="master"]

        data = data.build_successful
        data = pd.Series.tolist(data)
        data=data[0:]
        for j in  range(0,len(data)):
            if(data[j]==False):
                counter+=1
        print(counter/len(data),len(data),data_file[i])





def repetitive_failure_rate():
    global data

    for project in projects:
        counter=0
        counter1=0
        project_path = './data/extracted_project_travis/' + project
        data = pd.read_csv(project_path)
        if (project == 'ruby.csv'):
            data = data[data.git_branch == "trunk"]
        else:
            data = data[data.git_branch == "master"]
        data = data[100:]
        data = data.build_successful
        data = pd.Series.tolist(data)

        for j in  range(1,len(data)-1):
            if(data[j]==False):
                counter1+=1

            if(data[j]==False and data[j+1]==False):
                counter+=1


        print((counter/counter1), project)

def theoretical_limit():
    global data
    data_file=["ruby--ruby.csv",'rapid7--metasploit-framework.csv',"Graylog2--graylog2-server.csv","owncloud--android.csv","mitchellh--vagrant.csv","gradle--gradle.csv","puppetlabs--puppet.csv","opal--opal.csv","rspec--rspec-core.csv","okhttp.csv"]

    for project in projects:
        counter=0
        counter1=0
        project_path = './data/extracted_project_travis/' + project
        data = pd.read_csv(project_path)
        if (project == 'ruby.csv'):
            data = data[data.git_branch == "trunk"]
        else:
            data = data[data.git_branch == "master"]
        data = data[100:]
        data = data.build_successful
        data = pd.Series.tolist(data)

        for j in  range(1,len(data)-1):

            if(data[j]==False ):
               counter+=1
            elif(data[j]==True and data[j-1]==False):
                counter+=1
        print(1-(counter/len(data)),len(data),project)




theoretical_limit()


