import discord
import configparser

Token = "token"

client = discord.Client()

config = configparser.ConfigParser()

config['SETTINGS'] = {
    'DeleteNotification': 'on'
}
with open('config.ini', 'w') as file:
    config.write(file)


@client.event
async def on_ready():
    print("ログインしました。")


@client.event
async def on_message_delete(message):
    if message.author.bot:
        return

    config.read('sample/config.ini')

    if config['SETTINGS']['DeleteNotification'] == "on":
        message_text = (str(message.author) + " さんが、メッセージを削除しました。")
        message_content = ("    内容：「" + message.content + "」")
        await message.channel.send(message_text + message_content)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Config関連設定
    if message.content == "/config delete on":
        if config['SETTINGS']['DeleteNotification'] == "off":
            config['SETTINGS'] = {
                'DeleteNotification': 'on'
            }
            with open('config.ini', 'w') as file:
                config.write(file)

            await message.channel.send("DeleteMessageNotificationをONにしました。")

        if config['SETTINGS']['DeleteNotification'] == "on":
            await message.channel.send("DeleteMessageNotificationはすでにONです")

    if message.content == "/config delete off":
        if config['SETTINGS']['DeleteNotification'] == "off":
            await message.channel.send("DeleteMessageNotificationはすでにOFFです")

        if config['SETTINGS']['DeleteNotification'] == "on":
            config['SETTINGS'] = {
                'DeleteNotification': 'off'
            }
            with open('config.ini', 'w') as file:
                config.write(file)

            await message.channel.send("DeleteMessageNotificationをOFFにしました。")



client.run(Token)
