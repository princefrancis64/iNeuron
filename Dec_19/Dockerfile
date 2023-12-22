#Use the official Python 3.8 as the base image
FROM python:3.8

#set the user to root
USER root

# Create a directory named /app
RUN mkdir /app

#Copy the contents of the current directory to  /app in the container
COPY ./app/

#Set the working directory to /app
WORKDIR /app/

#Install python dependencies form requirements.txt
RUN pip3 install -r requirements.txt

# Set environment variables for Apache Airflow
ENV AIRFLOW_HOME = "/app/airflow"
ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT = 1000
ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING = True

#Initializing the airflow databse
RUN airflow db init

#Create and Airflow user
RUN airflow users create -e prince.francis64@gmail.com -f Prince -l Francis -p admin -r Admin -u admin

#Change permissions for start.sh
RUN chmod 777 start.sh

#Install AWS CLI
RUN apt update -y && apt install awscli -y

#Sets the default entry point of the container to /bin/sh
ENTRYPOINT ["/bin/sh"]

#Default command to run when the container starts
CMD["start.sh"]