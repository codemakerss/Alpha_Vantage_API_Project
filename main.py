import API_Data_Retrieves as api 
apikey = "YTK6VG8ZMVOB0Z0H"
alpah_vantage = api.FundamentalData(apikey)
data = alpah_vantage.GetListingDelistingStatus_Original()
print(data)
