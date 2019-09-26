import json
from flask import request, make_response, abort
from flask_cors import cross_origin
from flask import current_app as app
from models import db, CryptoKey, SignedMessage
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

    # Create a crypto key
    m = request.json['message']
    new_ck = CryptoKey(public_address=m['address'],
                       created=dt.now(),
                       network="bitcoin",
                       testnet=False)
    db.session.add(new_ck)
    db.session.commit()
    # Create a signed message
    new_sm = SignedMessage(message=m['message'],
                           signature=m['signature'],
                           created=dt.now(),
                           cryptokey=new_ck,
                           hodl_time_days=100,
                           crypto_value=100.123456789)
    db.session.add(new_sm)
    db.session.commit()

    return make_response(f"{new_sm} successfully created!")

'''
@app.route('/u', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the "
                            "playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")
'''
