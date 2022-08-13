from rich import print
import telebot
from telebot import types, util


#from config import messagechat

bot = telebot.TeleBot('token')
    
@bot.message_handler(content_types=['new_chat_members']) #Создаем функцию когда при заходе выполняется функция
def start(message):
    markup = types.InlineKeyboardMarkup()
    osnovgroup= types.InlineKeyboardButton("Основная группа", url='https://t.me/brythbit') #1 ссылка
    brainflayer = types.InlineKeyboardButton("Как пользоваться BrainFlayer", url='https://t.me/brythbit/189') #2 Ссылка
    markup.add(osnovgroup, brainflayer)
    mention = f'[{message.from_user.first_name}](tg://user?id={message.from_user.id})' #Это ссылка на имя человека который зашёл
    #===============================Это всё текст =======================
    messagechat = f"""
    Добро Пожаловать в чат канала <a href="t.me/brythbit">💢COIN BRUTE💢</a> !!!
    {mention}
<b>Предупреждение/Бан:</b>
1. Обсуждение политики
2. Оскорбление собеседника или администрации
3. Реклама
4. Пропаганда
5. 18+
6. Наркотики
7. Неуважительное отношение к людям (НЕ ЗВОНИТЬ И НЕ РЫГАТЬ В ТРУБКИ)
8. Выдавать себя за админа (любого)

<i>Спасибо за то, что Вы с нами!
По вопросам и улучшению писать <a href="t.me/xopmc">
💪XopMC💪
</a><a href="t.me/Szatan0">💥Szatan0💥
</a><a href="t.me/lordix_badaboom">🔥Lordix_badaboom🔥
</a><a href="t.me/markelox_off">✨ЖМЫХ✨
</a></i>
    """
#======================================================================

    bot.send_message(message.chat.id, messagechat, parse_mode="HTML", reply_markup=markup) #отправка сообщения в телеграм

#======================Удаление сообщение о выходе из группы ============

@bot.message_handler(content_types=util.content_type_service)
def delall(message: types.Message):
    bot.delete_message(message.chat.id, message.message_id)

#======================================================================
if __name__ == '__main__':
    bot.infinity_polling(allowed_updates=util.update_types)