import unittest
import numpy as np
from kst_app.engine.model_architecture import create_clean_model_hour
from kst_app import app


class ModelTest(unittest.TestCase):
    def test_learning_const(self):
        data = np.ones((200,24,150))
        target = np.ones((200,150))
        weather = np.ones((200,24,10))

        model = create_clean_model_hour()
        model.fit([data[:160],weather[:160]],target[:160], epochs=4)

        _, metrics = model.evaluate([data[160:],weather[160:]],target[160:])
        self.assertGreater(1,metrics,'Not good enough const')

    def test_learning_linear(self):
        data = np.zeros((200,24,150))
        target = np.zeros((200,150))
        weather = np.ones((200,24,10))

        for i in range(200):
            data[i] = np.ones((24,150)) * i
            target[i] = i
            weather[i] = np.ones((24,10)) * i

        model = create_clean_model_hour()
        model.fit([data[:160], weather[:160]], target[:160], epochs=4)

        _, metrics = model.evaluate([data[160:], weather[160:]], target[160:])
        self.assertGreater(1, metrics, 'Not good enough linear')
