import unittest
import requests
import json
from unittest.mock import patch

from exdelphi.client import authorize, HEADERS


class TestAuthorize(unittest.TestCase):
    @patch("requests.post")
    def test_authorize_success(self, mock_post):
        # Set up mock response for the `requests.post` call
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps({"access_token": "12345"}).encode("utf-8")
        mock_post.return_value = mock_response

        # Call the `authorize` function with the mock `requests.post`
        authorize("test_user", "test_password")

        # Verify that the `requests.post` function was called with the correct URL and data
        mock_post.assert_called_with(
            url="http://api.exdelphi.com/token",
            data={"username": "test_user", "password": "test_password"},
        )

        # Verify that the `HEADERS` dictionary contains the authorization token
        self.assertEqual(HEADERS["Authorization"], "Bearer 12345")

    @patch("requests.post")
    def test_authorize_failure(self, mock_post):
        # Set up mock response for the `requests.post` call
        mock_response = requests.Response()
        mock_response.status_code = 401
        mock_response._content = json.dumps(
            {"detail": "Incorrect username or password"}
        ).encode("utf-8")
        mock_post.return_value = mock_response

        # Call the `authorize` function with the mock `requests.post`
        with self.assertRaises(PermissionError) as error:
            authorize("test_user", "test_password")

        # Verify that the correct error message is raised
        self.assertEqual(
            str(error.exception), "Incorrect username or password"
        )
