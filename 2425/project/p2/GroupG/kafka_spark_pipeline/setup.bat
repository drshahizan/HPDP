@echo off
echo Setting up Kafka and Spark environment...

REM Create necessary directories
if not exist "spark-apps" mkdir spark-apps
if not exist "spark-data" mkdir spark-data
if not exist "kafka-data" mkdir kafka-data

echo Starting Docker containers...
docker-compose up -d

echo Waiting for services to start...
timeout /t 30

echo Creating Kafka topics...
docker exec kafka kafka-topics --create --topic game-reviews --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
docker exec kafka kafka-topics --create --topic sentiment-results --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
docker exec kafka kafka-topics --create --topic processed-reviews --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

echo Setup complete!
echo Kafka UI: http://localhost:9092
echo Spark Master UI: http://localhost:8080
echo Spark Worker UI: http://localhost:8081

echo To stop services, run: docker-compose down
pause
