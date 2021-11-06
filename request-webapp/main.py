from flask import *
import mysql.connector

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
    return render_template("index.html")

@app.route("/createRequest")
def create_req():
    params = list(request.args)
    user_id = params[0]
    business_id = params[1]
    time = params[2]
    req_type = params[3]
    special_info = params[4]
    cursor.execute(f"INSERT INTO Requests(guestId, businessId, reqTime, reqType, otherInfo) VALUES ({user_id}, {business_id}, {time}, \'{req_type}\', \'{special_info}\')")
    return jsonify(response = "Values inserted successfully")

@app.route("/getRequest")
def get_req():
    req_id = list(request.args)[0]
    req_id, user_id, business_id, time, req_type, special_info = query_db(f"SELECT * FROM Requests WHERE id={req_id}")[0]
    time = str(time)
    return jsonify(user = user_id, business = business_id, time = time, req_type = req_type, other = special_info)

if __name__ == "__main__":
    app.run(debug=True)
