import unittest
from scaledown import Scaledown
from analysis import ClimateAnalyzer
from api_client import AntigravityClient

class TestEnvironmentalTool(unittest.TestCase):
    def test_scaledown_compression(self):
        # Create dummy data
        data = [{'day': i, 'value': 10 + (i%2)} for i in range(20)]
        
        # Compress by factor of 5
        compressor = Scaledown(compression_factor=5)
        compressed = compressor.compress(data)
        
        # Expect 4 chunks (20 / 5)
        self.assertEqual(len(compressed), 4)
        
        # Check first chunk average (10, 11, 10, 11, 10) -> 10.4
        self.assertAlmostEqual(compressed[0]['value'], 10.4)
        
    def test_trend_analysis(self):
        analyzer = ClimateAnalyzer()
        
        # Increasing data
        data_inc = [{'day': i, 'value': i} for i in range(10)]
        self.assertEqual(analyzer.analyze_trend(data_inc), "Increasing")
        
        # Decreasing data
        data_dec = [{'day': i, 'value': 10-i} for i in range(10)]
        self.assertEqual(analyzer.analyze_trend(data_dec), "Decreasing")
        
    def test_api_client_init(self):
        # Should fail without key
        with self.assertRaises(ValueError):
            AntigravityClient("")
        
        # Should succeed with key
        client = AntigravityClient("dummy_key")
        self.assertEqual(client.api_key, "dummy_key")

if __name__ == '__main__':
    unittest.main()
