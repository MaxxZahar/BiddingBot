import os
from environs import Env

env = Env()
env.read_env()

SYSTEMS = {'crazy': {'admin': [int(admin) for admin in env.list('ADMINS')][0], 'path': os.path.normpath('public/systems/crazy.csv'), 
                     'id': 1}}