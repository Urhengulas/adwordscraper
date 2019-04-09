dep:
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi
	env-ads/bin/pip install -r requirements.txt
	ipython kernel install --user --name=env-ads
setup:
	# remove old image
	# if [ "$(shell docker images -q adwordscraper)" == "" ];then docker image rm adwordscraper;fi

	# build new image
	docker build -t adwordscraper .

run:
	docker run --rm -v "$(shell pwd)/data:/app/data" --name adwordscraper adwordscraper python cli.py data/keywords.csv data/ads.csv

python:
	python cli.py data/keywords.csv data/ads.csv

test:
	python -m tests.test