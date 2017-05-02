"""
Example application showing the use of the Translate method in the Text Translation API.
"""

from xml.etree import ElementTree
from microsoft_translator.auth import AzureAuthClient
import requests


class translator(object):
    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.access_token = AzureAuthClient(client_secret)

    def translate(self, textToTranslate, fromLangCode, toLangCode):
        token = self.access_token.get_access_token()
        bearer_token = 'Bearer ' + token.decode("utf-8") 
        headers = {"Authorization ": bearer_token}
        translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

        translationData = requests.get(translateUrl, headers = headers)
        # parse xml return values
        translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
        return translation.text
    

