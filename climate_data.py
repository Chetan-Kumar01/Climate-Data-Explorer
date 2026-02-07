from api_client import AntigravityClient

class ClimateDataManager:
    def __init__(self, api_key):
        self.client = AntigravityClient(api_key)
        
    def get_data(self, region, data_type, start_date, end_date):
        """
        Orchestrates fetching data from the API.
        """
        # In a real app, this might handle caching or merging multiple sources
        return self.client.fetch_climate_data(region, data_type, start_date, end_date)
