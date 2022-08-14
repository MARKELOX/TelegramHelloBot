# TelegramHelloBot

This script notifies the group when a new member joins.

![Image](https://github.com/MARKELOX/TelegramHelloBot/blob/main/image.png)

<b>How to edit the welcome message??</b>

On the 4th line of code, you need to insert your API [@BotFather](https://t.me/BotFather)

<code>bot = telebot.TeleBot('token')</code>

From the 17th to the 29th line, the message is being edited

<pre language="python">
messagechat = f"""
Добро Пожаловать в чат канала <a href="t.me/URL">💢NAME💢</a> !!!
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
<i>Спасибо за то, что Вы с нами!</i>
    """</pre>

11, 12, 13 line of code edits links

<pre language="python">
    osnovgroup= types.InlineKeyboardButton("Text", url='https://url.com') #1 ссылка
    brainflayer = types.InlineKeyboardButton("Text", url='https://url.com') #2 Ссылка
    markup.add(osnovgroup, brainflayer)</pre>
   
For all questions in telegram [@MARKELOX](t.me/MARKELOX)    
  
