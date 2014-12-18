from flask import Flask, request, make_response

# app configuration
app = Flask(__name__)
app.debug = True
PORT = 8080

# routing
@app.route("/")
def homePage():
  user = request.cookies.get("NAME", "Guest")
  respText = "Server is running. Hello World. Hello " + user + ".\n"
  resp = make_response(respText)
  resp.set_cookie("NAME", user)
  return resp

# run the app
if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = PORT)
