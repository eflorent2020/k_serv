
run:
	- echo Starting development server
	FLASK_APP=server.py flask run

install:
	- echo install PIP deps
	pip3 install -r requirements.txt
	python3 init_db.py

pytest:
	- echo testing with PyTest
	python3 -m pytest


build:
	- echo building app container
	docker build -t k_srv .

#prepare:
#	ansible-playbook ansible/prepare.yml -i ansible/vars/hosts.yml
deploy:
	ansible-playbook ansible/deploy.yml -i ansible/vars/hosts.yml

