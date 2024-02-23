from quart import request, jsonify, abort

from config import load_config

config = load_config()


async def before_request():
    token = request.headers.get('token')
    if not token:
        result = {'code': -1, 'message': 'proxy-secret is required.'}
        response = jsonify(result)
        abort(response)
    if token != config.coze_discord.token:
        result = {'code': -1, 'message': 'proxy-secret is invalid.'}
        response = jsonify(result)
        abort(response)


class Interceptor:
    def __init__(self, app):
        self.app = app

    def init_app(self):
        self.app.before_request(before_request)
