from pathlib import Path
import unittest
import joblib
import numpy

from cd4ml.ml_model import MLModel


def load_titanic_model():
    return load_model("full_model_titanic.pkl")


def load_groceries_model():
    return load_model("full_model_groceries.pkl")


def load_model(name: str):
    path = Path(Path(__file__).parent, "resources", name)
    loaded_model = joblib.load(path)
    loaded_model.load_encoder_from_package()
    model: MLModel = loaded_model

    assert model is not None
    return model


class TestMLModel (unittest.TestCase):
    ROW_TITANIC = dict(age=2, sibsp=0, parch='0', fare='23232', pclass='1', sex='male', embarked='S', cabin='F2')
    ROW_GROCERIES = dict(date='20170114', item_nbr='1963838')

    def test_predict_single_processed_row(self):
        pred = load_titanic_model().predict_single_processed_row(self.ROW_TITANIC)
        assert pred == "1"

    def test_predict_prob_single_processed_row(self):
        prob = load_titanic_model().predict_prob_single_processed_row(self.ROW_TITANIC)
        numpy.testing.assert_array_equal(prob, [0.395, 0.605])

    def test_predict_and_describe_prob_single_processed_row(self):
        prob = load_titanic_model().predict_and_describe_prob_single_processed_row(self.ROW_TITANIC)
        assert prob == {'0': 0.395, '1': 0.605}

    def test_groceries_predict_single_processed_row(self):
        pred = load_groceries_model().predict_single_processed_row(self.ROW_GROCERIES)
        assert pred == 4.0

    def test_groceries_predict_prob_single_processed_row(self):
        self.assertRaises(NotImplementedError,
                          load_groceries_model().predict_prob_single_processed_row, self.ROW_GROCERIES)

    def test_groceries_predict_and_describe_prob_single_processed_row(self):
        self.assertRaises(NotImplementedError,
                          load_groceries_model().predict_and_describe_prob_single_processed_row, self.ROW_GROCERIES)
