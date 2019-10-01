import json
import simplejson as simplejson
from decimal import Decimal
from datetime import datetime as dt

from flask import request, make_response, abort
from flask_cors import cross_origin
from flask import current_app as app

from .models import db, CryptoKey, SignedMessage


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


'''
Sample POST
{
    "message": {
    "address": "abcd1234",
    "message": "hello hodlboard-1",
    "signature": "hxllx hxdlxxard-x1",
    "show_hodl_time": true,
    "show_crypto_value": true
    }
}
'''


@app.route('/message', methods=['POST', 'GET'])
def handle_message_request():
    if request.method == 'POST':
        """
        Create a Signed Message Object
        """
        m = request.form

        # Create a crypto key if it does not exist
        ck = db.session.query(CryptoKey).\
            filter(CryptoKey.public_address == m['address']).\
            first()
        if not ck:
            ck = CryptoKey(public_address=m['address'],
                           created=dt.now(),
                           network="bitcoin",
                           testnet=False)
            db.session.add(ck)
            db.session.commit()
        # Create a signed message
        hodl_flag = False
        currency_value_flag = False
        if "hodl-time" in m:
            hodl_flag = True
        if "currency-value" in m:
            currency_value_flag = True
        new_sm = SignedMessage(message=m['message'],
                               signature=m['signature'],
                               created=dt.now(),
                               cryptokey=ck.public_address,
                               hodl_time_days=100,
                               crypto_value=Decimal("123456789.123456786"),
                               show_hodl_time=True if hodl_flag else False,
                               show_crypto_value=True if currency_value_flag else False,
                               view_count=0)
        db.session.add(new_sm)
        db.session.commit()

        return make_response(f"{new_sm} successfully created!")
    else:
        """
        Return signed messages
        """
        messages = db.session.query(SignedMessage).all()
        d = {}
        for m in messages:
            # Iterate over the messages
            d[m.id] = {
                "message": m.message,
                "created": "{} {} {}".format(m.created.day,
                                             m.created.month,
                                             m.created.year),
                "views": m.view_count
            }
            if m.show_hodl_time:
                d[m.id]["hold_days"] = m.hodl_time_days
            if m.show_crypto_value:
                d[m.id]["crypto_value"] = m.crypto_value
        response = app.response_class(
            response=simplejson.dumps(d),
            status=200,
            mimetype='application/json'
        )
        return response
