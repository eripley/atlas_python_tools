#!flask/bin/python
from flask import make_response
from flask import request
import unicodedata
from flask import Flask, jsonify, g, url_for
from zgl import tasks
from idna import unicode

zaglushka = Flask(__name__)


def GenerateCookie(username):
    CookieDict = {username : "UIO"}
    return CookieDict

def filter_dictoinary(old_dict):
    return {"createdBy": old_dict["createdBy"], "createdOn" : old_dict["createdOn"], "id" : old_dict["id"], "modifiedBy": old_dict["modifiedBy"], "modifiedOn": old_dict["modifiedOn"], "state" : old_dict["state"], "taskNumber": old_dict["taskNumber"]}


@zaglushka.route('/v1/account/loginbyperson')
def get_login():
    global Cookies, username
    username = request.args.get('username')
    password = request.args.get('password')
    deviceId = request.args.get('deviceId')
    manufacturer = request.args.get('manufacturer')
    model = request.args.get('model')
    osVersion = request.args.get('osVersion')
    resolution = request.args.get('resolution')
    Cookies = GenerateCookie(username)
    print('login')
    response = make_response(tasks.login_responce)
    response.set_cookie('.ASPXAUTH', Cookies[username], expires='Sun, 22-Apr-2018 15:17:21 GMT')
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

@zaglushka.route('/v1/notifications/pushsubscribe')
def get_pushId():
    PushId = request.args.get('deviceRegistrationId')
    #response= make_response(tasks.error)
    response = make_response(tasks.pushsubscribe_responce)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Mon, 22 Jan 2018 15:17:21 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    print('pushsubscribe')
    return response

@zaglushka.route('/v1/device/register', methods=['POST'])
def get_register():
    response = make_response(tasks.registration_responce)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Mon, 22 Jan 2018 15:17:21 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    print('register')
    return response


@zaglushka.route('/v1/company')
def show_company():
    response = make_response(tasks.getcompamy_responce)
    response = make_response(tasks.error)
    #response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"           
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    print('company')
    return response, 401


@zaglushka.route('/v1/tasks', methods=['GET'])
def get_task():
    taskIds = request.args.getlist('ids')
    print (taskIds)
    if taskIds == []:
        response = make_response(tasks.big_tasks)
    else:
        response = make_response(tasks.big_tasks)
    # if taskIds is None:
    #     response= make_response(jsonify({"state": 200,"message": "Ok",'data': list((map(lambda x: filter_dictoinary(x), tasks.data)))}))
    # else:
    #     task = list(filter(lambda t: t['id'] == taskIds, tasks.data))
    #     if len(task) == 0:
    #         abort(404)
    #     response = make_response(jsonify({"state": 200,"message": "Ok",'data': task}))
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response


@zaglushka.route('/v1/tasks/setstate', methods=['PUT'])
def update_task():
    taskId = request.json[0]['Id']
    #response= make_response(tasks.error)
    response = tasks.set_state_responce
    # task = list(filter(lambda t: t['id'] == taskId, tasks.data))
    # if len(task) == 0:
    #     abort(404)
    # if not request.json:
    #     abort(400)
    # task[0]['State'] = request.json[0]['State']
    #     #request.json.get('State', task[0]['State'])
    # task[0]['modifiedOn'] = request.json[0]['CreatedOn']
    # response = make_response(jsonify({"state": 200, "message": "Ok", 'data': [task[0]['id']]}))
    return response

@zaglushka.route('/v1/maps/GetRealRoute', methods=['GET'])
def get_route():
    response = make_response(tasks.get_realroute)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

@zaglushka.route('/v1/pack', methods=['POST'])
def post_pack():
    response = make_response(tasks.post_pack)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

# @zaglushka.route('/v1/pack/PutPack', methods=['PUT'])
# def post_pack():
#     response = make_response(tasks.post_pack)
#     response.headers["cache-control"] = "no-cache"
#     response.headers["content-Type"] = "application/json; charset=utf-8"
#     response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
#     response.headers["expires"] = "-1"
#     response.headers["pragma"] = "no-cache"
#     response.headers["server"] = "Microsoft-IIS/10.0"
#     response.headers["x-aspnet-version"] = "4.0.30319"
#     response.headers["x-powered-by"] = "ASP.NET"
#     return response

@zaglushka.route('/v1/taskPredictions', methods=['POST'])
def taskPred():
    response = make_response(tasks.task_prediction)
    #response = make_response(tasks.error)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

@zaglushka.route('/v1/tasks/confirm/rating', methods=['PUT'])
def rating():
    response = make_response(tasks.confirmation)
    #response= make_response(tasks.error)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

@zaglushka.route('/v1/tasks/confirm/photo', methods=['PUT'])
def foto_confirm():
    conftype = request.args.get('confirmType')
    preview = request.args.get('preview')
    # if (conftype == "photo") and (preview == "false"):
    #     #response = make_response(tasks.error)
    #     response = make_response(tasks.confirmation)
    #     response.headers["cache-control"] = "no-cache"
    #     response.headers["content-Type"] = "application/json; charset=utf-8"
    #     response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    #     response.headers["expires"] = "-1"
    #     response.headers["pragma"] = "no-cache"
    #     response.headers["server"] = "Microsoft-IIS/10.0"
    #     response.headers["x-aspnet-version"] = "4.0.30319"
    #     response.headers["x-powered-by"] = "ASP.NET"
    #     return response
    response = make_response(tasks.confirmation)
    #response = make_response(tasks.error)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    return response

@zaglushka.route('/v1/account/Logout', methods=['GET'])
def get_logout():
    logoutdev = request.args.get('deviceId')
    response = make_response(tasks.logout_responce)
    response.headers["cache-control"] = "no-cache"
    response.headers["content-Type"] = "application/json; charset=utf-8"
    response.headers["date"] = "Thu, 09 Nov 2017 16:42:44 GMT"
    response.headers["expires"] = "-1"
    response.headers["pragma"] = "no-cache"
    response.headers["server"] = "Microsoft-IIS/10.0"
    response.headers["x-aspnet-version"] = "4.0.30319"
    response.headers["x-powered-by"] = "ASP.NET"
    print ('logout')
    return response


@zaglushka.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    zaglushka.run(debug=True, host='192.168.1.177', port=5000)

