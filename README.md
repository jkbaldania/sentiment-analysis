# Sentiment Analysis using Python "germansentiment" package

## Live at:
https://flask-service.o6cp6h5btngdi.us-west-2.cs.amazonlightsail.com/getSentiment

## CURL usage of REST API:
curl https://flask-service.o6cp6h5btngdi.us-west-2.cs.amazonlightsail.com/getSentiment -d "sentence=nicht so schlecht wie erwartet" -X PUT

Replace the sentence with any german sentence to get the json response indicating the sentiment of the sentence ("negative", "positive" or "neutral").

## Deploy in local machine (Create image and run container)
* Clone this github repo.
* Make sure to have Docker installed in the machine.
* In cmd, change the directory to the location where "service.py" file is located.
* In cmd, run the command : docker build -t sentimentanalysis:latest .
* Wait for few minutes for image to build.
* In cmd, run the command : docker run -it -p 5000:5000 sentimentanalysis
* Wait for the container to spin up.
* Check in the logs that Flask REST Application has started.
* In cmd, run the command : curl http://localhost:5000/getSentiment -d "sentence=Mit keinem guten Ergebniss" -X PUT
* Check the response. It should be : {"sentiment": ["negative"]}

## Deploy in AWS
* Prerequisites are:
  * AWS Account.
  * Docker should be installed in the machine.
  * AWS CLI should be installed in the machine.
  * AWS lightsailctl plugin should be installed in the machine.
* Repeat above steps for local machine, only upto building the image out of a container.
* In cmd, change the directory to the location where "service.py" file is located.
* Using cmd, do the following:
  * Create container service.
  * Deploy the container.
