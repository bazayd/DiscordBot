# Imports OS module
import os

from discord.ext.commands import bot
# Import load_dotenv function from dotenv module
from dotenv import load_dotenv

# Imports Discord.PY, allows access to discord's API
import discord

# Loads the .env file that resides on the same level as the script.
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
GEN_CHANNEL = int(os.getenv("DISCORD_GEN_CHANNEL"))
QUESTION_CHANNEL = int(os.getenv("DISCORD_QUES_CHANNEL"))


class BotClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guild = None

    #
    # #Event listener for bot going form offline to online
    # @bot.event
    async def on_ready(self):
        for guild in self.guilds:
            if guild.name == GUILD:
                break

            print(f"{self.user} is connected to the following guild")
            print(f"{guild.name}, {guild.id}")
        # # Keeps track of how many servers/guils the bot is connected to
        # guild_count = 0
        #
        # # Iterates through all bot guilds
        # for guild in bot.guilds:
        #     # prints server's ID and name
        #     print(f"- {guild.id} (name: {guild.name})")
        #
        #     # increments guild count to move onto the next
        #     guild_count = guild_count + 1
        #
        # # Prints out how many guilds the bot is in (String)
        # print("ZaydsBot is in " + str(guild_count) + " guilds.")

    # event listener for when a new message is sent to the channel
    async def on_message(self, message):
        if message.content == "hello":
            await message.channel.send("Hello bro.")
            print("Message Sent")

    async def on_member_join(self, member):
        channel = await self.fetch_channel(GEN_CHANNEL)
        embed = discord.Embed(title="Welcome!", description=f"{member.mention} Just Joined")
        await channel.send(embed = embed)


def main():
    # Client object from discord.py library, synonymous with bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = BotClient(intents=intents)
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
