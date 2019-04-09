# use via docker (standard way)
setup:
	# build new image
	docker build -t adwordscraper .

run:
	docker run --rm -v "$(shell pwd)/data:/app/data" --name adwordscraper adwordscraper python cli.py data/keywords.csv data/ads.csv


# use via python directly
python-setup:
	# is env-ads already existing?
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi

	# install requirements
	env-ads/bin/pip install -r requirements.txt

	# update the ipython kernel (for jupyter notebooks)
	ipython kernel install --user --name=env-ads

python-run:
	python cli.py data/keywords.csv data/ads.csv

notebook:
	# update the ipython kernel (for jupyter notebooks)
	ipython kernel install --user --name=env-ads

	# start jupyter notebook
	jupyter notebook

# tests
test:
	python -m tests.test