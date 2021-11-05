#/bin/sh
python3 -m venv ./django_venv
source ./django_venv/bin/activate
pip3 install -r requirement.txt

pip3 install ../ex00/django-gallery/dist/django-gallery-0.1.tar.gz

cp nginx.conf /usr/local/etc/nginx/nginx.conf
mkdir /usr/local/etc/nginx/servers/
cp myproject /usr/local/etc/nginx/servers/myproject

brew services restart nginx

uwsgi --ini project_uwsgi.ini
