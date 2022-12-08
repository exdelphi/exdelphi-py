import json
import unittest
from unittest.mock import patch

import requests

from exdelphi.client import HEADERS, authorize, get_product_list
from exdelphi.data_model import Product


class TestClient(unittest.TestCase):
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
    def test_get_product_list_server_error(self, mock_get):
        mock_response = requests.Response()
        mock_response.status_code = 500
        mock_response._content = json.dumps({"detail": "Server Error"}).encode("utf-8")
        mock_get.return_value = mock_response
        with self.assertRaises(ConnectionError) as context:
            get_product_list()
        self.assertEqual(str(context.exception), "Server error")
