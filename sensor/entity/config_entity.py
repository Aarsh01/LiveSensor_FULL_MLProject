from datetime import datetime
import os
from sensor.constant import training_pipeline


# This class is made to build the folder(1, 2, 3) on different timestamp after the artifact folder is builded....
class TrainingPipelineConfig:

    def __init__(self,timestamp:datetime.now()):
      timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")

      self.pipeline_name = training_pipeline.PIPELINE_NAME # This is a pipeline, so name it, according to below fig.
      self.artifact_dir = os.path.join( training_pipeline.ARTIFACT_DIR, timestamp) # timestamp folder is in artifacts diratory 
      # According to below fig, (a to b) or (b in a) is build

# Example: If training_pipeline.ARTIFACT_DIR is /path/to/artifacts and timestamp is 10_20_2024_15_30_00, 
# then self.artifact_dir would be /path/to/artifacts/10_20_2024_15_30_00.

############ Hence till b-part has build!. ######################

      self.timestamp:str = timestamp


"""
There are 6 parts ...............

                        From fig-0 from flowcharts: Ist Part 
MongoDB Database + Data Ingestion Config ---> Data Ingestion Component -----> Data Ingestion Artifacts
"""


"""
        artifacts (a)
            |
            |              
            v                     
        timestampt (b)-------------- --------------------------|
            |                       |                          |
            |                       |                          |
            v   (1)                 v    (2)                   v  (3)
        DATA INGESTION         DATA VALIDATION           DATA TRANSFORMATION                                           
            |       |                                                          
            |       |-----------|                                                          
            v                   |                                                
        ingested_data-----|     |------> Feature Store  
            |             |                 |
            |             |                 |
            v             v                 v
        train.csv      test.csv          sensor.csv  <--------------- MogoDb

"""


# # ***************** 1 **********************

class DataIngestionConfig: 
       
        # Basically We are setting the path of the folders according to the above fig provided.
        # Take the help of the above fig and variables from 'training_pipeline' from sensor.training_pipeline.py

        def __init__(self,training_pipeline_config:TrainingPipelineConfig):

            self.data_ingestion_dir: str = os.path.join(
                training_pipeline_config.artifact_dir, 
                training_pipeline.DATA_INGESTION_DIR_NAME
            )
            # Example: If artifact_dir is /path/to/artifacts/10_20_2024_15_30_00 and DATA_INGESTION_DIR_NAME is data_ingestion, 
            # then self.data_ingestion_dir would be /path/to/artifacts/10_20_2024_15_30_00/data_ingestion.

            ######## Hence (b to 1) or (1 in b) is done! ########

            self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, 
                training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, 
                training_pipeline.FILE_NAME
            )
            # Example: If data_ingestion_dir is /path/to/artifacts/10_20_2024_15_30_00/data_ingestion, 
            # DATA_INGESTION_FEATURE_STORE_DIR is feature_store, 
            # and FILE_NAME is features.csv, 
            # then self.feature_store_file_path would be /path/to/artifacts/10_20_2024_15_30_00/data_ingestion/feature_store/features.csv.



            self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, 
                training_pipeline.DATA_INGESTION_INGESTED_DIR, 
                training_pipeline.TRAIN_FILE_NAME
            )

            self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, 
                training_pipeline.DATA_INGESTION_INGESTED_DIR, 
                training_pipeline.TEST_FILE_NAME
            )
            #Example: If DATA_INGESTION_INGESTED_DIR is ingested_data, 
            # TRAIN_FILE_NAME is train.csv, and TEST_FILE_NAME is test.csv, then:
            # self.training_file_path would be /path/to/artifacts/10_20_2024_15_30_00/data_ingestion/ingested_data/train.csv.
            # self.testing_file_path would be /path/to/artifacts/10_20_2024_15_30_00/data_ingestion/ingested_data/test.csv.
            

            self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
            self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME




    


    
   
   



