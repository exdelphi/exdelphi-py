import unittest

import pydantic
from pydantic import BaseModel

from exdelphi.data_model import Data, Dataset, Product, Token, User


class TestDataClass(unittest.TestCase):
    def test_valid_data(self):
        data = Data(t=1.0, v=0.5)
        self.assertEqual(data.t, 1)
        self.assertEqual(data.v, 0.5)
        self.assertIsInstance(data.t, int)
        self.assertIsInstance(data.v, float)
        self.assertTrue(issubclass(Data, BaseModel))
        self.assertTrue(isinstance(data, BaseModel))

    def test_invalid_data_raises_ValidationError(self):
        with self.assertRaises(pydantic.ValidationError):
            data = Data(t="etc", v=0.5)


class TestUserClass(unittest.TestCase):
    def test_valid_user(self):
        user = User(id=1.0)
        self.assertEqual(user.id, 1)
        self.assertIsInstance(user.id, int)

    def test_invalid_user_raises_ValidationError(self):
        with self.assertRaises(pydantic.ValidationError):
            user = User(id="etc")


class TestTokenClass(unittest.TestCase):
    def test_valid_token(self):
        token = Token(access_token="str0", token_type="str1")
        self.assertEqual(token.access_token, "str0")
        self.assertEqual(token.token_type, "str1")
        self.assertIsInstance(token.access_token, str)
        self.assertIsInstance(token.token_type, str)

    def test_invalid_token_raises_ValidationError(self):
        with self.assertRaises(pydantic.ValidationError):
            token = Token(id="etc")
        with self.assertRaises(pydantic.ValidationError):
            token = Token(access_token=None, token_type="etc")


class TestProductClass(unittest.TestCase):
    def test_valid_product(self):
        product = Product(id=0, name="etc")
        self.assertEqual(product.id, 0)
        self.assertEqual(product.name, "etc")
        self.assertIsInstance(product.id, int)
        self.assertIsInstance(product.name, str)

    def test_invalid_product_raises_ValidationError(self):
        with self.assertRaises(pydantic.ValidationError):
            product = Product(id=0)
        with self.assertRaises(pydantic.ValidationError):
            product = Product(id=None, name="etc")


class TestDatasetClass(unittest.TestCase):
    def test_valid_dataset(self):
        dataset = Dataset(id=0, start_time=1)
        self.assertEqual(dataset.id, 0)
        self.assertEqual(dataset.start_time, 1)
        self.assertIsInstance(dataset.id, int)
        self.assertIsInstance(dataset.start_time, int)

    def test_invalid_dataset_raises_ValidationError(self):
        with self.assertRaises(pydantic.ValidationError):
            dataset = Dataset(start_time=0)
        with self.assertRaises(pydantic.ValidationError):
            dataset = Dataset(id=None, name="etc")
