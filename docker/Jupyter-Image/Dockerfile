FROM ubuntu:latest
MAINTAINER NAME weynand@threefold.io

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y build-essential
RUN apt -y install net-tools
RUN apt -y install python3
RUN apt -y install python-pip
RUN pip install jupyter
RUN pip install notebook
RUN pip install jupyterlab

# ENTRYPOINT ["/usr/local/bin/jupyter-lab", "--no-browser"]
