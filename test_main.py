from unittest import TestCase
from main import read_csv
import json
import os


class Test1(TestCase):
    def test_read_csv1(self):
        self.assertRaises(FileNotFoundError, read_csv, 'non_existing_file.txt')


class Test2(TestCase):
    def test_read_csv2(self):
        with self.assertRaises(TypeError) as exc:
            a = read_csv(r'test_files/test_0.docx')
        self.assertEqual(str(exc.exception), 'Allowed formats are: .txt, .csv')


class Test3(TestCase):
    def test_read_csv3(self):
        json_f = r'test_files/test_1_output.json'
        read_csv(r'test_files/test_1.txt', json_f)

        with open(json_f) as json_file:
            data = json.load(json_file)
            features = data['features'][0]
            geometry = features['geometry']
            coordinates = geometry['coordinates']

        self.assertListEqual(coordinates, [2, 6])

    def tearDown(self):
        os.remove('test_files/test_1_output.json')


class Test4(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.json_f = 'test_files/tmp.json'

    def test_read_csv4(self):
        read_csv('test_files/test_2.csv', self.json_f)

        with open(self.json_f) as json_file:
            data = json.load(json_file)
            features = data['features'][0]
            geometry = features['geometry']
            coordinates = geometry['coordinates']

        self.assertListEqual(coordinates, [2, 6])

    def tearDown(self):
        os.remove(self.json_f)
