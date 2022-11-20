import os
from dotenv import dotenv_values

TOKEN = dotenv_values(dotenv_path='.env').get('TOKEN')
