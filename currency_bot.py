import telebot
import requests
from bs4 import BeautifulSoup


token = 'YOUR_TOKEN'
bot = telebot.TeleBot(token)

    

# _____________________
# REPLY BUTTON
reply_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
reply_button.add('قیمت دلار', 'BTCUSDT', 'ETH', 'BNB', 'SOL', 'USDC', 'XRP', 'DOGE', 'TON')

money_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
money_button.add('قیمت دلار', 'یورو', 'درهم امارات', 'پوند بریتانیا', 'لیر ترکیه', 'فرانک سوئیس', 'یوان چین',
                 'دلار کانادا' ,'افغانی')

# GLASS BUTTON
glass_button = telebot.types.InlineKeyboardButton(text='حمایت از ما🌹', url='www.google.com')
keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
keyboard.add(glass_button)

currency_btn = telebot.types.InlineKeyboardButton(text='قیمت ارزهای دیجتال💶', callback_data='btn1')
currency_btn1 = telebot.types.InlineKeyboardButton(text='قیمت واحد های پول💵', callback_data='btn2')
currency2 = telebot.types.InlineKeyboardMarkup(row_width=2)
currency2.add(currency_btn1, currency_btn)

glass_button2 = telebot.types.InlineKeyboardButton(text='مشاهده 5 ارز برتر', callback_data='see1')
glass_button1 = telebot.types.InlineKeyboardButton(text='مشاهده 5 واحد پولی برتر', callback_data='see2')


keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=2)
keyboard2.add(glass_button2, glass_button1, glass_button)

combind = telebot.types.InlineKeyboardMarkup(row_width=1)
combind.add(currency_btn1, currency_btn, glass_button)

chat_ids =[]


# START COMMAND
@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,
                 'به ربات قیمت لحظه ای رمز ارز خوش آمدید,\nبرای مشاهده ارزهای دیجیتال دستور /currency را وارد کنید \n  برای قیمت واحد های پول دستور /money را وارد کنید',
                 reply_markup=keyboard2)
    member_id=msg.chat.id
    chat =[member_id]
    if chat not in chat_ids:
        chat_ids.append(chat)
        with open('chat_id.txt',"w") as f:
            f.write(f'{chat_ids}')
            f.close()
    else:pass
# SUPPORT US COMMAND
@bot.message_handler(commands=['supportus'])
def support_us(msg):
    bot.reply_to(msg, '💳لینک حمایت مالی از ما', reply_markup=keyboard)



# CALLBCK DATA
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "see1":
            bot.send_message(call.message.chat.id,
                            "۱-بیت کوین (Bitcoin)\n 2-اتریوم (Ethereum)\n 3-بایننس کوین (Binance Coin)\n 4-تتر (Tether)\n 5-سولانا (Solana)",
                            reply_markup=currency2)

        elif call.data == "see2":
            bot.send_message(call.message.chat.id,
                            "۱-دینار کویت (KWD)\n 2-دینار بحرین (BHD)\n 3-ریال عمان (OMR)\n 4-دینار اردن (JOD)\n 5-پوند استرلینگ بریتانیا (GBP)",
                            reply_markup=currency2)

        elif call.data == 'btn1':
            bot.send_message(call.message.chat.id, ':ارز مورد نظر خود را انتخاب کنید', reply_markup=reply_button)

        elif call.data == 'btn2':
            bot.send_message(call.message.chat.id, ':ارز مورد نظر خود را انتخاب کنید', reply_markup=money_button)
        else:pass
    except:pass
# CURRENCY COMMAND
@bot.message_handler(commands=['currency'])
def currency(msg):
    bot.send_message(msg.chat.id, ':ارز مورد نظر خود را انتخاب کنید', reply_markup=reply_button)

# MONEY COMMAND
@bot.message_handler(['money'])
def money(msg):
    bot.send_message(msg.chat.id, ':ارز مورد نظر خود را انتخاب کنید', reply_markup=money_button)

# HELP COOMAND
@bot.message_handler(commands=['help'])
def help(msg):
    bot.reply_to(msg,
                 'این ربات به شما کمک میکند تا قیمت ارزها را در لحظه دریافت کنید , برای اینکار فقط کافی از دکمه های زیر استفاده کنید:\n دستور /money برای قیمت ارز ها \n دستور /currency برای قیمت ارز های دیجیتال\n دستور /support راه ارتباطی ما \n دستور /supportus برای حمایت از ما',
                 reply_markup=combind)

# SUPPORT COMMAND
@bot.message_handler(commands=["support"])
def support(msg):
    email = 'YOUR_EMAIL'
    admin = 'YOUR_USERNAME'
    bot.send_message(msg.chat.id, f'ارتباط با ما \n email: {email} \n developer :{admin}')

@bot.message_handler(commands=['proxy'])
def proxy(msg):
    a=open('proxy.txt' ,'r')
    bot.send_message(msg.chat.id,a.read())

        

# DIGITAL CURRENCY
@bot.message_handler()
def digital_currency(msg):
    try:
        if msg.text == 'قیمت دلار':
            url = 'https://www.tgju.org/profile/price_dollar_rl'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features='html.parser')
            price = soup.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'قیمت دلار به ریال:{price}')

        elif msg.text == 'BTCUSDT':

            url2 = 'https://www.tgju.org/profile/crypto-bitcoin'
            response2 = requests.get(url2).content
            soup2 = BeautifulSoup(response2, 'html.parser')
            price2 = soup2.select_one('tbody.table-padding-lg').text
            bot.reply_to(msg, f'بیت کوین : \n {price2}')

        elif msg.text == "ETH":
            url3 = "https://www.tgju.org/profile/crypto-ethereum"
            response3 = requests.get(url3).content
            soup3 = BeautifulSoup(response3, 'html.parser')
            price3 = soup3.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'اتریوم : \n {price3}')

        elif msg.text == 'BNB':
            url5 = 'https://www.tgju.org/profile/crypto-binance-coin'
            response5 = requests.get(url5).content
            soup5 = BeautifulSoup(response5, 'html.parser')
            price5 = soup5.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'بی ان بی: \n {price5}')

        elif msg.text == 'SOL':
            url6 = 'https://www.tgju.org/profile/crypto-solana'
            response6 = requests.get(url6).content
            soup6 = BeautifulSoup(response6, 'html.parser')
            price6 = soup6.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'سولانا: \n {price6}')

        elif msg.text == 'USDC':
            url7 = 'https://www.tgju.org/profile/crypto-usd-coin'
            response7 = requests.get(url7).content
            soup7 = BeautifulSoup(response7, 'html.parser')
            price7 = soup7.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'یو اس دی کوین: \n {price7}')

        elif msg.text == 'XRP':
            url8 = 'https://www.tgju.org/profile/crypto-ripple'
            response8 = requests.get(url8).content
            soup8 = BeautifulSoup(response8, 'html.parser')
            price8 = soup8.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'ریپل: \n {price8}')

        elif msg.text == 'DOGE':
            url9 = 'https://www.tgju.org/profile/crypto-dogecoin'
            response9 = requests.get(url9).content
            soup9 = BeautifulSoup(response9, 'html.parser')
            price9 = soup9.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'دوج کوین: \n {price9}')

        elif msg.text == 'TON':
            url10 = 'https://www.tgju.org/profile/crypto-toncoin'
            response10 = requests.get(url10).content
            soup10 = BeautifulSoup(response10, 'html.parser')
            price10 = soup10.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f' تون: \n {price10}')

            # ________________________________________________________________________________

        elif msg.text == 'یورو':
            url11 = 'https://www.tgju.org/profile/price_eur'
            response11 = requests.get(url11).content
            soup11 = BeautifulSoup(response11, 'html.parser')
            price11 = soup11.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'یورو به ریال: \n {price11}')

        elif msg.text == 'درهم امارات':
            url12 = 'https://www.tgju.org/profile/price_aed'
            response12 = requests.get(url12).content
            soup12 = BeautifulSoup(response12, 'html.parser')
            price12 = soup12.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'ذرهم امرات به ریال: \n {price12}')

        elif msg.text == 'پوند بریتانیا':
            url13 = 'https://www.tgju.org/profile/price_gbp'
            response13 = requests.get(url13).content
            soup13 = BeautifulSoup(response13, 'html.parser')
            price13 = soup13.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'پوند بریتانیا به ریال:\n {price13}')

        elif msg.text == 'لیر ترکیه':
            url14 = 'https://www.tgju.org/profile/price_try'
            response14 = requests.get(url14).content
            soup14 = BeautifulSoup(response14, 'html.parser')
            price14 = soup14.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'لیر ترکیه به ریال:\n {price14}')

        elif msg.text == 'فرانک سوئیس':
            url15 = 'https://www.tgju.org/profile/price_gbp'
            response15 = requests.get(url15).content
            soup15 = BeautifulSoup(response15, 'html.parser')
            price15 = soup15.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f'فرانک سوئیس به ریال : \n {price15}')

        elif msg.text == 'یوان چین':
            url16 = 'https://www.tgju.org/profile/price_cny'
            response16 = requests.get(url16).content
            soup16 = BeautifulSoup(response16, 'html.parser')
            price16 = soup16.select_one('tbody.table-padding-lg').text

            bot.reply_to(msg, f' یوان چین به ریال :\n {price16}')

        elif msg.text == 'دلار کانادا':
            url17 = 'https://www.tgju.org/profile/price_cad'
            response17 = requests.get(url17).content
            soup17 = BeautifulSoup(response17, 'html.parser')
            price17 = soup17.select_one('tbody.table-padding-lg').text
            bot.reply_to(msg, f'دلار کانادا به ریال :\n {price17}')

        elif msg.text == 'افغانی':
            url17 = 'https://www.tgju.org/profile/price_afn'
            response17 = requests.get(url17).content
            soup17 = BeautifulSoup(response17, 'html.parser')
            price17 = soup17.select_one('tbody.table-padding-lg').text
            bot.reply_to(msg, f'افغانی به ریال :\n {price17}')

        else:
            pass

    except:
        pass


bot.infinity_polling()
