# define `make run` (convenience purposes) 
make run:
	make python-run

# use via docker (standard way)
docker-setup:
	# build new image
	docker build -t adwordscraper .

docker-run:
	docker run --rm -v "$(shell pwd)/data:/app/data" --name adwordscraper adwordscraper python cli.py data/keywords.csv data/ads.csv


# use via python directly
python-setup:
	# is env-ads already existing?
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi

	# install requirements
	env-ads/bin/pip install -r requirements.txt

python-run:
	env-ads/bin/python cli.py data/keywords.csv data/ads.csv

# additional commands
notebook:
	# update the ipython kernel (for jupyter notebooks)
	ipython kernel install --user --name=env-ads

	# start jupyter notebook
	jupyter notebook

test:
	env-ads/bin/pytest -vv	

lint:
	env-ads/bin/pylint adscraper
	env-ads/bin/pylint tests
	env-ads/bin/pylint cli.py
