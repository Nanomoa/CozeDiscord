import discord

from discord_core.common import config


class Channel:
    def __init__(self, client: discord.Client):
        self.client = client
        self.guild_id = config.coze_discord.guild_id

    async def create_channel(self, channel_name):
        try:
            guild = await self.client.fetch_guild(self.guild_id)
            try:
                channel = await guild.create_text_channel(channel_name)
                return channel
            except Exception as e:
                print("Failed to create channel: ", e)
                return None
        except Exception as e:
            print("Failed to get guild: ", e)
            return None

    async def delete_channel(self, channel_id):
        try:
            guild = await self.client.fetch_guild(self.guild_id)
            try:
                channel = await guild.fetch_channel(channel_id)
                try:
                    await channel.delete()
                    return True
                except Exception as e:
                    print("Failed to delete channel: ", e)
                    return False
            except Exception as e:
                print("Failed to get channel: ", e)
                return False
        except Exception as e:
            print("Failed to get guild: ", e)
            return False
