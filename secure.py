import hashlib
from flask import Flask, request, make_response

# app configuration
app = Flask(__name__)
app.debug = True
PORT = 8080

# helper functions
def isUserAwesome(username):
  return username == "ANDREW"

def makeCookie(userid):
  return "%s|%s" %(userid, hashlib.sha256(userid+SALT).hexdigest())

def isCookieValid(cookie):
  (userid, hashed) = parseCookie(cookie)
  return hashed == hashlib.sha256(userid+SALT).hexdigest()

def parseCookie(cookie):
  parsed = cookie.split("|")
  userid = parsed[0]
  if (len(parsed) > 1):
    hashed = parsed[1]
  else:
    hashed = ""
  return (userid, hashed)

# constants
suc_message = "OH NO! YOU BROKE INTO THE WEBSITE!"
norm_message = "GREETINGS FROM THE SERVER, HELLO WORLD!"
SALT = "@#3k25l23#KW#LRsekr@#"

# routing
@app.route("/")
def homePage():
  cookie = request.cookies.get("USERID", "GUEST")
  (userid, hashed) = parseCookie(cookie)
  if isUserAwesome(userid) and isCookieValid(cookie):
    resp = make_response(suc_message)
    resp.set_cookie("USERID", makeCookie("ANDREW"))
  else:
    resp = make_response(norm_message)
    resp.set_cookie("USERID", makeCookie("GUEST"))
  return resp

# run the app
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
