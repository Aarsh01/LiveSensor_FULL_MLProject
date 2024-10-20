# In requirement.txt :
    # # -r why? beacuse it will read the file .txt one by one and install them.... 
    # pandas
    # numpy 
    # scikit-learn
    # python-dotenv
    # -e .
    # # to make the code readibility and if anyone else want to use the code he/she can.. # editable mode
    # # why? generally setup.py file is run then req.txt is run , So no to do again and again for running the setup.py file we add -e . at the last in req.txt, which triggers the setup.py file at the end and run the find_package() method.

    """
    pymongo[srv]==4.2.0
    pandas
    numpy
    scikit-learn
    pymongo
    # python-dotenv

    # -e .   #editable mode 
*********************************************************************************************************
# In main.py & sensor.exception:

    from sensor.exception import SensorException
    import sys

    def test_exception():
        try:
            a=1/0
        except Exception as e:
            raise SensorException(e,sys)

    if __name__=='__main__':
        try:
            test_exception()
        except Exception as e:
            print(e)

    Output: 
    PS D:\Bakchodi\LiveSensor> & C:/Users/aarsh/AppData/Local/Programs/Python/Python312/python.exe d:/Bakchodi/LiveSensor/LiveSensor_FULL_MLProject/main.py
    for reading the .env file
    Error occured and the file name is [d:\Bakchodi\LiveSensor\LiveSensor_FULL_MLProject\main.py] and the lineNumber is [6] and error is [division by zero]

********************************************************************************************************************************************

# In main.py & logger.py

    from sensor.exception import SensorException
    import sys
    from sensor.logger import logging

    def test_exception():
        try:
            logging.info("Error present!") # No uppercase of info
            a=1/0
        except Exception as e:
            raise SensorException(e,sys)

    if __name__=='__main__':
        try:
            test_exception()
        except Exception as e:
            print(e)

Output: 
logs folder is build.
In terminal:
PS D:\Bakchodi\LiveSensor> & C:/Users/aarsh/AppData/Local/Programs/Python/Python312/python.exe d:/Bakchodi/LiveSensor/LiveSensor_FULL_MLProject/main.py
for reading the .env file
Error occured and the file name is [d:\Bakchodi\LiveSensor\LiveSensor_FULL_MLProject\main.py] and the lineNumber is [8] and error is [division by zero]


********************************************************************************************************************************************

# why .env file:
1. Security: Protects sensitive data (like passwords and API keys) from being exposed in version control.
2. Configuration: Centralizes and simplifies managing environment-specific settings.
3. Portability: Facilitates easy replication and sharing of configurations across different systems.
4. Flexibility: Allows dynamic configuration changes without altering the code.
5. Ease of Use: Provides straightforward integration with code via libraries like python-dotenv .

********************************************************************************************************************************************

# How we can load our dataset into mongoDB server :

### MongoDB pe kya karna hai:
1. make project in mongoDB
2. make cluster0 
3. give permissions to the yourself bu making yourself user 

### Coming to vs code file:
1. make .env file paste the mongoDB connection url with the name of "MONGO_DB_URL"
2. to have the access of the file install "load_dotenv" library and write code in __init__.py file in sensor folder 
3. Build 2 python file in sensor i.e "config.py" and "utils.py"
4. a. In config file:/n
      - a.1. The code is designed to encapsulate the retrieval of a MongoDB connection URL from an environment variable,
      - a.2. Establish a connection to a MongoDB database using that URL.
   b. In utils file:
      b.1 It define a function, which help us to load the dataset into the mongoDB cluster. 
5. After that import them in main.py 
6. Provide the database name, collection name, dataset location path and just run
7. After running the main.py file dataset it loaded into the mongoDB cluster server

********************************************************************************************************************************************
# Sensor Fault Detection High Level Code Flow
### Start:
1. Build all folders in sensor folder i.e (cload_storage, components, configuration, constant, data_access, entity, pipeline).
2. Make them package by building "__init__.py" file i each folder. 

### Step - 1: Data Ingestion
    - Decide the variables in "sensor.constant.training_pipeline.__init__.py" 
    - Do the coding stuff in 2 files i.e "config_entity.py" and then "artifact_entity.py".

    - In config_entity.py file: class name "DataIngestionConfig"
        a. set the path from artifacts to train.csv, test.csv, sensor.csv datasets. It is well explained there. 

    - In artifact_entity.py: class name "DataIngestionArtifact"
        a. Straightforward way to encapsulate the paths of training and testing datasets in a structured manner.
    
    - Now coming to sensor.configuration.mongodb_db_connection :

    - Now coming to sensor.data_access.sensor_data :

    - Now coming to sensor.component.data_ingestion.py :


