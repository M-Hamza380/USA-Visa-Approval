import os, sys
import dill, yaml
import numpy as np
import pandas as pd

from src.usa_visa.utils.exception import USAVISAException
from src.usa_visa.utils.logger import logger

def read_yaml_file(file_path: str) -> dict:
    try:
        logger.info(f"Reading yaml file: [{file_path}].")
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        logger.info(f"Yaml file: [{file_path}] loaded successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        logger.info(f"Creating yaml file: [{file_path}].")
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file, allow_unicode=True)
        logger.info(f"Yaml file: [{file_path}] created successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def load_object(file_path: str) -> object:
    try:
        logger.info(f"Loading object file: [{file_path}].")
        if not os.path.exists(file_path):
            raise Exception(f"The file: [{file_path}] does not exist.")
        with open(file_path, "rb") as file:
            return dill.load(file)
        logger.info(f"Object file: [{file_path}] loaded successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    try:
        logger.info(f"Saving object: [{file_path}]")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logger.info(f"Object: [{file_path}] saved successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    try:
        logger.info(f"Saving numpy array data: [{file_path}]")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
        logger.info(f"Numpy array data: [{file_path}] saved successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def load_numpy_array_data(file_path: str) -> np.array:
    try:
        logger.info(f"Loading numpy array data: [{file_path}]")
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
        logger.info(f"Numpy array data: [{file_path}] loaded successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def save_dataframe(dataframe: pd.DataFrame, file_path: str) -> None:
    try:
        logger.info(f"Saving dataframe: [{file_path}]")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        dataframe.to_csv(file_path)
        logger.info(f"Dataframe: [{file_path}] saved successfully.")
    except Exception as e:
        raise USAVISAException(e, sys)

def drop_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    try:
        logger.info(f"Dropping columns: [{columns}] from dataframe: [{dataframe}]")
        dataframe.drop(columns, axis=1, inplace=True)
        logger.info(f"Columns: [{columns}] dropped from dataframe: [{dataframe}]")
        return dataframe
    except Exception as e:
        raise USAVISAException(e, sys)

