from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/capture", methods=["POST"])
def capture():
    try:
        data = request.get_json()

        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        filename = f"capture_{timestamp}.json"

        # Join unique file name to directory
        filepath = os.path.join('Captures', filename)

        # Write the JSON data to the file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

        return jsonify({"message": "Data successfully captured"}), 200
                        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Some MacOS devices use port default port 5000 in other processes (using 8080 to avoid conflicts)
    app.run(host="0.0.0.0", port=8080, debug=True)