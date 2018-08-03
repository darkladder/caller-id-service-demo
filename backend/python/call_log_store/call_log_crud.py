from call_log_store import CallLogSchema, Base, Session, engine, exc
from .phone_number_normalizer import get_normalized_phone_number

def as_dict(ormResult):
  return {c.name: getattr(ormResult, c.name) for c in ormResult.__table__.columns}

session = Session()

def add_call_log_data(raw_phone_number, context, caller_name):
  try:  
    query = CallLogSchema(raw_phone_number, context, caller_name)
    session.add(query)
    session.commit()
    
    print (str(query.id))
    return str(query.id)

  except exc.SQLAlchemyError as e:
    session.rollback()
    
    raise ValueError(e)

def get_call_log_data_with_phone_number(raw_phone_number):
  '''
  Note: This currently only returns the first result.
  '''
  try:
    result = session.query(CallLogSchema).filter(CallLogSchema.phone_number == get_normalized_phone_number(raw_phone_number)).first()

    if result == None:
      raise ValueError("No results")

    return as_dict(result)
    
  except exc.SQLAlchemyError as e:
    raise ValueError(e)