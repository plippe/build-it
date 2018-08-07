.PHONY: init run docker-build docker-run

init:
	pip install scapy

run:
	python myspider.py

docker-build:
	docker build -t plippe/build-it .

docker-run:
	docker run --rm -iv $(PWD)/log:/opt/repository/log plippe/build-it
