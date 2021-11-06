from flask import *
import mysql.connector
import requests

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sweet123",
  database="AVA_Data",
  autocommit = True
 )

cursor = mydb.cursor()

app = Flask(__name__)

def query_db(query):
    cursor.execute(query)
    return cursor.fetchall()

@app.route("/")
def index():
    res = requests.get('http://localhost:5000/getAllRequests')
    res_json = res.json()
    return render_template("index.html", req_data = res.json())

@app.route("/createRequest")
def create_req():
    params = list(request.args)
    user_name = params[0]
    business_name = params[1]
    time = params[2]
    req_type = params[3]
    special_info = params[4]
    cursor.execute(f"INSERT INTO Requests(guestName, businessName, reqTime, reqType, otherInfo) VALUES (\'{user_name}\', \'{business_name}\', \'{time}\', \'{req_type}\', \'{special_info}\')")
    return jsonify(response = "Values inserted successfully")

@app.route("/getAllRequests")
def get_req():
    data_tuples = []
    for entry in query_db(f"SELECT * FROM Requests"):
        data_tuples.append(entry)
    return jsonify(data_tuples)

@app.route("/reqCount")
def req_amt():
    res = list(query_db("SELECT COUNT(*) FROM Requests")[0])[0]
    return jsonify(count = res)

if __name__ == "__main__":
    app.run(debug=True)
