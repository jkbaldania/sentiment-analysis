# Sentiment Analysis using Python "germansentiment" package

## Deploy in local machine
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
