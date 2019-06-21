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
	if [ ! -d "env" ];then virtualenv env;fi

	# install requirements
	env/bin/pip install -r requirements.txt

python-run:
	env/bin/python cli.py data/keywords.csv data/ads.csv

# additional commands
notebook:
	# update the ipython kernel (for jupyter notebooks)
	ipython kernel install --user --name=env-ads

	# start jupyter notebook
	jupyter notebook

test:
	env/bin/pytest -vv	

lint:
	env/bin/pylint adscraper
	env/bin/pylint tests
	env/bin/pylint cli.py
