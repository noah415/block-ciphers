import urllib.parse

def submit(msg: str):
  info = 'userid=456; userdata='
  session_id = ';session-id=31337'

  data = safe_string = urllib.parse.quote_plus(info + msg + session_id)

  # pad the data

  # encrypt the data

  return encrypted_data

def verify():
  pass
