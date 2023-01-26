import unittest
from kst_app.data_storage.models import get_all_predicted_measurements
from kst_app.engine.predictor import predict_12h, _predict_for_test
from kst_app import app
import time


class TestPredictior(unittest.TestCase):
    def test_prediction_12h(self):
        with app.app_context():
            predict_12h()
            measurements = get_all_predicted_measurements()
            print(measurements)
            self.assertEqual(12*50, len(measurements))

    def test_preds(self):
        with app.app_context():
            self.assertEqual(12 * 50, len(get_all_predicted_measurements()))

    def test_prediction_on_data(self):
        with app.app_context():
            out = _predict_for_test(100)
