from sqlalchemy import Column, String, Integer, Date
from .base import Base
from .phone_number_normalizer import get_normalized_phone_number

# @see https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
class CallLogSchema(Base):
  __tablename__ = 'call_logs'
  id=Column(Integer, primary_key=True)
  phone_number=Column('phone_number', String(45))
  context=Column('context', String(45))
  caller_name=Column('caller_name', String(100))

  def __init__(self, raw_phone_number, context, caller_name):
    phone_number = get_normalized_phone_number(raw_phone_number)

    self.phone_number = phone_number
    self.context = context
    self.caller_name = caller_name
  
    return