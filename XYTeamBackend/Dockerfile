# set the base image 
FROM python:3.10.14
# File Author / Maintainer
MAINTAINER 1577212376@qq.com
#add project files to the usr/src/app folder
ADD . /usr/src/app
#set directoty where CMD will execute 
WORKDIR /usr/src/app
COPY requirements.txt ./
# Get pip to download and install requirements:
# RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools==57.5.0
RUN pip install -r requirements.txt
# Expose ports
EXPOSE 8000
# default command to execute    
CMD python manage.py runserver 0.0.0.0:8000