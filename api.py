# app.py
from flask import Flask, request, jsonify
from src.fundamental_analyst.crew import FundamentalAnalyst
import os
from datetime import datetime
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/fundamental-report", methods=["POST"])
def generate_fundamental_report():
    data = request.get_json()

    # Validate input
    required_fields = ["company_name"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Missing fields. Required: {', '.join(required_fields)}"}), 400

    # Add default current_year if missing
    if "current_year" not in data:
        data["current_year"] = str(datetime.now().year)

    try:
        # Run the crew
        FundamentalAnalyst().crew().kickoff(inputs=data)

        # Try to read the result file
        report_path = "report.md"
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                report_content = f.read()
            return jsonify({
                "message": "Report generated successfully.",
                "company": data["company_name"],
                "year": data["current_year"],
                "report": report_content
            }), 200
        else:
            return jsonify({"error": "report.md file not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8092)
