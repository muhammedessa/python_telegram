# Echo
import nmap
from telegram.ext import Updater, CommandHandler

updater = Updater(token="fffffffffffff")
dispatcher = updater.dispatcher


def command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="/scanports \n /checkstatus")
start_handler = CommandHandler("command", command)
dispatcher.add_handler(start_handler)


def scanports(bot, update):
    nm = nmap.PortScanner()
    scan_range = nm.scan(hosts="192.168.0.104")
    data = scan_range['scan']
    print(data)
    bot.send_message(chat_id=update.message.chat_id, text=data)
scanports_handler = CommandHandler("scanports", scanports)
dispatcher.add_handler(scanports_handler)



def checkstatus(bot, update):
    nm = nmap.PortScanner()
    scan_range = nm.scan('192.168.0.104', '21-443')
    for host in nm.all_hosts():
        print('Host : %s' % (host))
        print('State : %s' % nm[host].state())
    bot.send_message(chat_id=update.message.chat_id, text='Host : 192.168.0.104' + '  =>  ' + nm[host].state())
checkstatus_handler = CommandHandler("checkstatus", checkstatus)
dispatcher.add_handler(checkstatus_handler)


updater.start_polling()

