import discord
from quart import Quart, request, jsonify
from quart_cors import cors

from config import load_config
from discord_core.channel import Channel
from discord_core.message import Message

intents = discord.Intents.all()
intents.messages = True

client: discord.Client

config = load_config()

if config.coze_discord.discord.proxy_url is not None and config.coze_discord.discord.proxy_url != "":
    client = discord.Client(intents=intents, proxy=config.coze_discord.discord.proxy_url)
else:
    client = discord.Client(intents=intents)

app = Quart(__name__)
app = cors(
    app_or_blueprint=app,
    allow_origin="*",
    allow_methods=["GET", "POST", "PUT", "DELETE"]
)


@app.route('/api/channel/create', methods=['POST'])
async def create_channel():
    data = await request.get_json()
    channel_name = data['channel_name']
    channel = await Channel(client).create_channel(channel_name)
    result = {}
    if channel is not None:
        result['code'] = 1
        result['message'] = 'Create channel success.'
        result['data'] = {'channel_name': channel.name, 'channel_id': channel.id}
    else:
        result['code'] = -1
        result[
            'message'] = 'Failed to create channel, please check whether the configuration file information is correct.'
    return jsonify(result)


@app.route('/api/channel/delete', methods=['POST'])
async def delete_channel():
    data = await request.get_json()
    channel_id = data['channel_id']
    success = await Channel(client).delete_channel(channel_id)
    result = {}
    if success:
        result['code'] = 1
        result['message'] = 'Delete channel success.'
    else:
        result['code'] = -1
        result['message'] = 'Delete channel failed.'
    return jsonify(result)


@app.route('/api/chat/send', methods=['POST'])
async def send_message():
    data = await request.get_json()
    message = data['message']
    channel_id = data['channel_id']
    message = await Message(client).send_message(channel_id, message)
    result = {}
    if message is not None:
        result['code'] = 1
        result['message'] = 'Send message success.'
        result['data'] = {'message': message}
    else:
        result['code'] = -1
        result[
            'message'] = 'Failed to send message, please check whether the configuration file information is correct.'
    return jsonify(result)
