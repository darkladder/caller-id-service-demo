from flask import Flask, request 
from call_log_store import call_log_crud
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  app.logger.debug(request.args)
  return "API is online"

@app.route('/number', methods=['POST'])
def addCallerLogData():
  '''
  Adds caller id data to the service.
  '''

  app.logger.debug(request.json)

  try:
    raw_phone_number = request.json['number']
    context = request.json['context']
    caller_name = request.json['name']

    caller_log_data = call_log_crud.add_call_log_data(raw_phone_number, context, caller_name)
    app.logger.debug(caller_log_data)

    return json.dumps({
      'status': 'success'
    })

  except ValueError as e:
    app.logger.debug(e)

    return json.dumps({
      'error': 'Could not add record. Possible duplicate value.'
    }), 404

@app.route('/number/<string:raw_phone_number>', methods=['GET'])
def getCallerLogData(raw_phone_number):
  '''
  Retrieves caller id data from the service.
  '''
  try:
    caller_log_data = call_log_crud.get_call_log_data_with_phone_number(raw_phone_number)

    resp_data = {
      'number': caller_log_data['phone_number'],
      'context': caller_log_data['context'],
      'name': caller_log_data['caller_name']
    }

    app.logger.debug(caller_log_data)

    return json.dumps(resp_data)

  except ValueError as e:
    app.logger.debug(e)
    
    return json.dumps({
      'error': 'Could not locate record.'
    }), 404