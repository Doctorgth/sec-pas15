import hashlib
import numpy as np
symv="qwertyuiopasdfghjklzxcvbnm"
symvU=symv.upper()
num="1234567890"
spec="!?@#$%*_=()"
types=[symv,symvU,num,spec]
def sha512(string):
    # Преобразуем строку в байтовый формат, так как hashlib ожидает байтовый ввод
    byte_string = string.encode('utf-8')

    # Создаем объект хэша
    sha512_hash = hashlib.sha512()

    # Обновляем хэш с байтовыми данными
    sha512_hash.update(byte_string)

    # Получаем хэш в шестнадцатеричном формате
    hash_result = sha512_hash.hexdigest()

    return hash_result

def md5(string):
    # Преобразуем строку в байтовый формат, так как hashlib ожидает байтовый ввод
    byte_string = string.encode('utf-8')

    # Создаем объект хэша
    sha512_hash = hashlib.md5()

    # Обновляем хэш с байтовыми данными
    sha512_hash.update(byte_string)

    # Получаем хэш в шестнадцатеричном формате
    hash_result = sha512_hash.hexdigest()

    return hash_result

def hash_to_mas(hash:str):
    ret=[]
    while len(hash)>0:
        ret.append(hash[:3])
        hash=hash[2:]
    return ret

def change_len(mas,len_):
    if len_>0 and len_<len(mas):
        while len(mas)% len_ !=0:
            mas.append(0)

        #mas=np.array(mas)
        #mas=np.array([int(x, 16) for x in mas])
        matrix = np.reshape(mas, (-1, len_))
        # Инициализируем массив для хранения поксорированных значений
        result = []

        # Выполняем поксоривание по столбцам
        for column in matrix.T:
            xored_value = np.bitwise_xor.reduce(column)
            result.append(xored_value)

        return list(result)
    mas = np.array(mas)
    mas = np.array([int(x, 16) for x in mas])
    mas=list(mas)
    return mas

def mas_type_int(mas):
    mas = np.array(mas)
    mas = np.array([int(x, 16) for x in mas])
    mas = list(mas)
    return mas


def inc_len(key):
    len_=len(key)
    a=key[:len_]
    b=key[len_:]
    ret=sha512(b)+sha512(a)
    return ret

def create_pas_key(input_key):
    key=hash_to_mas(input_key)
    key=mas_type_int(key)
    return key

def get_symvol(type_,pos):
    type_=type_ % len(types)
    mas=types[type_]
    return mas[pos % len(mas)]


def create_type_key(input_key):
    key=md5(input_key)
    key=inc_len(key)
    key=hash_to_mas(key)
    key=mas_type_int(key)
    return key

def backward_trans(key,len_):
    type_key=create_type_key(key)
    key=inc_len(key)
    pas_key=create_pas_key(key)

    type_key=change_len(type_key,len_)
    pas_key=change_len(pas_key,len_)
    ret=""
    for i in range(len_):
        ret+=get_symvol(type_key[i],pas_key[i])
    return ret

    pass
