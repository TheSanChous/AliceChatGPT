from json import load
from dotenv import dotenv_values

secrets = dotenv_values(".env")

configuration = dict(**load(open("appsettings.json", encoding="UTF-8")), **secrets)
