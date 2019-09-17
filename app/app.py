import os
import logging
import json

from flask import Flask
from flask_cors import cross_origin

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

@app.route('/content')
@cross_origin(["staging.hodlboard.com"])
def home():
	data = {
		'msg': "this is a message text from staging-2",
		'key': "1234abcd",
		'crypto': "btc",
		'amt': 100
	}
	r = []
	for i in range(7):
		r.append(data)
	response = app.response_class(
		response=json.dumps(r),
		status=200,
		mimetype='application/json'
	)
	return response

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
