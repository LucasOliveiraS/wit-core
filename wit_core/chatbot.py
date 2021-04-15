import os
from wit import Wit
from dotenv import load_dotenv

from .core import utils


load_dotenv(dotenv_path=os.path.abspath(os.curdir) + '/.env')


def get_user_input(message, access_token=os.getenv("ACCESS_TOKEN")):
    '''
        Receive user message and search for intents.
    '''
    wit_client = Wit(access_token)

    response = wit_client.message(message)
    if not response['intents']:
        raise Exception(
            "No intents were found for the question: "
            + message)

    return utils.rename_entities_keys(response)
