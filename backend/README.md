cd backend
virtualenv -p /usr/bin/python3 .
. bin/activate
pip install -r requirements.txt
cp config.sample.py config.py
