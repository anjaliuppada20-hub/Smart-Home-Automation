from flask import Flask, render_template, jsonify
from hardware import get_devices, set_device

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", devices=get_devices())


@app.route("/api/devices")
def devices():
    return jsonify(get_devices())


@app.route("/api/device/<name>/<state>")
def control_device(name, state):
    if state not in ["on", "off"]:
        return jsonify({"error": "Invalid state"}), 400

    if set_device(name, state):
        return jsonify({
            "device": name,
            "state": state,
            "status": "success"
        })

    return jsonify({"error": "Unknown device"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
