from telegram import Update
from telegram.ext import ContextTypes

async def function_a(update:Update, context:ContextTypes.DEFAULT_TYPE ):
    query = update.message.chat.username
    print(' - '*10)
    print(type(query))
    print(query)
    print(' - '*10)
    
    await update.message.reply_text("just replying")

'''update'''
# Update(
#     message=Message(
#         channel_chat_created=False, 
#         chat=Chat(first_name='WlthrLnrd', id=821915079, type=<ChatType.PRIVATE>, username='waltherleonardo'), 
#         date=datetime.datetime(2023, 10, 8, 5, 51, 16, tzinfo=datetime.timezone.utc), 
#         delete_chat_photo=False, 
#         from_user=User(first_name='WlthrLnrd', id=821915079, is_bot=False, language_code='en', username='waltherleonardo'), 
#         group_chat_created=False, 
#         message_id=62, 
#         supergroup_chat_created=False, 
#         text='asd'),
#     update_id=445847676)

'''update.message'''
# Message(
#     channel_chat_created=False, 
#     chat=Chat(first_name='WlthrLnrd', id=821915079, type=<ChatType.PRIVATE>, username='waltherleonardo'), 
#     date=datetime.datetime(2023, 10, 8, 5, 58, 4, tzinfo=datetime.timezone.utc), 
#     delete_chat_photo=False, 
#     from_user=User(first_name='WlthrLnrd', id=821915079, is_bot=False, language_code='en', username='waltherleonardo'), 
#     group_chat_created=False, 
#     message_id=64, 
#     supergroup_chat_created=False, 
#     text='xx')

