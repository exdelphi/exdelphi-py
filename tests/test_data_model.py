import unittest

import pydantic

from exdelphi.data_model import Data
from pydantic import BaseModel


class TestDataClass(unittest.TestCase):
    def test_data_class(self):
        data = Data(t=1.0, v=0.5)
        self.assertEqual(data.t, 1)
        self.assertEqual(data.v, 0.5)
        self.assertIsInstance(data.t, int)
        self.assertIsInstance(data.v, float)
        self.assertTrue(issubclass(Data, BaseModel))
        self.assertTrue(isinstance(data, BaseModel))

    def test_invalid_data_class(self):
        with self.assertRaises(pydantic.ValidationError):
            data = Data(t="etc", v=0.5)
