import json

class Connector():

    def __init__(self):
        self.details = json.load(open('dwc_bot/configuration/config.json'))
