import json
from flask import Flask, jsonify
app = Flask(__name__)
def load_airport_data():
    try:
        with open('airports.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: airports.json file not found.")
        return []
airports = load_airport_data()
@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    target_icao = icao.upper()
    airport_found = next((a for a in airports if a.get('ident') == target_icao), None)
    if airport_found:
        response = {
            "icao": airport_found.get('ident'),
            "name": airport_found.get('name'),
            "city": airport_found.get('municipality'),
            "country": airport_found.get('iso_country')
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": f"Airport with ICAO {target_icao} not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)