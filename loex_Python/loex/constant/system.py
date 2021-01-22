
LOEX_URL_PRO = "https://xxxxxxxx"


LOEX_WEBSOCKET_URI_PRO = "ws://xxxxxxxx"

class WebSocketDefine:
    Uri = LOEX_WEBSOCKET_URI_PRO

class RestApiDefine:
    Url = LOEX_URL_PRO

class HttpMethod:
    GET = "GET"
    GET_SIGN = "GET_SIGN"
    POST = "POST"
    POST_SIGN = "POST_SIGN"


class ApiVersion:
    VERSION_V1 = "v1"
    VERSION_V2 = "v2"

def get_default_server_url(user_configed_url):
    if user_configed_url and len(user_configed_url):
        return user_configed_url
    else:
        return RestApiDefine.Url
