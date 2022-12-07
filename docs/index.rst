

Welcome to EXDELPHI Python client documentation!
=================================


The EXDELPHI Python client is a Python library that allows you to easily interact with the EXDELPHI platform and access its features and functionality. With the Python client, you can upload and download forecasts, evaluate the quality of forecasts, and manage your user account and settings.

To get started with the Python client, you will need to install the library using pip:

```
pip install exdelphi-client
```

Once the library is installed, you can import it into your Python code and initialize the client by providing your EXDELPHI API key:

```
from exdelphi import client
client = Client(api_key="YOUR_API_KEY")
```


From there, you can use the various methods provided by the client to access the different features of the EXDELPHI platform. For example, you can use the `upload()` method to upload a forecast to the platform, and the `download()` method to download a forecast from the platform. You can also use the `get_forecast_quality()` method to evaluate the quality of a forecast, and the `get_user_settings()` method to access and manage your user account settings.

For more detailed information about the methods and functionality provided by the EXDELPHI Python client, please refer to the rest of the documentation. We hope you find the Python client to be a useful and convenient tool for working with the EXDELPHI platform!

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


