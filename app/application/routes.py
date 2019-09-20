import json

from flask import Flask
from flask_cors import cross_origin


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
