# hodlboard


## Design

1. Frontend is a static and can be seen under web/. We use HTML, CSS, JS

2. Backend is Flask, Python3, MySQL & Docker. This runs in Google Cloud Run and serves the API

3. Frontend www.hodlboard.com calls Backend api.hodlboard.com

4. Staging frontend staging.hodlboard.com calls backend api.staging.hodlboard.com


## Local Testing

0. My OS is Mac OSX

1. Set up a python 3 environment. I use Anaconda. Install packages in requirements.text

2. <DB Setup>

3. Run the below from the python environment to serve static files locally

(inside the web/ directory)
python -m http.server

http://localhost:8000 should host index.html

4. <API Container Launch>


## Deploying staging


### Deploying Staging API

1. Run the below to deploy a new staging API container

gcloud builds submit --tag gcr.io/hodlboard/hodlboard-staging

2. Run the below to update the staging revision

gcloud beta run deploy hodlboard-staging --image gcr.io/hodlboard/hodlboard-staging

### Deploying Staging Web

1. Run the below from the python environment to deploy staging

(inside the hodlboard/ directory)
python deploy_web.py


## Deploying Production


### Deploying production API

1. <TBD>

### Deploying production Web

1. Run the below from the python environment to deploy production. You will need to confirm

(inside the hodlboard/ directory)
python deploy_web.py --production
