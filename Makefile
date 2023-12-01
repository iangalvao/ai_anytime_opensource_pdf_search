build:
	docker build -t langchain_notebook .

run:
	docker run -it -p 8501:8501 -v $$(pwd)/.env:/my_app/.env -v $$(pwd)/app/:/my_app/app/ langchain_notebook /bin/bash