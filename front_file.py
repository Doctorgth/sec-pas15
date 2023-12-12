import hashlib

def has_f(s):
    md5_hash = hashlib.sha256(s.encode()).hexdigest()
    return str(md5_hash)
def sh512(s):
    md5_hash = hashlib.sha512(s.encode()).hexdigest()
    return str(md5_hash)


def forward_trans(key,base_w,place_w):
    a=has_f(key+base_w)
    b=has_f(base_w+place_w)
    c=has_f(place_w+key)
    ret=a+b+c
    ret=sh512(ret)
    return ret

def read_file(name):
    f=open("static/about_text/"+name+".txt","r",encoding="UTF-8")
    k=f.readlines()
    f.close()
    ret=""
    for i in k:
        ret+=i+" "
    return ret

def get_image_name(inp):
    name=inp["location"]
    pos=inp["pos"]
    name="static/images/sorry/"+name+"_"
    if pos=="0":
        name+="off"
    if pos=="1":
        name+="onn"
    name+=".jpg"
    inp["img"]=name
    return inp