import phonenumbers

def get_normalized_phone_number(raw_phone_number):
  x = phonenumbers.parse(raw_phone_number, "US")
  return phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)