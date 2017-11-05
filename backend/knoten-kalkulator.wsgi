import sys
import os
os.environ['APP_CONFIG'] = 'development'
os.environ['APP_DEVELOPMENT_DATABASE_URI'] = 'postgres://foobar:foobar@localhost/foobar'
sys.path.insert(0, '/var/www/vhosts/kk.local/knoten-kalkulator/backend/lib/python3.5/site-packages')
sys.path.insert(1, '/var/www/vhosts/kk.local/knoten-kalkulator/backend')
activate_this = '/var/www/vhosts/kk.local/knoten-kalkulator/backend/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
from flask_script import Manager
from app import create_app, db

application = create_app(os.getenv('APP_CONFIG', 'development'))
manager = Manager(application)
