import asyncio
import io
import os
import json

import nest_asyncio

# import logging  <---- telegram
from telegram import Update
from telegram.ext import filters, Application, CommandHandler, MessageHandler, ContextTypes

from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.http.request_options import RequestOptions
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files import file

nest_asyncio.apply()

# from openpyxl import load_workbook

import pandas as pd

SITEURL="https://panamotorssac-my.sharepoint.com/personal/pyanaura_panaautos_com_pe"
FILE_URL="/Documents/Reporte%20%20Modelo%20Retail%20&%20Wholesale%20de%20Ventas%202022.xlsx"
PASSWORD="Panaautos2023"
USERNAME="wrojas@panaautos.com.pe"
TOKEN="6528642672:AAEBweExhh5x5jZCkQEzVkrRyi6k6gIc1Ic"

# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# logging.getLogger("httpx").setLevel(logging.WARNING)
'''core Sharepoint Functions'''
''' ------------------------------------------------------------------------------------------------------------------'''
# sharepoint core login
async def loging():
    username=USERNAME
    password=PASSWORD
    site_url=SITEURL
    file_url=FILE_URL
    ctx = ClientContext(site_url).with_credentials(UserCredential(f"{username}", f"{password}"))
    
    request = RequestOptions("{0}/_api/web/".format(site_url))
    response = ctx.pending_request().execute_request_direct(request)
    ajson = json.loads(response.content)
    web_title = ajson['d']['Title']
    print(web_title)

    ctx.load(ctx.web)
    ctx.execute_query()

    # response = file.File.open_binary(ctx, file_url)   
    # response = ctx.web.get_file_by_server_relative_url(file_url).open_binary(ctx, file_url)
    # response = ctx.web.get_file_by_server_relative_url(file_url)
    # with open(file=file_url ,mode="rb"):
    # response = ctx.web.get_file_by_guest_url(file_url).open_binary(ctx, file_url)
    # response = file.File.open_binary(ctx, file_url)
    # # bytes_file_obj=io.BytesIO()
    # # bytes_file_obj.write(response.content)
    # # bytes_file_obj.seek(0)
    # bytes_file_obj=io.BytesIO(response.content)
    # bytes_file_obj.seek(0)
    # print(type(bytes_file_obj))
    # wb =  load_workbook(bytes_file_obj)
    # df = pd.read_excel(bytes_file_obj)

    response = file.File.open_binary(ctx, file_url)
    bytes_file_obj = io.BytesIO()
    bytes_file_obj.write(response.content)
    bytes_file_obj.seek(0) #set file object to start
    df = pd.read_excel(bytes_file_obj.read(), engine='openpyxl')

    return df
''' ------------------------------------------------------------------------------------------------------------------'''


'''data Functions'''
''' ------------------------------------------------------------------------------------------------------------------'''
# loging
async def log():
    await loging()
    # return ctx
# downloads
# async def down(ctx):
#     await download(ctx)

# work data



''' ------------------------------------------------------------------------------------------------------------------'''


'''Bot Functions'''
''' ------------------------------------------------------------------------------------------------------------------'''
application = Application.builder().token(TOKEN).build()

async def ventasSI(update:Update, context:ContextTypes.DEFAULT_TYPE ):
    fileobject = asyncio.run(log())
    # asyncio.run(down(contexto))
    print(' - '*10)
    print(type(fileobject))
    print(' - '*10)
    await update.message.reply_text("option a chosen")

async def ventasSM(update:Update, context:ContextTypes.DEFAULT_TYPE ):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="option b chosen")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry,I didn't understand that command")
''' ------------------------------------------------------------------------------------------------------------------'''


admin_a = CommandHandler('ventassi', ventasSI)
admin_b = CommandHandler('ventassm', ventasSM)
unknown_handler = MessageHandler(filters.COMMAND, unknown)
application.add_handler(admin_a)
application.add_handler(admin_b)
application.add_handler(unknown_handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)




