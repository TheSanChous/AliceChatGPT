from json import load
from dotenv import dotenv_values
from os import environ

secrets = {**dotenv_values(".env"), **environ}

configuration = dict(**load(open("appsettings.json", encoding="UTF-8")), **secrets)
