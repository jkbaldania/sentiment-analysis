from flask import Flask, request
from flask_restful import Resource, Api
from germansentiment import SentimentModel
import os
import sys

app = Flask(__name__)
api = Api(app)
model = SentimentModel()
port = 5000

if sys.argv.__len__() > 1:
    port = sys.argv[1]

print("Port is : " + str(port))

class SentimentAnalysis(Resource):
    def put(self, getSentiment):
        sentiment = model.predict_sentiment([str(request.form['sentence'])])
        return {"sentiment": sentiment}

api.add_resource(SentimentAnalysis, '/<string:getSentiment>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)