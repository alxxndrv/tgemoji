from telethon import TelegramClient, events, sync
from dotenv import dotenv_values
from random import choices, randint

STANDART_EMOJIS = ["🙏", "🥰", "😍", "🔥", "🤣", "🥺", "❤️", "✨", "😂", "😭", "😉🤙"]
QUESTION_EMOJIS = ["⁉️⁉️", "👉👈", "🥺"]


def pick_emojis(question=False):
    return "".join(choices(QUESTION_EMOJIS if question else STANDART_EMOJIS, k=randint(1, 3)))


# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = dotenv_values(".env").get('api_id')
api_hash = dotenv_values(".env").get('api_hash')

client = TelegramClient('EmojiBot', api_id, api_hash)
client.start()


@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    if event.text.endswith('?'):
        await event.edit(event.text + ' ' + pick_emojis(question=True))
    else:
        await event.edit(event.text + ' ' + pick_emojis())

client.run_until_disconnected()
