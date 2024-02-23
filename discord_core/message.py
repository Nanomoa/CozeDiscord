import json

import discord
import requests

from discord_core.common import config


class Message:
    def __init__(self, client: discord.Client):
        self.client = client
        self.guild_id = config.coze_discord.guild_id
        self.target_bot_id = config.coze_discord.target_bot_id
        self.user_id = config.coze_discord.user.id
        self.user_authorization = config.coze_discord.user.authorization

    def check_reply(self, message):
        user = self.client.get_user(self.user_id)
        if message.author == user:
            return False
        if message.reference and message.reference.resolved:
            original_message = message.reference.resolved
            if original_message.author == user and message.author.id == int(
                    self.target_bot_id):
                return True
        return False

    async def create_msg(self, channel_id, content):
        content = content.replace("\\u0026", "&")

        try:
            request_body = json.dumps({"content": content})
        except json.JSONDecodeError as e:
            print("Error encoding request body:", e)
            return None

        formatted_post_url = f"https://discord.com/api/v9/channels/{str(channel_id)}/messages"

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.user_authorization,
            "Origin": "https://discord.com",
            "Referer": f"https://discord.com/channels/{str(self.guild_id)}/{str(channel_id)}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }

        try:
            response = requests.post(formatted_post_url, headers=headers, data=request_body)
            response.raise_for_status()
        except requests.RequestException as e:
            print("Error sending request:", e)
            return None

        try:
            result = response.json()
            msg_id = result.get("id")
            print(f"Message id: {msg_id}")
            try:
                channel = await self.client.fetch_channel(channel_id)
                try:
                    msg = await channel.fetch_message(msg_id)
                    return msg
                except Exception as e:
                    print("Error fetching message:", e)
                    return None
            except Exception as e:
                print("Failed to get channel: ", e)
                return None
        except json.JSONDecodeError as e:
            print("Error decoding the response body:", e)
            return None

    async def get_reply(self, channel):
        def check_edit(before, after):
            return before.channel == channel and before.author.id == self.target_bot_id and before.content == after.content

        try:
            _, msg = await self.client.wait_for('message_edit', check=check_edit, timeout=180)

            content = msg.content
            embeds = msg.embeds

            image_urls = [embed.image.url for embed in embeds if embed.image]
            md_image_links = '\n'.join(f"![Embedded Image]({url})" for url in image_urls)
            full_message = content + '\n\n' + md_image_links if md_image_links else content

            return full_message
        except Exception as e:
            print("Error waiting for reply message: ", e)
            return None

    async def send_message(self, channel_id, content):
        try:
            target_bot = await self.client.fetch_user(self.target_bot_id)
            channel = await self.client.fetch_channel(channel_id)
            content = f'{target_bot.mention} ' + content
            try:
                msg_sent = await self.create_msg(channel_id, content)
                if msg_sent is not None:
                    try:
                        await self.client.wait_for('message', check=self.check_reply, timeout=180)
                        reply_msg = await self.get_reply(channel)
                        return reply_msg
                    except Exception as e:
                        print("Error wait for reply message:", e)
                        return None
            except Exception as e:
                print("Error sending message: ", e)
                return None
        except Exception as e:
            print("Failed to get target bot or channel: ", e)
            return None
