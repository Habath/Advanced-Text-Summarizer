import os
from box.exception import BoxValueError
import yaml
from advanced_text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml(str): path to yaml file

    Raises:
         ValueError: if yaml is empty 
         
        
    Returns:
        ConfigBox: ConfigBox object
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """ creates a list of irectories

    Args:
        path_to_directories (list): list o path of directories
        ignore_log (bool, optional) : ignore if multiple dirs is to be created.
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("created directory at :{path}")




@ensure_annotations
def get_size(path: Path) ->str:
    """ get size in KB

    Args:
    path (Path) : path of the file


    Returns:
    str: size in KB

    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"