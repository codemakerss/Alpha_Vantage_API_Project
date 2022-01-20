import API_Data_Retrieves as api 
apikey = "YTK6VG8ZMVOB0Z0H"
alpah_vantage1 = api.StockTimeSeries(apikey)
alpah_vantage2 = api.FundamentalData(apikey)
#data = alpah_vantage1.GetWeeklyStockPrice("AAPL")
data = alpah_vantage2.GetListingDelistingStatus_Original()
print(data)
