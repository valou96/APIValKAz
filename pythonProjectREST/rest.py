from csv import DictReader
from flask import Flask, jsonify, request


egapro_data = {}

with open("index-egalite-fh-utf8.csv", encoding='utf-8') as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')

    for row in reader:
        siren = row.get("SIREN")
        annee = row.get("Année")

        if not siren or not annee:
            continue

        if egapro_data.get(siren) is None:
            egapro_data[siren] = row
        elif egapro_data[siren].get("Année", "") < annee:
            egapro_data[siren].update(row)

application = Flask(__name__)


@application.route("/api/siren/<siren>", methods=["GET"])
def get_siren_data(siren: str):
    """
    Return the EgaPro data for a given SIREN number.
    A 404 is returned if the SIREN is not found.

    :param siren: SIREN number as string
    :return: The corresponding data as a JSON
    """
    response = egapro_data.get(siren)

    if response is None:
        return jsonify({"error": "SIREN not found"}), 404
    return jsonify(response), 200


@application.route("/api/sirens", methods=["GET"])
def get_all_sirens():
    """
    Return a list of all available SIREN numbers.
    """
    sirens = list(egapro_data.keys())
    return jsonify(sirens), 200


@application.route("/api/data", methods=["GET"])
def get_all_data():
    """
    Return all EgaPro data.
    """
    return jsonify(egapro_data), 200


if __name__ == "__main__":
    application.run(debug=True)