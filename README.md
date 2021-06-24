# Replication Package

Paper Title: "Mining Historical Test Failures to Dynamically Batch Tests to Save CI Resources"

Authors: Amir Hossein Bavand, and Peter C. Rigby

Contact us:  <a_bavand@encs.concordia.ca>, <peter.rigby@concordia.ca>


### Instalation and running

1. Install [Docker](https://docs.docker.com/get-docker/) on your computer.
2. Clone this github repo, this includes both the code and the [data](https://github.com/CESEL/BatchBuilderResearch/tree/master/RQ3/data/extracted_project_travis)
3. In the terminal, go to this directory and run the commands below

<code> docker build -t rq3 .</code>

In which "rq1and" is the name of the docker image

5. After completing the build process, run the following command, with project ID

<code> docker run -it rq3 </code>

