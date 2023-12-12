from flask import Flask, request, render_template

from random import randint
from back_file import backward_trans
from front_file import read_file,get_image_name
import hashlib
locations={}
locations["inistra"]={"name": "Не чекается", "pos":"0","location":"inistra"}
locations["two_k"]={"name": "Не чекается", "pos":"0","location":"two_k"}
locations["tera"]={"name": "Не чекается", "pos":"0","location":"tera"}
locations["song"]={"name": "Не чекается", "pos":"0","location":"song"}
locations["solrid"]={"name": "Не чекается", "pos":"0","location":"solrid"}
locations["ppz"]={"name": "Не чекается", "pos":"0","location":"ppz"}



app = Flask(__name__)
app.config.from_object('config')
def has_f(s):
    md5_hash = hashlib.md5(s.encode()).hexdigest()
    return str(md5_hash)
    pass

"""
@app.route('/',methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        key=request.form['key']
        place=request.form['place_w']
        base=request.form['base_w']
        len=request.form['len']
        if len=="":
            print("EMPTY")
        a=forward_trans(key,base,place)

        return render_template('form.html',info=a)
    return render_template('form.html')
"""
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    page=read_file("page")
    new_gen_man=read_file("new_gen_man")
    fish_def=read_file("fish_def")
    guide=read_file("guide_programm")
    how_work=read_file("how_it_work")
    learn_pas=read_file("learn_pass")
    secure=read_file("secure_mer")
    return render_template("about.html",page=page,new_gen_man=new_gen_man,fish_def=fish_def,
                           guide=guide,how_work=how_work,learn_pas=learn_pas,secure=secure)



@app.route('/sorry')
def sorry():
    return render_template("sorry.html",two_k=get_image_name(locations["two_k"]),ppz=get_image_name(locations["ppz"]),
                           solrid=get_image_name(locations["solrid"]),inistra=get_image_name(locations["inistra"]),song=get_image_name(locations["song"]),
                           tera=get_image_name(locations["tera"]))

@app.route('/api_sorry', methods=['POST'])
def api_sorry():
    type=request.form.get('type')
    if type=="activate":
        location=request.form.get('location')
        name=request.form.get('name')
        locations[location]["name"]="Чекается by: "+name
        locations[location]["pos"]="1"
        return "True"
    elif type=="deactivate":
        location = request.form.get('location')
        locations[location]["name"] = "Не чекается"
        locations[location]["pos"] = "0"
        return "True"
    return "False"



@app.route('/api', methods=['POST'])
def api():
    key=request.form.get('key')
    len_=request.form.get("len")
    try:
        len_=int(len_)
    except:
        len_=20
    password=backward_trans(key,len_)
    return password



    pass
"""
@app.route('/index')
def index():
    mas=[]
    for i in range(10):
        buf={}
        buf["name"]=str(randint(10,15))
        buf["info"]=str(randint(100,150))
        mas.append(buf)
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user,
                           test="TESTING",
                           info=mas
                           )
"""


if __name__ == '__main__':
    #app.run()
    from waitress import serve

    serve(app, host="0.0.0.0", port=80)

