import random
import time

class AntigravityClient:
    def __init__(self, api_key):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("API Key is required")
        print(f"Antigravity API initialized with key: {self.api_key[:5]}...")

    def fetch_climate_data(self, region, data_type, start_date, end_date):
        """
        Simulates fetching large climate datasets.
        Returns a list of data points.
        """
        print(f"Fetching {data_type} for {region} from {start_date} to {end_date} via Antigravity API...")
        # Simulate network latency
        time.sleep(0.5) 
        
        # Mock data generation based on type
        days = 365 # Mocking a year's worth of data for simplicity in this step
        data = []
        
        base_val = 0
        if data_type.lower() == 'temperature':
            base_val = 15 # Celsius
        elif data_type.lower() == 'rainfall':
            base_val = 5 # mm
        elif data_type.lower() == 'co2':
            base_val = 400 # ppm
        elif data_type.lower() == 'sea_level':
            base_val = 0 # mm change
            
        for i in range(days):
            val = base_val + random.uniform(-5, 5)
            # Add some trend
            val += (i / days) * 2 
            data.append({"day": i, "value": val})
            
        return data

    def upload_data(self, data):
        """
        Simulates uploading processed data back to potential cloud storage.
        """
        print(f"Uploading {len(data)} records to Antigravity Cloud...")
        time.sleep(0.2)
        return True
