sudo apt-get remove libapache2-mod-wsgi
sudo apt-get install libapache2-mod-wsgi-py3
a2enmod wsgi
pip install virtualenv
virtualenv -p python3 ./venv
source ./venv/bin/activate
pip install -r requirements.txt

