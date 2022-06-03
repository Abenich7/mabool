import pywhatkit


def send(num, msg):
    pywhatkit.sendwhatmsg_instantly(num, msg, 10, True, 1)
