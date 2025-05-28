<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# 🛠️ Apache Spark & Kafka Setup Guide

## 🔧 Step-by-Step Installation (Local or Cloud Environment)

### 1. **Apache Kafka (for Streaming)**

* Download from: [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads)
* Install Zookeeper & Kafka

  ```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties
  bin/kafka-server-start.sh config/server.properties
  ```
* Create Kafka topic

  ```bash
  bin/kafka-topics.sh --create --topic tweets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  ```

### 2. **Apache Spark (for Processing)**

* Install Spark (recommended: Spark 3.3+ with Hadoop 3)
* Set up PySpark:

  ```bash
  pip install pyspark
  ```
* Run a Spark streaming job to consume data from Kafka:

  ```python
  spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "tweets") \
    .load()
  ```

### 3. **Optional Tools**

* Use Docker to simplify deployment.
* Use Databricks, Google Colab, or AWS EMR for cloud-based Spark.


## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
