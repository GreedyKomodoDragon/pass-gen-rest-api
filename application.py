from functions.pass_strength import pass_strength
from functions.pass_gen import pass_gen
from flask import Flask, jsonify, request
from flask_api import status

application = app = Flask(__name__)

@application.route("/")
def hello():
  return "API for PassGen"

@application.route("/api/v1/passgen/<int:length>/<int:hasSym>", methods=['GET'])
def handlePasswordGeneration(length: int, hasSym: int):
  if length < 8:
    return "invalid", status.HTTP_204_NO_CONTENT

  return jsonify({"password":pass_gen(length, hasSym)}), status.HTTP_200_OK
  

@application.route("/api/v1/strength", methods=['POST'])
def handleStrengthCheck():

  if "password" in request.form:
    password = request.form["password"]

    return jsonify({"score":pass_strength(password)}), status.HTTP_200_OK
  
  else:
    return "invalid", status.HTTP_204_NO_CONTENT




if __name__ == "__main__":
  application.run('localhost',port=8000)