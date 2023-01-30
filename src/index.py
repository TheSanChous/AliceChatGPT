from .common import configuration, storage
from .query_processor import create_query
from datetime import datetime
from json import dumps
from threading import Thread


def handler(request, context):
    response = {
        "response": {},
        "session": request['session']['session_id'],
        "version": request['version']
    }
    try:
        if request["request"]["original_utterance"] is "":
            response["response"]['text'] = configuration["commands"]["greetings"]
            return dumps(response)
        if request["request"]["command"] in configuration["commands"]["GetResultCommands"]:
            if request["state"]["session"] in [{}, {"last_request_key": None}]:
                response["response"]['text'] = configuration["responses"]["request_list_empty"]
                return dumps(response)
            last_request_key = request["state"]["session"]["last_request_key"]
            result = storage.get(last_request_key)
            if result is None:
                response["response"]["text"] = configuration["responses"]["request_in_process"]
                response.update({"session_state": {"last_request_key": last_request_key}})
            else:
                response["response"]["text"] = result.decode("utf-8")
                response.update({"session_state": {"last_request_key": None}})
            return dumps(response)
        current_request_key = str(datetime.now())

        query_thread = Thread(target=create_query, args=(request["request"]["original_utterance"], current_request_key))

        query_thread.start()

        response.update({"session_state": {"last_request_key": current_request_key}})
        response["response"]["text"] = configuration["responses"]["request_created"]
    except Exception:
        response["response"]["text"] = configuration["responses"]["internal_error"]
    return dumps(response)
