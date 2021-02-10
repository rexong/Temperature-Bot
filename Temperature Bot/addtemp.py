from webscraping import myTemperatureBot
from timeNtemperature import timeNtemp
import message
import time

# create object
bot = myTemperatureBot()
tnt = timeNtemp()


def process(period):
    # load page
    bot.setUp()
    time.sleep(2)
    # check if temp is filled
    if period == "AM":
        i = 1
    else:
        i = 2
    firstRow = bot.checkHistory()
    time.sleep(2)
    print(f"[Current First Row Value] {firstRow[i]}")
    if firstRow[i] == "Nil":
        # enter pin
        bot.setPin("")
        time.sleep(2)
        # enter temp
        temp = tnt.get_temp()
        bot.setTemperature(temp)
        time.sleep(2)
        # press submit
        bot.activateSubmitBtn()
        time.sleep(2)
        # press confirm
        bot.activateConfirmBtn()
        time.sleep(2)
        # send message to my whatsapp
        message.send_message(
            f"Temperature {temp} has been updated as of {tnt.get_time()}.")
        print("[Message Sent]")
    else:
        print("[Temperature already updated]")
        message.send_message(f"Temperature has already been updated")
    bot.tearDown()


def morning():
    message.send_message("Starting AM temperature input")
    process("AM")


def afternoon():
    message.send_message("Starting PM temperature input")
    process("PM")
