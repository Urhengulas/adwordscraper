dep:
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi
	env-ads/bin/pip install -r requirements.txt
	ipython kernel install --user --name=env-ads

run:
	sudo docker run --rm -v "$(pwd)/data:/app/data" --name adwordscraper adwordscraper python main.py data/keywords.csv
