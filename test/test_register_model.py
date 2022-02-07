import importlib
import os

import pytest


@pytest.mark.integration
class TestRegisterModel:

    @classmethod
    def setup_class(cls):
        os.environ["MLFLOW_TRACKING_URL"] = 'http://localhost:12000'
        os.environ["MLFLOW_S3_ENDPOINT_URL"] = 'http://localhost:9000'
        os.environ["AWS_ACCESS_KEY_ID"] = 'minio'
        os.environ["AWS_SECRET_ACCESS_KEY"] = 'minio123'
        os.environ["BUCKET_NAME"] = 'cd4ml-ml-flow-bucket'
        cls.pipeline_script = importlib.import_module("scripts.pipeline")
        cls.register_model_script = importlib.import_module("scripts.register_model")

    def test_pipeline_and_register_model(self):
        self.pipeline_script.main(['titanic', 'default', 'default', 'default', 'default'])
        self.register_model_script.main(['http://localhost:12000'])

