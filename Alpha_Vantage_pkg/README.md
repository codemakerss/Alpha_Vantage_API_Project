# Alpha_Vantage_API Financial Data 

Alpha_Vantage_API is a package for collecting stocks price and 
their related information.

https://img.shields.io/badge/python-v3.6-brightgreen

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Alpha_Vantage_API.

```bash
pip install Alpha_Vantage_API
```

## Example

```python
from Alpha_Vantage_API import API_Data_Retrieve

# returns stock daily result 
StockTimeSeries = API_Data_Retrieve.StockTimeSeries(apikey)
daily_data = StockTimeSeries.GetDailyStockPrice("IBM")
print(daily_data)

# returns company information
FundamentalData = API_Data_Retrieve.FundamentalData(apikey)
stock_company_info = FundamentalData.CompanyInfo("AAPL)
print(stock_company_info)
```

Go to [Alpha_Vantage_API_Project Issues Page](https://github.com/codemakerss/Alpha_Vantage_API_Project/issues) to report any issues.

## License
[MIT](https://choosealicense.com/licenses/mit/)