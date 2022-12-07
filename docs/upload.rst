### Uploading Forecasts with the EXDELPHI Python Client

Uploading Forecasts with the EXDELPHI Python Client

The EXDELPHI Python client provides a convenient and easy-to-use way to upload forecasts to the EXDELPHI platform. This section of the documentation will provide a detailed overview of the upload_forecast() method, including its syntax, arguments, and usage examples.

Syntax

The upload_forecast() method has the following syntax:

Copy code
upload_forecast(file, metadata=None, price=None, validate=True)
Arguments

The upload_forecast() method takes the following arguments:

file: The forecast file to be uploaded to the EXDELPHI platform. This should be a file-like object containing the forecast data in a supported format (such as CSV or JSON).
metadata (optional): A dictionary of metadata associated with the forecast. This can include information such as the forecast horizon, the forecasting method used, and any relevant contextual information.
price (optional): The price of the forecast. This should be a numeric value (in the currency specified in the user's account settings) representing the amount that the forecast should be sold for. If not provided, the forecast will be made available for free.
validate (optional): A boolean value indicating whether the forecast should be validated before being uploaded. If True (the default), the forecast will be validated to ensure that it is in a supported format and contains the required data. If False, the forecast will be uploaded without validation.


The EXDELPHI Python client provides a convenient and easy-to-use way to upload forecasts to the EXDELPHI platform. This section of the documentation will provide a detailed overview of the upload_forecast() method, including its syntax, arguments, and usage examples.

The upload_forecast() method of the EXDELPHI Python client allows you to upload a forecast to the EXDELPHI platform. This method accepts a number of parameters that specify the details of the forecast that you are uploading, including the forecast data, the forecast horizon, and any relevant metadata.

To upload a forecast using the upload_forecast() method, you will need to provide the following parameters:

forecast_data: This parameter should be set to the data for the forecast that you are uploading. The data should be provided as a Pandas DataFrame, with the columns of the DataFrame representing the different variables or dimensions of the forecast, and the rows representing the different time periods or points in the forecast horizon.
forecast_horizon: This parameter specifies the time period or horizon over which the forecast data applies. The forecast horizon should be provided as a Pandas DateOffset object, which specifies the length of time (e.g. 1 day, 1 week, 1 month) and the starting point of the forecast horizon.
metadata: This parameter allows you to provide additional metadata about the forecast that you are uploading. The metadata should be provided as a dictionary,



