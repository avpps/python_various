import time
import datetime
import json
import random
from string import hexdigits as hd
from pprint import pprint as pp

file_path = 'sample.txt'

users = 40
sessions = 30
fro_r = 2
deb_r = (20, 40)
bac_r = (0, 15)
cont_l = 3000

attr_ext = 10
attr_ext_cont = 20


attributes = [
    'user_id',
    'sess_id',
    'req_id',
    'req_name',
    'obj_type',
    'str_cont',
    'json_cont',
]

attributes_ext = ['sample_attr_{}'.format(i) for i in range(attr_ext)]

req_names = [
    'sign_up',
    'login',
    'get_info',
    'send_message',
    'get_response',
    'logout',
]

obj_types = [
    ['fff', 2],
    ['ddd', random.randrange(deb_r[0], deb_r[1], 1)],
    ['bbb', random.randrange(bac_r[0], bac_r[1], 1)],
]

objects = list()


def _gen_sample_str_cont(datetime, user_id, sess_id, req_id, req_name, obj_type):
    a = ''.join((random.choice(hd) for i in range(cont_l)))
    b = ''.join((random.choice(hd) for i in range(cont_l)))

    return a + '\n {}\n {}\n {}\n {}\n {}\n {}\n'.format(
        datetime, user_id, sess_id, req_id, req_name, obj_type) + b


def _gen_sample_str(length):
    return ''.join((random.choice(hd) for i in range(length)))


def _gen_sample_json_cont(datetime, user_id, sess_id, req_id, req_name, obj_type):
    return dict(details='\n {} {} {} {} {} {} \n'.format(
                         datetime, user_id, sess_id, req_id, req_name, obj_type),
                other='agasfdgsds',
                sth_else='asafaagahethtearf')


with open(file_path, 'w') as file:
    file.close()

dt = datetime.datetime.now()
counter = 0
with open(file_path, 'a') as file:
    for u in range(users):
        print(u, counter)
        user_id = random.randrange(1000, 9999, 1)
        dt = dt + datetime.timedelta(hours=random.random(), seconds=random.random())
        for s in range(sessions):
            dt = dt + datetime.timedelta(hours=random.randrange(-1000, 1000, 1)/100)
            sess_id = 'S_' + ''.join((random.choice(hd) for i in range(15)))
            for req_name in req_names:
                dt = dt + datetime.timedelta(minutes=random.randrange(-1000, 1000, 1) / 100)
                req_id = 'R_' + ''.join((random.choice(hd) for i in range(8)))
                for o in obj_types:
                    obj_type = o[0]
                    for o_c in range(o[1]):
                        head = dict(
                            datetime=str(dt),
                            user_id=user_id,
                            sess_id=sess_id,
                            req_id=req_id,
                            req_name=req_name,
                            obj_type=obj_type)
                        head.update({n: _gen_sample_str(attr_ext_cont) for n in attributes_ext})
                        head = ' '.join('{}:{}'.format(k, v) for k, v in head.items())
                        head = '[' + head + ']' + '\n'

                        if o[0] == 'fff':
                            json_cont = _gen_sample_json_cont(dt, user_id, sess_id, req_id, req_name, obj_type)
                            cont = json.dumps(json_cont, indent=4)
                        else:
                            str_cont = _gen_sample_str_cont(dt, user_id, sess_id, req_id, req_name, obj_type)
                            cont = str_cont
                        cont = str(cont)

                        file.write(head + cont + '\n\n')
                        counter += 1


print('Object items count: ', counter)
