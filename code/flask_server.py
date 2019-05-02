from flask import Flask, render_template, jsonify, Response
import datetime
import sqlite3 as sqlite
import json

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/fetchData")
def fetchData():
	con = sqlite.connect('../log/templog.db')
	cur = con.cursor()
	con.row_factory = sqlite.Row
	cur.execute("SELECT * FROM templog")
	dataset = cur.fetchall()
	chartData = []
	for row in dataset:
		chartData.append({"Date": row[0], "Temperature": float(row[1])})
	con.close()
	print (chartData)
	return Response(json.dumps(chartData), mimetype='application/json')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)


