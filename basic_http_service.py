"""
  Dave Skura
  
"""

print (" Starting ") # 
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
	if request.method == "GET":
		return "Hello from basic_http_service.py"

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
	app.run(threaded=True,host='0.0.0.0',port=PORT)