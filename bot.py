# DO NOT REMOVE CREDITS
# Copyright (c) 2021 Devansh20055/LINK-SHORTER
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from os import environ
import aiohttp
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', '9e34d95839fb3826358586dece7a90c8258fe823')

bot = Client('DROPLINKBOT',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "<i><u><b>I'm a specialised bot for shortening <a href=\"https://bit.ly/3pkR1ft\">droplink.co</a> .  </i></u></b>\n\n  <i><u><b> π USE /help FOR MORE π  \n\n π°πMade by @TEAM_SILENT_KING π°π. \n\n βοΈ MY DEV :- @ITS_NOT_ROMEO βοΈ \n\n β‘οΈβ‘οΈ FOR MORE OPEN SOURCE FOLLOW :- [DEVANSH20055](https://github.com/Devansh20055) \n ON GITHUB β‘οΈβ‘οΈ \n\n βΌοΈ USE /SOURCE FOR SOURCE CODE OF BOT βΌοΈ </i></u></b>", disable_web_page_preview=True )

@bot.on_message(filters.command('help') & filters.private)
async def start(bot, message):
      await message.reply(
          f"**__π»π» HeLlo {message.chat.first_name} π»π».\n Send Your Link 1stβ I Will Send Short Link π \n\n <u><b><i> π°TRY MY OTHER BOTS π°  \n\n β β α΄α΄α΄ Ιͺα΄ κ±α΄α΄Κα΄Κ Κα΄α΄ β­ β @STORE_FOR_ALL_BOT  \n\n β β α΄Κα΄α΄ΚΙͺΙ΄α΄ κ±Κα΄Κα΄ β @DROPLINK_CREATOR_BOT\n\n β β URLSHORTX β @link_shorter_op_bot \n\n  β β OTHER SHORTER β @STORE_FOR_ALL_BOT  \n\n β β Group Manager Bot β @STORE_FOR_ALL_BOT  \n\n π° Powered by [TEAM SILENT KING π°](https://t.me/team_silent_king)  \n\n β‘οΈβ‘οΈ FOR MORE OPEN SOURCE FOLLOW </u></b></i> :- [DEVANSH20055](https://github.com/Devansh20055) β‘οΈβ‘οΈ __ ",  disable_web_page_preview=True)


@bot.on_message(filters.command('source') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}! **\n\n"
        " **HERE IS THE SOURCE CODE :- \n https://github.com/Devansh20055/droplink-convertor **<i><b><u> \n\n Star β­οΈ THE REPO TOO ** \n\n π°πMade by @TEAM_SILENT_KING π°π. \n\n βοΈ MADE BY  :- @ITS_NOT_ROMEO βοΈ \n\n β‘οΈβ‘οΈ FOR MORE OPEN SOURCE FOLLOW :- [DEVANSH20055](https://github.com/Devansh20055) \n ON GITHUB β‘οΈβ‘οΈ \n\n βΌοΈ USE /SOURCE FOR SOURCE CODE OF BOT βΌοΈ </i></u></b>", disable_web_page_preview=True )




@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    links = message.text
    links = links.split("\n")
    for num in range(len(links)):
      try:
        short_link = await get_shortlink(links[num])
        await message.reply(f"<i><u>**π± Long URL:** {links[num]}</i></u> \n\n <i><u>** βοΈ Shortened URL: {short_link}\n\n πDON'T KNOW HOW TO DOWNLOAD...?π \n π° WATCH THIS VIDEO </i></u> :- https://bit.ly/33WN8Wz π° \n\nγ½οΈ<i><u> Powered by @TEAM_SILENT_KING </i></u>** " , quote=True, disable_web_page_preview=True)
      except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def get_shortlink(link):
    url = 'https://droplink.co/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


bot.run()
