import argparse
import sys
from climate_data import ClimateDataManager
from scaledown import Scaledown
from analysis import ClimateAnalyzer

# API Key provided by user
API_KEY = "JxaDlyPA2R2nGwTpevwjM2qKDYU5PqJ68mjr0TW2"

def main():
    parser = argparse.ArgumentParser(description="Environmental Research Tool")
    parser.add_argument("--region", type=str, required=True, help="Region to analyze (e.g., Arctic, Amazon)")
    parser.add_argument("--type", type=str, required=True, choices=['Temperature', 'Rainfall', 'CO2', 'Sea Level'], help="Data type")
    parser.add_argument("--start", type=str, default="2023-01-01", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default="2023-12-31", help="End date (YYYY-MM-DD)")
    parser.add_argument("--compress", action="store_true", help="Use Scaledown compression")
    
    args = parser.parse_args()
    
    print(f"--- Initializing Environmental Research Tool for {args.region} ---")
    
    # 1. Pipeline: Ingest Data
    manager = ClimateDataManager(API_KEY)
    raw_data = manager.get_data(args.region, args.type, args.start, args.end)
    print(f"Fetched {len(raw_data)} raw data points.")
    
    processed_data = raw_data
    
    # 2. Compress if requested
    if args.compress:
        print("Applying Scaledown compression...")
        compressor = Scaledown(compression_factor=10)
        processed_data = compressor.compress(raw_data)
        print(f"Compressed to {len(processed_data)} data points.")
    
    # 3. Analyze
    analyzer = ClimateAnalyzer()
    trend = analyzer.analyze_trend(processed_data)
    prediction = analyzer.predict_next(processed_data)
    
    print("\n--- Analysis Results ---")
    print(f"Trend: {trend}")
    print(f"Prediction (next 30 days estimate): {prediction:.2f}")
    
    if args.compress:
        print("\n(Note: Analysis performed on compressed data)")

if __name__ == "__main__":
    main()
