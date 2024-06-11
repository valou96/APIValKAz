from csv import DictReader
from flask import Flask
from spyne import Application, rpc, ServiceBase, Integer, Unicode, ComplexModel, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Read the index-egalite-fh.csv file and store it in a dictionary
egapro_data = {}

with open("index-egalite-fh-utf8.csv") as csv_file:
    reader = DictReader(csv_file, delimiter=";", quotechar='"')
    for row in reader:
        if egapro_data.get(row["SIREN"]) is None:
            egapro_data[row["SIREN"]] = row
        elif egapro_data[row["SIREN"]]["Année"] < row["Année"]:
            egapro_data[row["SIREN"]].update(row)

class EgaProData(ComplexModel):
    SIREN = Unicode
    Année = Unicode
    Score = Unicode
    # Add other fields as necessary
    a

class EgaProService(ServiceBase):
    @rpc(Unicode, _returns=EgaProData)
    def get_data_by_siren(ctx, siren):
        """
        Return the EgaPro data for a given SIREN number.
        """
        data = egapro_data.get(siren)
        if data:
            return EgaProData(**data)
        return None
    
    @rpc(_returns=Iterable(Unicode))
    def get_all_sirens(ctx):
        """
        Return a list of all available SIREN numbers.
        """
        return egapro_data.keys()

    @rpc(_returns=Iterable(EgaProData))
    def get_all_data(ctx):
        """
        Return all EgaPro data.
        """
        return [EgaProData(**data) for data in egapro_data.values()]

application = Flask(__name__)

soap_app = Application(
    [EgaProService],
    tns='spyne.examples.flask',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(soap_app)

@application.route("/soap", methods=["POST"])
def soap_service():
    """
    SOAP endpoint to handle SOAP requests.
    """
    return wsgi_application

if __name__ == "__main__":
    application.run(debug=True)
