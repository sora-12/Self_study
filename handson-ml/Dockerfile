FROM ubuntu:18.04

WORKDIR /home/Handson-ML


RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y build-essential

RUN apt-get install python3.6 -y python3-pip -y

RUN pip3 install jupyter
RUN jupyter notebook --generate-config --allow-root



ADD requirements.txt /home/Handson-ML
RUN pip3 install -r /home/Handson-ML/requirements.txt

# jt -t grade3 -f roboto -fs 12 -altp -tfs 12 -nfs 12 -cellw 80% -T -N
