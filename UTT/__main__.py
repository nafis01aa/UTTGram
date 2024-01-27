from pyrogram.handlers import MessageHandler

from UTT import bot, bot_start, bot_loop, bot_username, bot_scheduler, logger

async def start(_, message):
    user_id = message.from_user.id
    text = (
        f'**I am UTTGram Telegram Bot.**\n'
        f'**I can communicate between admins and users.**\n'
        f'**To use my services, you have to connect your bot with my server.**\n\n'
        f'To connect, please use /connect bot_token: where bot_token is the http authorization token of your bot get by @BotFather'
    )
    await message.reply(text, disable_web_page_preview=True)

async def connect(_, message):
    if len(message.command) < 2:
        await message.reply('**You will have to provide a bot token along with the command /connect to connet your bot with my server and use communication service.**')
        return

    bot_token = message.command[1]
    if ':' not in bot_token:
        await message.reply('**Sorry, the bot token you provided is not a valid token from @BotFather**')
        return

    h

async def main():
    logger.info("UTTGram has been started! ☠️")

bot_loop.run_until_complete(main())
bot_loop.run_forever()
