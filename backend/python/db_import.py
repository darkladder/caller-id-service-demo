'''
Imports records into our DB.
'''

from call_log_store import call_log_crud
import csv
import phonenumbers

with open('/tmp/callerid.csv', 'r') as csvfile:
  logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in logreader:
    raw_phone_number = row[0]
    context = row[1]
    caller_name = row[2]

    try:
      call_log_crud.add_call_log_data(raw_phone_number, context, caller_name)
    
    except ValueError as e:
      # Duplicate input, ignore
      print (e)