from flask import Flask,jsonify,request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
try:
    env = os.environ.get('MAIN')
except:
    pass

@app.route('/',methods=['GET'])
def index():
    name = request.args.get('name')
    
    if name:
        return jsonify({"status":200,"message":f"hello {name} how are you {env}"})
    return "<h1> write in url ? name=any one name </h1>"

if __name__ == "__main__":
    app.run(debug=True)

