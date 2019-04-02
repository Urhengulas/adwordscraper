dep:
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi
	env-ads/bin/pip install -r requirements.txt
	ipython kernel install --user --name=env-ads

run:
	echo $(pwd)
	sudo docker run --rm -v "/home/urhengulas/Documents/CODE/semster2/STS_Correctiv/adwordscraper/data:/app/data" --name adwordscraper adwordscraper python main.py data/keywords.csv
