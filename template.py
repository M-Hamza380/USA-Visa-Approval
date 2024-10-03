import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)d : %(message)s ]"
    )

Project_Name = "usa_visa"

list_of_files = [
    ".github/workflows",
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/components/__init__.py",
    f"src/{Project_Name}/components/01_data_ingestion.py",
    f"src/{Project_Name}/components/02_data_validation.py",
    f"src/{Project_Name}/components/03_data_transformation.py",
    f"src/{Project_Name}/components/04_feature_engineering.py",
    f"src/{Project_Name}/components/05_feature_selection.py",
    f"src/{Project_Name}/components/06_model_training.py",
    f"src/{Project_Name}/components/07_model_evaluation.py",
    f"src/{Project_Name}/components/08_model_tuning.py",
    f"src/{Project_Name}/components/09_model_pusher.py",
    f"src/{Project_Name}/configuration/__init__.py",
    f"src/{Project_Name}/constant/__init__.py",
    f"src/{Project_Name}/entity/__init__.py",
    f"src/{Project_Name}/entity/config_entity.py",
    f"src/{Project_Name}/entity/artifact_entity.py",
    f"src/{Project_Name}/pipeline/__init__.py",
    f"src/{Project_Name}/pipeline/training_pipeline.py",
    f"src/{Project_Name}/pipeline/predict_pipeline.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/utils/logger.py",
    f"src/{Project_Name}/utils/exception.py",
    f"src/{Project_Name}/utils/main_utils.py",
    "config/config.yaml",
    "config/model.yaml",
    "config/schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "requirements.txt",
    "notebook_experiments/01_eda.ipynb",
    "notebook_experiments/02_model.ipynb",
    "templates/index.html",
    "static/style.css",
    ".env"
]

for filename in list_of_files:
    filepath = Path(f"{filename}")
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
