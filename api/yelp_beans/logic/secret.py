# -*- coding: utf-8 -*-
import json
import os


def get_secret(id):
    if os.path.isfile("client_secrets.json"):
        secrets = json.loads(open("client_secrets.json").read())
        return secrets[id]
    else:
        raise IOError("No secrets file.")
