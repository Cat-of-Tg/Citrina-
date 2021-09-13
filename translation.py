class Translation(object):
    START_TEXT = """Hi! I Am Citrina 🍁
Thank you for using me 🍁
Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org

PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_ID),
parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="🍁ADD ELZA TO YOUR GROUP🍁",url="t.me/{}?startgroup=true".format(bot.username))
                    ],
                     [
                         InlineKeyboardButton(
                             text="🍁HELP🍁",
                            callback_data="help_back".format(bot.username)),
                         InlineKeyboardButton(
                             text="🍁UPDATES🍁",
                             url="https://t.me/TEAM_LAD")
                     ],
                     [
                         InlineKeyboardButton(
                             text="🍁MY CREATOR🍁",
                             url="t.me/cat_of_tg")
                     ]]))

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """I see!
Now please send the Telegram code that you received from Telegram!


/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@team_lad"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
