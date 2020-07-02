FROM ubuntu:18.04

WORKDIR /home/Handson-ML


RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y build-essential

RUN apt-get install python3.6 -y python3-pip -y

RUN pip3 install jupyter
RUN jupyter notebook --generate-config
RUN mkdir /root/.jupyter/custom
RUN echo '.CodeMirror pre {font-family: Inconsolata-g; font-size: 12pt; line-height: 140%;}\n.container { width:100% !important; }\ndiv.output pre{\n    font-family: Inconsolata-g;\n    font-size: 12pt;\n}' >> /root/.jupyter/custom/custom.css

ADD requirements.txt /home/Handson-ML
RUN pip3 install -r /home/Handson-ML/requirements.txt