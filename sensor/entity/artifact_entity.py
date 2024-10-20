from dataclasses import dataclass

@dataclass # Decorator # if you want to store data then use this decorator. 
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str


"""
The DataIngestionArtifact class is a straightforward way to encapsulate the paths of training and testing datasets in a structured manner, 
making it easier to manage data artifacts in a machine learning workflow. 
Using data classes enhances code readability and reduces boilerplate code, allowing developers to focus on functionality.

"""