from . import db as db


class CryptoKey(db.Model):
    """
    Model for crypto key accounts.
    """

    __tablename__ = 'CryptoKey'
    public_address = db.Column(db.String(256),
                               index=False,
                               unique=True,
                               nullable=False,
                               primary_key=True)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    network = db.Column(db.String(256),
                        index=False,
                        unique=False,
                        nullable=False)
    testnet = db.Column(db.Boolean,
                        index=False,
                        unique=False,
                        nullable=False)
    messages = db.relationship("SignedMessage", backref="messages")

    def __repr__(self):
        return '<CryptoKey {}>'.format(self.public_address)


class SignedMessage(db.Model):
    """
    Model for signed messages.
    """
    __tablename__ = 'SignedMessage'
    id = db.Column(db.BigInteger,
                   primary_key=True)
    message = db.Column(db.Text,
                        index=False,
                        unique=False,
                        nullable=False)
    signature = db.Column(db.Text,
                          index=False,
                          unique=False,
                          nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    # Foreign Key to CryptoKey
    cryptokey = db.Column(db.String(256),
                          db.ForeignKey('CryptoKey.public_address'))
    hodl_time_days = db.Column(db.BigInteger,
                               index=False,
                               unique=False,
                               nullable=False)
    # precision- digits, scale- digits after decimal point
    crypto_value = db.Column(db.Numeric(precision=32, scale=12),
                             index=False,
                             unique=False,
                             nullable=False)

    def __repr__(self):
        return '<SignedMessage {}>'.format(self.id)
