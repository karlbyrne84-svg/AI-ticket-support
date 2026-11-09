from flask import Flask, request, jsonify
from flask_cors import CORS
from src.models import predict_category, predict_priority
from src.llmMk2 import ticket_summary

app = Flask(__name__)
CORS(app)

@app.route("/analyse", methods=["POST"])
def get_ticket():

    data = request.get_json()

    ticket = data.get("ticket", "").strip()

    if not ticket:
        return jsonify({"error": "No ticket found"}), 400

    summary = ticket_summary(ticket)

    return jsonify({
        "message": "Ticket recieved",
        "ticket summary": summary
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
