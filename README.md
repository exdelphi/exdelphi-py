# EXDELPHI Python Client

[![PyPI version](https://img.shields.io/pypi/v/exdelphi.svg)](https://pypi.python.org/pypi/exdelphi)
[![build](https://github.com/exdelphi/exdelphi-py/actions/workflows/example.yml/badge.svg)](https://github.com/exdelphi/exdelphi-py/actions/workflows/example.yml)
[![License](https://img.shields.io/pypi/l/exdelphi.svg)](LICENSE)
[![codecov](https://codecov.io/gh/exdelphi/exdelphi-py/branch/master/graph/badge.svg)](https://codecov.io/gh/exdelphi/exdelphi-py)

The EXDELPHI Python client allows users to interact with the [EXDELPHI](https://www.exdelphi.com/) 
platform from their Python scripts. With this client, users can upload and download forecasts, 
compare the accuracy of forecasts, and access quality measures of all forecasts on the platform.

Installation

To install the EXDELPHI Python client, run the following command:

```
pip install exdelphi
```

## Usage

To use the EXDELPHI Python client, import it in your Python script and create a client instance with your API key:

```
from exdelphi import Client
client = Client(api_key="YOUR_API_KEY")
```

Then, use the client instance to access the various methods available on the EXDELPHI platform:

```
# Upload a forecast
client.upload_forecast(forecast_data)

# Download a forecast
forecast = client.download_forecast(forecast_id)

# Compare the accuracy of two forecasts
accuracy = client.compare_forecasts(forecast_id1, forecast_id2)

# Access quality measures of all forecasts on the platform
quality_measures = client.get_quality_measures()
```


For detailed usage instructions and examples, see the 
[EXDELPHI Python client documentation](https://exdelphi.readthedocs.io/en/latest/).


## Credits

exdelphi, 2022
