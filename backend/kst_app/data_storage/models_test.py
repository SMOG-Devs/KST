import unittest
import pickle
from .models import Measurement, add_measurements

class TestModels(unittest.TestCase):
    def add_measurements_test(self):
        with open('C:\\Users\\bartw\\OneDrive\\Pulpit\\KST\\backend\\kst_app\\data.pkl', 'rb') as port:
            data = pickle.load(port)

        list_of_measurments = []
        for key, value in data.items():
            for id, info in value.items():
                measurment = Measurement(info[0], info[1], info[2], 0, 0, 0, key, id)
                list_of_measurments.append(measurment)

        add_measurements(list_of_measurments)
