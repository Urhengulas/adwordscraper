dep:
	if [ ! -d "env-ads" ];then virtualenv env-ads;fi
	env-ads/bin/pip install -r requirements.txt
	ipython kernel install --user --name=env-ads