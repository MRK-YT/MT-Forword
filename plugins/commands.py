#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/thewarriorsreal'),
        InlineKeyboardButton('📢Updates', url='t.me/defenderofthemultiverse'),
        InlineKeyboardButton('😎 ᥴ𝘳ꫀꪖ𝓽ꪮ𝘳', url='https://t.me/ANKIT3690'),
        Inlinekeyboardbutton(' 😎 ᥴ𝘳ꫀꪖ𝓽ꪮ𝘳', url='https://t.me/Saurav3BV6SA9LLElon7Musk'),
    ],[
        InlineKeyboardButton('🖥️ How To Own 🖥️', url='https://t.me/thewarriorsreal')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/mo_tech_Group'),
        InlineKeyboardButton('📢Updates', url='t.me/mo_tech_yt'),
        InlineKeyboardButton('🔐Close', callback_data='close_btn')
        ],[
        InlineKeyboardButton('🖥️ How To Own 🖥️', url='https://youtu.be/8kS8C9Tyvnc')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode="html")

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('🗣️Group', url='t.me/mo_tech_Group'),
        InlineKeyboardButton('📢Updates', url='t.me/mo_tech_yt'),
        InlineKeyboardButton('🔐Close', callback_data='close_btn')
        ],[
        InlineKeyboardButton('🖥️ How To Own 🖥️', url='https://youtu.be/8kS8C9Tyvnc')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode="html"
    )

        
