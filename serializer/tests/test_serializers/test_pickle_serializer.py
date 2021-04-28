import unittest
from os import path, curdir

from serializer.serializers.pickle_serializer import PickleSerializer
from test_data import data, get_answer_files, get_test_files


class PickleSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_pickle_ser = PickleSerializer()
        self.path_dir = path.join(
                    path.abspath(curdir),
                    'test_answers',
                    'test_pickle'
                    )
        self.data = data
        self.answer_files = get_answer_files('pickle')
        self.pickle_files = get_test_files('pickle')

    def test_dump(self):
        for value, test_pickle in zip(
                                    self.data,
                                    self.pickle_files):
            self.test_pickle_ser.dump(
                value, path.join(self.path_dir, test_pickle))
            self.assertIsNotNone(
                path.getsize(path.join(self.path_dir, test_pickle))
            )

        self.assertIsNone(
            self.test_pickle_ser.dump(None, self.data[:-1])
        )

    def test_dumps(self):
        for value, test_pickle in zip(self.data[:-4],
                                      self.pickle_files[:-4]):
            with open(path.join(
                    self.path_dir, test_pickle), 'rb') as rf:
                answer = rf.read()
            self.assertEqual(
                self.test_pickle_ser.dumps(value), answer
            )
        self.assertIsNone(
            self.test_pickle_ser.dump(self.data[:-1], self.data[:-1])
        )

    def test_load(self):
        for value, test_pickle in zip(self.data[:-4],
                                    self.pickle_files[:-4]):
            self.assertEqual(self.test_pickle_ser.load(
                    path.join(self.path_dir, test_pickle)), value)
        func = self.test_pickle_ser.load(path.join(
            self.path_dir, self.pickle_files[4]),
            convert=True)
        self.assertEqual(type(func), dict)
        simple_class = self.test_pickle_ser.load(path.join(
                    self.path_dir, self.pickle_files[5]))
        self.assertEqual(type(simple_class), type)
        complex_class = self.test_pickle_ser.load(path.join(
                    self.path_dir, self.pickle_files[6]))
        self.assertTrue(hasattr(complex_class, 'func_in_class'))
        complex_object = self.test_pickle_ser.load(path.join(
                    self.path_dir, self.pickle_files[7]))
        self.assertEqual(complex_object.other.string, 'string')
        self.assertIsNone(self.test_pickle_ser.load('incorrect_path'))

    def test_loads(self):
        for value, test_pickle in zip(self.data[:-4],
                                      self.pickle_files[:-4]):
            with open(path.join(
                    self.path_dir,
                    test_pickle), 'rb') as rf:
                data_ = rf.read()
            self.assertEqual(
                self.test_pickle_ser.loads(data_), value
                    )

        def get_data():
            for data_file in self.pickle_files[4:]:
                with open(path.join(
                        self.path_dir,
                        data_file), 'rb') as rf:
                    data_ = rf.read()
                yield data_

        data_ = get_data()
        func = self.test_pickle_ser.loads(next(data_))
        self.assertEqual(func(12), 101)
        simple_class = self.test_pickle_ser.loads(next(data_))
        self.assertEqual(type(simple_class), type)
        complex_class = self.test_pickle_ser.loads(next(data_))
        self.assertTrue(hasattr(complex_class, 'func_in_class'))
        complex_object = self.test_pickle_ser.loads(next(data_))
        self.assertEqual(complex_object.other.string, 'string')
        self.assertIsNone(self.test_pickle_ser.loads('bad_data'))


if __name__ == "__main__":
    unittest.main()
