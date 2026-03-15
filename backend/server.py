from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/satellites")
def satellites():
    data = [
        {"name": "ISS", "altitude": 408, "velocity": 7.66},
        {"name": "STARLINK-1023", "altitude": 550, "velocity": 7.5}
    ]
    return jsonify(data)

@app.route("/api/collisions")
def collisions():
    data = [
        {
            "satA": "STARLINK-1023",
            "satB": "COSMOS-2251",
            "distance": 0.8,
            "risk_score": 82,
            "time": "18 minutes"
        }
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)