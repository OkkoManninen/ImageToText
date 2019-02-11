#Insert image link
link = "Link_here"
#Insert project_ID 
PROJECT_ID = "Project_ID_here"
gcloud services enable vision.googleapis.com
export GOOGLE_CLOUD_PROJECT="PROJECT_ID"
gcloud iam service-accounts create my-vision-sa \
  --display-name "my vision service account"
  gcloud iam service-accounts keys create ~/key.json \
  --iam-account my-vision-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com
  export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"
  
  
  ipython
  
  
  
  
  from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
image.source.image_uri = 'link'
resp = client.text_detection(image=image)
print('\n'.join([d.description for d in resp.text_annotations]))
