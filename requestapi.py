from typing import Optional
from fastapi import FastAPI
import pymysql.cursors
from flask import Flask,render_template
conn = pymysql.connect(host='remotemysql.com',
                        port=3306,
                        database='fvpnSn9xtp',
                        user='fvpnSn9xtp',
                        password='x6DdkN6mXz')

app = Flask(__name__)
@app.route("/")
def read_root():
    return {"Hello": "World"}

@app.route("/ap")
def ap():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM ap ORDER BY id_ap DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_ap": result[0],
                "ap": result[1],
                "avg_ap": result[2],
                "level_ap": result[3],
                "time": result[4]}
@app.route("/dst")
def dst():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM dst ORDER BY id_dst DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_dst": result[0],
                "dst": result[1],
                "avg_dst": result[4],
                "level_dst": result[5],
                "time": result[3]}
@app.route("/kp")
def kp():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM kp_index ORDER BY id_kp DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_kp": result[0],
                "kp": result[1],
                "avg_kp": result[2],
                "level_kp": result[3],
                "time": result[4]}
@app.route("/radio")
def radio():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM radio ORDER BY radio_id DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"radio_id": result[0],
                "r1_r2": result[1],
                "avg_radio": result[2],
                "level_radio": result[3],
                "time": result[4]}
@app.route("/f107")
def f107():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM solarflux ORDER BY id_flux DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_flux": result[0],
                "adjusted_flux": result[1],
                "avg_flux": result[2],
                "level_flux": result[3],
                "time": result[4]}
@app.route("/srstorm")
def srstorm():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM srstorm ORDER BY id_srs DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_srs": result[0],
                "srstorm": result[1],
                "avg_srs": result[2],
                "level_storm": result[3],
                "time": result[4]}
@app.route("/knn")
def knn():
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM Knn ORDER BY id_knn DESC "
        cursor.execute(sql)
        result = cursor.fetchone()
        return {"id_knn": result[0],
                "knn": result[1],
                "time": result[2]}
#
@app.route("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
    