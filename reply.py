import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        elif message.content.startswith('bot'):
            await message.channel.send('You rang?'.format(message))

client = MyClient()
client.run('NjkxNDAwMzcyNTA1NTQyNzQ2.XnfbUA.ohxXZV3W4k8Uu-zMGQTBFvHlCGo')
