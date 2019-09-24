from flask_sqlalchemy import (Column, String, Text,
                              DateTime, Boolean, Model,
                              Integer, Float, ForeignKey)
from sqlalchemy.orm import relationship


class SignedMessage(Model):
    """
    Model for signed messages.
    """
    __tablename__ = 'SignedMessage'
    id = Column(Integer,
                primary_key=True)
    message = Column(Text,
                     index=False,
                     unique=False,
                     nullable=False)
    signature = Column(Text,
                       index=False,
                       unique=False,
                       nullable=False)
    created = Column(DateTime,
                     index=False,
                     unique=False,
                     nullable=False)
    # Foreign Key to CryptoKey
    cryptokey = Column(Text,
                       ForeignKey('cryptokey.public_address'))
    hodl_time_days = Column(Integer,
                            index=False,
                            unique=False,
                            nullable=False)
    crypto_value = Column(Float,
                          index=False,
                          unique=False,
                          nullable=False)


class CryptoKey(Model):
    """
    Model for crypto key accounts.
    """

    __tablename__ = 'CryptoKey'
    public_address = Column(Text,
                            index=False,
                            unique=True,
                            nullable=False,
                            primary_key=True)
    created = Column(DateTime,
                     index=False,
                     unique=False,
                     nullable=False)
    network = Column(String(256),
                     index=False,
                     unique=False,
                     nullable=False)
    testnet = Column(Boolean,
                     index=False,
                     unique=False,
                     nullable=False)
    messages = relationship("SignedMessage", backref="cryptokey")

    def __repr__(self):
        return '<CryptoKey {}>'.format(self.public_address)
