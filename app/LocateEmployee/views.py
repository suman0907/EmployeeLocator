from turtledemo.penrose import f

from . import test
from app import *
from flask import jsonify,request
import requests
import json



@test.route('/tes', methods=['GET'])
def tes():
    return jsonify({"msg": "welcome to employee Locator module"})



@test.route('/locate_all_employee',methods=['GET'])
def locate_all_employee():

    try:

        API_ENDPOINT = "https://n240.meraki.com/Gradeup-Noida-/n/n8pHdaWd/manage/usage/client_list_json"
        PARAMS = {'timespan': 86400}
        headers = {'Cookie':'_session_id_for_n240=fd02a826d90f10090760f6ecd699a486;dash_auth=MG67Kk8LoO4OQ28MOh.hPnM2LZdPi-0hJFZz8D2YihTjODceLaoSdZ4GXp7cW2Kpl3bYbvYwPqohRbgCsq5rYKkzHb_iqKfe-rNE-4ZRGRjDKSLu2Bb51etj9W3aWZMdTwGQ1yBnTmGxi3J-Iv5Np0wxhbaUP-gM7vIQz_7-LKxZ9a7K3KjdCr33B7qgGui9hg751CerzAW21TC_mbUFjFYyAygtqsr9_FyZAPCHK8AqEGZ3t13DZCFdB0oBSxpfr_5fqP8v9mt1KpNrKVyUx3Wn1kaBs8nbjZzggKFyUg0tF9f7ERjahEBR2h06DbdRrsS0NvduVeZOQ.ceMdCAmrGj6Qi_s1WFMyKw'}
        r = requests.get(url=API_ENDPOINT,params = PARAMS,headers=headers)

        result = r.json()
        temp_result = []

        for i in result['clients']:
            res = {}
            res['description'] = i[1]
            res['access point'] = i[2]
            res['ip'] = i[7]
            res['OS'] = i[10]
            res['mac address'] = i[14]
            temp_result.append(res)


        return jsonify({"data": temp_result})
    except Exception as e:
        print (str(e))
        return jsonify({"response": "failure", "error": str(e)})



@test.route('/locate_employee',methods=['GET'])
def locate_employee():
    search = request.args["device"]

    try:

        API_ENDPOINT = "https://n240.meraki.com/Gradeup-Noida-/n/n8pHdaWd/manage/usage/client_list_json"
        PARAMS = {'timespan': 86400}
        headers = {'Cookie':'_session_id_for_n240=fd02a826d90f10090760f6ecd699a486;dash_auth=MG67Kk8LoO4OQ28MOh.hPnM2LZdPi-0hJFZz8D2YihTjODceLaoSdZ4GXp7cW2Kpl3bYbvYwPqohRbgCsq5rYKkzHb_iqKfe-rNE-4ZRGRjDKSLu2Bb51etj9W3aWZMdTwGQ1yBnTmGxi3J-Iv5Np0wxhbaUP-gM7vIQz_7-LKxZ9a7K3KjdCr33B7qgGui9hg751CerzAW21TC_mbUFjFYyAygtqsr9_FyZAPCHK8AqEGZ3t13DZCFdB0oBSxpfr_5fqP8v9mt1KpNrKVyUx3Wn1kaBs8nbjZzggKFyUg0tF9f7ERjahEBR2h06DbdRrsS0NvduVeZOQ.ceMdCAmrGj6Qi_s1WFMyKw'}
        r = requests.get(url=API_ENDPOINT,params = PARAMS,headers=headers)

        result = r.json()
        temp_result = []

        for i in result['clients']:

            if i[1]==search:
                return jsonify({"The employee is connected to the access point": i[2]})


        return jsonify({"msg": "No employee found with such name"})

    except Exception as e:
        print (str(e))
        return jsonify({"response": "failure", "error": str(e)})
