import json
from typing import List

import pandas as pd
import requests

import exdelphi.data_model as data_model
from exdelphi.api_time import datetime_to_int, int_to_datetime

BASE_URL = "http://api.exdelphi.com"
HEADERS = {"Content-Type": "application/json", "Authorization": ""}


def authorize(username: str, password: str) -> None:
    """Sets headers to contain authorization token generated from given username and password"""
    response = requests.post(
        url=f"{BASE_URL}/token",
        data={"username": username, "password": password},
    )
    response_text = json.loads(response.text)
    if response.status_code == 200:
        token = response_text["access_token"]
        HEADERS["Authorization"] = f"Bearer {token}"
        print(f"Authenticated {username} at {BASE_URL}")
        return
    _raise_response_error(response)


def _raise_response_error(response):
    if response.status_code == 401:
        raise PermissionError("Incorrect username or password")
    elif response.status_code == 500:
        raise ConnectionError("Server error")
    else:
        raise RuntimeError(json.loads(response.text))


def get_product_list() -> List[data_model.Product]:
    """Returns list of all products available to authorized user"""
    response = requests.get(url=f"{BASE_URL}/products/", headers=HEADERS)
    response_text = json.loads(response.text)
    if response.status_code == 200:
        return [data_model.Product.parse_obj(item) for item in response_text]
    _raise_response_error(response)


def get_data_sets_for_product(product_id) -> List[data_model.Dataset]:
    """Returns list of datasets from given product available to authorized user"""
    response = requests.get(url=f"{BASE_URL}/data_sets/{product_id}", headers=HEADERS)
    response_text = json.loads(response.text)
    if response.status_code == 200:
        return [data_model.Dataset.parse_obj(item) for item in response_text]
    _raise_response_error(response)


def get_data(data_set_id: int) -> pd.DataFrame:
    """Returns data set with given ID to authorized user"""
    response = requests.get(url=f"{BASE_URL}/data/{data_set_id}", headers=HEADERS)
    response_text = json.loads(response.text)
    if response.status_code == 200:
        data = pd.DataFrame(response_text)
        data.set_index("t", inplace=True)
        return data
    _raise_response_error(response)


def convert_int_to_datetime(data: pd.DataFrame) -> pd.DataFrame:
    """Converts time column `t` from int representation to time stamps"""
    data.index = data.index.map(lambda t: int_to_datetime(t))
    return data


def convert_datetime_to_int(data: pd.DataFrame) -> pd.DataFrame:
    """Converts time column `t` from time stamps representation to int"""
    data["t"] = data["t"].map(lambda t: datetime_to_int(t))
    return data


def upload_data(product_id: int, start_time: int, data: pd.DataFrame) -> None:
    """ "Convert pandas DataFrame with columns 't' and 'v' to json and upload to database"""
    _prepare_time_column(data)
    data_as_json = data.to_json(orient="records")
    requests.put(
        url=f"{BASE_URL}/data/?product_id={product_id}&start_time={start_time}",
        headers=HEADERS,
        data=f"{data_as_json}",
    )


def _prepare_time_column(data):
    if data.index.name == "t":
        data["t"] = data.index
    if "t" not in data:
        raise ValueError("time t is missing in data")
    if "v" not in data:
        raise ValueError("value v is missing in data")
    try:
        data = convert_datetime_to_int(data)
    except AttributeError:
        pass
    if data["t"].dtype != int:
        raise ValueError("data['t'] must be of type int")
