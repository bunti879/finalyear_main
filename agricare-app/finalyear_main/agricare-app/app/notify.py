from flask import Blueprint, jsonify, request

notify = Blueprint("notify", __name__)
subscriptions = []  # in-memory for now

@notify.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    subscriptions.append(data)
    return jsonify({"status": "subscribed"})

@notify.route("/send", methods=["POST"])
def send():
    return jsonify({"status": "sent", "subs_count": len(subscriptions)})
