import json
from flask import request, make_response, abort
from flask_cors import cross_origin
from flask import current_app as app
from .models import db, CryptoKey, SignedMessage
from datetime import datetime as dt


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


@app.route('/')
def hello():
    response = app.response_class(
        response=json.dumps("hello world"),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/message', methods=['POST'])
def create_signed_message():
    """
    Create a Signed Message Object
    """
    if not request.json or 'message' not in request.json:
        abort(400)
    m = request.json['message']

    # Create a crypto key if it does not exist
    ck = db.session.query(CryptoKey).\
        filter(CryptoKey.public_address == m['address']).\
        first()
    print(ck)
    if not ck:
        ck = CryptoKey(public_address=m['address'],
                       created=dt.now(),
                       network="bitcoin",
                       testnet=False)
        db.session.add(ck)
        db.session.commit()
    # Create a signed message
    new_sm = SignedMessage(message=m['message'],
                           signature=m['signature'],
                           created=dt.now(),
                           cryptokey=ck.public_address,
                           hodl_time_days=100,
                           crypto_value=100.123456789)
    db.session.add(new_sm)
    db.session.commit()

    return make_response(f"{new_sm} successfully created!")
