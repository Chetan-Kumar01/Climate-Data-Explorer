import statistics

class ClimateAnalyzer:
    def analyze_trend(self, data):
        """
        Analyzes the trend of the data (Increasing, Decreasing, Stable).
        Simple linear slope estimation.
        """
        if not data:
            return "No Data"
        
        # Extract values
        values = [d['value'] for d in data]
        n = len(values)
        if n < 2:
            return "Stable"
            
        # Simple slope calculation (end - start) / n
        slope = (values[-1] - values[0]) / n
        
        if slope > 0.05:
            return "Increasing"
        elif slope < -0.05:
            return "Decreasing"
        else:
            return "Stable"

    def predict_next(self, data, horizon_days=30):
        """
        Predicts the value after horizon_days based on current trend.
        """
        if not data:
            return 0.0
            
        values = [d['value'] for d in data]
        avg = statistics.mean(values)
        
        # Simple trend application
        trend = self.analyze_trend(data)
        factor = 0
        if trend == "Increasing":
            factor = 0.1
        elif trend == "Decreasing":
            factor = -0.1
            
        # Current last value + (trend_factor * days)
        last_val = values[-1]
        prediction = last_val + (factor * horizon_days)
        return prediction


def analyze_data(data):
    analyzer = ClimateAnalyzer()
    trend = analyzer.analyze_trend(data)
    prediction = analyzer.predict_next(data)

    return {
        "trend": trend,
        "prediction_next_30_days": round(prediction, 2)
    }
