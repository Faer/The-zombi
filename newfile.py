import telebot
from telebot import types
import datetime

password = False

one_one = "Пусто"
one_two = "Пусто"
one_tree = "Пусто"
one_four = "конспект по § и вопросы стр 79"
one_five = "Пусто"
one_six = "§ 46,47; упр 29"
one_seven = "№ 426, 430, 432, 434, 436"

two_one = "§ антарктида"
two_two = "Простите я не написал"
two_tree = "Пусто"
two_four = "Пусто"
two_five = "Пусто"
two_six = "Пусто"
two_seven = "§"

tree_one = "Пусто"
tree_two = "Пусто"
tree_tree = "Пусто"
tree_four = "Пусто"
tree_five = "Пусто"
tree_six = "Пусто"
tree_seven = "2 группа- №3,7 стр 74"

four_one = "Пусто"
four_two = "Пусто"
four_tree = "Пусто"
four_four = "Пусто"
four_five = "Инф- №188-191 в старых"
four_six = "Пусто"
four_seven = "Пусто"

five_one = "Пусто"
five_two = "Пусто"
five_tree = "Пусто"
five_four = "Пусто"
five_five = "Пусто"
five_six = "Пусто"
five_seven = "Пусто"

time = datetime.datetime.now()

bot = telebot.TeleBot("6972454180:AAFtlNy5XTQnuRSdTq1OpX3BM5hSaqIfK8g")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    
    btn1= types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    btn6 = types.KeyboardButton("Полное расписание без дз")
    
    markup.row(btn1,btn2,btn3)
    markup.row(btn4,btn5,btn6)
    
    bot.send_message(message.chat.id,"Здравствуйте, выберите день.",reply_markup=markup)

@bot.message_handler()
def nedela(message):
            
    if message.text.lower() == "понедельник":
            bot.send_message(message.chat.id,f"Уроки на понедельник 📚:\n\n""Разговоры о важном -- "+one_one+"\n""Русский язык -- "+one_two+"\n""Литература -- "+one_tree+"\n""Музыка/ОДНК -- "+one_four+"\n""Физра -- "+one_five+"\n""Физика -- "+one_six+"\n""Алгебра -- "+one_seven)
            print(f"{message.from_user.first_name} {message.from_user.last_name} Понедельник",time)
            
    if message.text.lower() == "вторник":
            bot.send_message(message.chat.id,"Уроки на вторник 📚:\n\n""География -- "+two_one+"\n""Геометрия -- "+two_two+"\n""Физра -- "+two_tree+"\n""Технол/ИЗО -- "+two_four+"\n""Физика -- "+two_five+"\n""Вероят и стат -- "+two_six+"\n""Обществ -- "+two_seven)
            print(f"{message.from_user.first_name} {message.from_user.last_name} Вторник",time)
            
    if message.text.lower() == "среда":
            bot.send_message(message.chat.id,"Уроки на среду 📚:\n\n""Класный час -- "+tree_one+"\n""Родная литра -- "+tree_two+"\n""Алгебра -- "+tree_tree+"\n""Биология -- "+tree_four+"\n""Русский -- "+tree_five+"\n""Технология -- "+tree_six+"\n""Англ.яз -- "+tree_seven+"\n")
            print(f"{message.from_user.first_name} {message.from_user.last_name} Среда",time)
            
    if message.text.lower() == "четверг":
            bot.send_message(message.chat.id,"Уроки на четверг 📚:\n\n""Рос.мои.гор. -- "+four_one+"\n""Русский -- "+four_two+"\n""География -- "+four_tree+"\n""Англ/Инфо -- "+four_four+"\n""Инфо/Англ -- "+four_five+"\n""История -- "+four_six+"\n""Геометрия -- "+four_seven+"\n")
            print(f"{message.from_user.first_name} {message.from_user.last_name} Четверг",time)
            
    if message.text.lower() == "пятница":
            bot.send_message(message.chat.id,"Уроки на пятницу 📚:\n\n""Родной русс -- "+five_one+"\n""Русский -- "+five_two+"\n""Алгебра -- "+five_tree+"\n""Башкирский -- "+five_four+"\n""Литер -- "+five_five+"\n""История --  "+five_six+"\n""Англ -- "+five_seven+"\n")
            print(f"{message.from_user.first_name} {message.from_user.last_name} Пятница",time)
            
    if message.text.lower() == "полное расписание без дз":
            bot.send_message(message.chat.id,"Понедельник:\n\nРусский язык 211\nЛитература 211\nМузыка 412/ОДНК 412\nФизическая культура\nФизика 320\nАлгебра 307\n\nВторник:\n\nГеография 301\nГеометрия 307\nФизическая культура\nТехнология 301 /ИЗО 401\nФизика 320\nВероятность и статистика 307\nОбществознание 227\n\nСреда:\n\nКлассный час 211\nРодная литература 211/322\nАлгебра 307\nБиология 102\nРусский язык 211\nТехнология 301\nАнглийский язык 309/315\n\nЧетверг:\n\nРоссия мои горизонты 211\nРусский язык 211\nГеография 301\nАнгл. язык 315/Информ. 311\nИнформ. 311/Английский жык 305\nИстория 227\nГеометрия 307\nРодной клик 211/322\n\nПятница:\n\nРодной русс 211\nРусский язык 211\nАлгебра 307\nБашкирский язык 214/322\nЛитература 211\nИстория 227\nАнгл.яз 315")
            print(f"{message.from_user.first_name} {message.from_user.last_name} Полное расписание без дз",time)

bot.polling(none_stop=True,interval=0)