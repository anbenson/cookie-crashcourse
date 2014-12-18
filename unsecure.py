from flask import Flask, request, make_response

# app configuration
app = Flask(__name__)
app.debug = True
PORT = 8080

# helper functions
def isUserAwesome(username):
  return username == "ANDREW"

# constants
suc_message = "OH NO! YOU BROKE INTO THE WEBSITE!"
norm_message = "GREETINGS FROM THE SERVER, HELLO WORLD!"

# routing
@app.route("/")
def homePage():
  cookie = request.cookies.get("USERID", "GUEST")
  if isUserAwesome(cookie):
    resp = make_response(suc_message)
    resp.set_cookie("USERID", makeCookie("ANDREW"))
  else:
    resp = make_response(norm_message)
    resp.set_cookie("USERID", makeCookie("GUEST"))
  return resp

# run the app
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
