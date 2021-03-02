from pyrogram import Client as Bot
import uvicorn

@app.get('/')
return {
        'response': {Fuck you            
        }
    }

from tgcalls import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
run()

time.sleep(5)
    uvicorn.run("app", host="0.0.0.0", port=1512, log_level="info")
