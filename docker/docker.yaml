FROM ubuntu 
#quay.io/strimzi/kafka:latest-kafka-3.2.3

ENV SPARK_HOME "/opt/spark/jars"

USER root

WORKDIR /opt/spark/jars
WORKDIR /app

COPY ./app/ /app/

RUN apt update
RUN apt install python3-pip -y
RUN apt install curl -y
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.13/3.3.1/spark-sql-kafka-0-10_2.13-3.3.1.jar \ 
    --output spark-sql-kafka-0-10_2.13-3.3.1.jar \
    && mv spark-sql-kafka-0-10_2.13-3.3.1.jar ${SPARK_HOME}   
RUN curl https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.13/3.3.1/spark-streaming-kafka-0-10-assembly_2.13-3.3.1.jar \ 
    --output spark-streaming-kafka-0-10-assembly_2.13-3.3.1.jar \
    && mv spark-streaming-kafka-0-10-assembly_2.13-3.3.1.jar ${SPARK_HOME}

RUN pip install pyspark==3.3.1
RUN pip install delta-spark

USER 1001
