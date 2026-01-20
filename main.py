import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

import pyrogram.utils
pyrogram.utils.MIN_CHANNEL_ID = -1002275431283

from bot import Bot

if __name__ == "__main__":
    Bot().run()
