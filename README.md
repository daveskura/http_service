# http_service
 
Creating a simple microservice on GCP

## Create an Artifact repo on GCP
```
gcloud artifacts repositories create dave-docker-repo --repository-format=docker --location=northamerica-northeast1 --description="Daves Docker Repository"

gcloud config get-value project
gcloud config set artifacts/location northamerica-northeast1
gcloud artifacts repositories list
```
## create basic_http_service.py

	import os
	from flask import Flask, request

	app = Flask(__name__)

	@app.route("/", methods=["GET"])
	def homepage():
		if request.method == "GET":
			return "Hello World!"

	PORT = int(os.environ.get("PORT", 8080))
	if __name__ == '__main__':
		app.run(threaded=True,host='0.0.0.0',port=PORT)

## create requirements.txt

	flask
	gunicorn

## create a Dockerfile

	FROM python:3.6-slim-buster
	WORKDIR /app
	COPY . .
	RUN pip install -r requirements.txt
	CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 basic_http_service:app


## build an image on gcp and push to the repo
```
SET PROJECT_ID=<my gcp project id>
gcloud builds submit --region=northamerica-northeast1 --tag northamerica-northeast1-docker.pkg.dev/%PROJECT_ID%/dave-docker-repo/basic_http_service:initial_build
```

### if you get an error message like this...
denied: Permission "artifactregistry.repositories.uploadArtifacts" denied on resource

you need to run:
```
gcloud auth login
gcloud init
```


## deploy to Cloud Run



