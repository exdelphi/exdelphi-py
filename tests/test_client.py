import json
import unittest
from unittest.mock import patch
from datetime import datetime

import pandas as pd
import requests

from exdelphi.client import (
    HEADERS,
    authorize,
    get_data,
    get_product_list,
    convert_int_to_datetime,
)
from exdelphi.data_model import Product


class TestClient(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame with integer timestamps
        self.data = pd.DataFrame({"v": [10, 20, 30]}, index=[0, 1, 2])
        self.data.index.name = "t"

    @patch("requests.post")
    def test_authorize_success(self, mock_post):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps({"access_token": "12345"}).encode("utf-8")
        mock_post.return_value = mock_response
        authorize("test_user", "test_password")
        mock_post.assert_called_with(
            url="http://api.exdelphi.com/token",
            data={"username": "test_user", "password": "test_password"},
        )
        self.assertEqual(HEADERS["Authorization"], "Bearer 12345")

    @patch("requests.post")
    def test_authorize_failure(self, mock_post):
        mock_response = requests.Response()
        mock_response.status_code = 401
        mock_response._content = json.dumps(
            {"detail": "Incorrect username or password"}
        ).encode("utf-8")
        mock_post.return_value = mock_response
        with self.assertRaises(PermissionError) as error:
            authorize("test_user", "test_password")
        self.assertEqual(str(error.exception), "Incorrect username or password")

    @patch("requests.get")
    def test_get_product_list_success(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps(
            [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]
        ).encode("utf-8")
        mock_get.return_value = mock_response
        products = get_product_list()
        self.assertEqual(len(products), 2)
        self.assertIsInstance(products[0], Product)
        self.assertEqual(products[0].id, 1)
        self.assertEqual(products[0].name, "Product 1")
        self.assertEqual(products[1].id, 2)
        self.assertEqual(products[1].name, "Product 2")

    @patch("requests.get")
    def test_get_product_list_unauthorized(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 401
        mock_response._content = json.dumps(
            {"detail": "Incorrect username or password"}
        ).encode("utf-8")
        mock_get.return_value = mock_response
        with self.assertRaises(PermissionError) as context:
            get_product_list()
        self.assertEqual(str(context.exception), "Incorrect username or password")

    @patch("requests.get")
    def test_get_data(self, mock_get):
        # Create a mock response object with a 200 status code
        # and a pre-defined response text
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps(
            [{"t": 0, "v": 10}, {"t": 1, "v": 20}, {"t": 2, "v": 30}]
        ).encode("utf-8")
        mock_get.return_value = mock_response
        result = get_data(1)
        pd.testing.assert_frame_equal(result, self.data)

    @patch("requests.get")
    def test_no_connection_error(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 500
        mock_response._content = json.dumps({"detail": "Server Error"}).encode("utf-8")
        mock_get.return_value = mock_response
        with self.assertRaises(ConnectionError):
            get_data(1)
        with self.assertRaises(ConnectionError):
            get_product_list()

    def test_convert_int_to_datetime(self):
        data = convert_int_to_datetime(self.data)
        self.assertEqual(data.index.dtype, "datetime64[ns, UTC]")
        self.assertListEqual(data.values.T.tolist()[0], [10, 20, 30])
        self.assertEqual(
            data.index[0], pd.Timestamp(year=1970, month=1, day=1, tz="UTC")
        )
        self.assertEqual(
            data.index[1], pd.Timestamp(year=1970, month=1, day=1, second=1, tz="UTC")
        )
        self.assertEqual(
            data.index[2], pd.Timestamp(year=1970, month=1, day=1, second=2, tz="UTC")
        )
