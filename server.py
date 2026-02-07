from flask import Flask, request, jsonify
from flask_cors import CORS

from api_client import AntigravityClient
from analysis import analyze_data
from scaledown import Scaledown

API_KEY = "JxaDlyPA2R2nGwTpevwjM2qKDYU5PqJ68mjr0TW2"

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query():
    data = request.json

    region = data["region"]
    climate_type = data["type"]
    start = data.get("start")
    end = data.get("end")
    compress = data.get("compress", False)

    api = AntigravityClient(API_KEY)

    raw_data = api.fetch_climate_data(
        region=region,
        data_type=climate_type,
        start_date=start,
        end_date=end
    )

    if compress:
        raw_data = Scaledown.compress(raw_data)

    result = analyze_data(raw_data)

    return jsonify({
        "region": region,
        "type": climate_type,
        "analysis": result
    })

if __name__ == "__main__":
    app.run(debug=True)
