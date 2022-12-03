from flask import Flask, render_template, request, redirect
import requests
import json
from waitress import serve

app = Flask(__name__)

app.secret_key = "BHrTTJ24VkvS7B2pQ15v"

@app.route('/')
def home():
    return redirect("https://www.projectrexa.ml/blogs")

@app.route('/pokemon')
def pokemon():
    try:
        if request.args.get('search') == None:
            id = "1"
        else:
            id = request.args.get('search').lower()
        data = (requests.get(f"https://api.projectrexa.ml/pokemon?key=Wqccm_WrbLkuRxpe-InFHo_cwuVWzEszyX0t2_vJ&query={id}").json()) 
        name=data["name"]
        if data["secondary_type"] == None:
            secondary = "blank"
        else:
            secondary = data["secondary_type"]
        if (requests.get(f"https://img.pokemondb.net/sprites/black-white/anim/normal/{name}.gif").status_code) == 200:
            link = f"https://img.pokemondb.net/sprites/black-white/anim/normal/{name}.gif"
        else:
            link = f"https://cdn.projectrexa.ml/sprites/{name}.png"
 
        return render_template("dex.html",link = link, name=data["name"],id=data["_id"],type_1=data["primary_typing"],type_2=secondary,description=data["description"],height=data["height"],weight=data["weight"],hp=data["hp"],attack=data["attack"],defence=data["defence"],special_attack=data["special_attack"],special_defence=data["special_defence"],speed=data["speed"])
    except:
        return "Not Found"


if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=8080)
