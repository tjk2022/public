# -------------------------------------------------------
#coder :- KC 22.2.2023
# -------------------------------------------------------
import subprocess
import datetime
import argparse
import sys
import time
#import random
import datetime
import telepot
import sys
import urllib
#import CStringIO
#from PIL import Image
import requests
from io import BytesIO

# ----------------------------------------------------------------                
# --- Functions
# ----------------------------------------------------------------

# -------------------------------------------------------
#
# -------------------------------------------------------


# -------------------------------------------------------
def wlanstatus():
        parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
        parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
        args = parser.parse_args()

        print("*** WLAN Status asked.")

#        while True:
# note: using shell=True can be a security hazard!!         
        cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
        for line in cmd.stdout:
                if 'Link Quality' in line:
                        return line.lstrip(' ')
                        qual = line.lstrip(' ')	
                        f = qual.find("=")
                        if f > 0:
                                if int(qual[f+1]) < 5:
                                        return '**** Warning: WLAN Link quality is low. ***'
                elif 'Not-Associated' in line:
                        return 'No signal'
#            time.sleep(50)
# ----------------------------------------------------------------
# --- WLAN Quality 
# ----------------------------------------------------------------
def wlan_quality():
        parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
        parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
        args = parser.parse_args()

# note: using shell=True can be a security hazard!!         
        cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
        for line in cmd.stdout:
                if 'Link Quality' in line:
                        qual = line.lstrip(' ')	
                        f = qual.find("=")
                        if f > 0:
                                return int(qual[f+1])
                        else:
                                return -1
                elif 'Not-Associated' in line:
                        return -1

# ----------------------------------------------------------------
# --- Send Images to Telegram client
# ----------------------------------------------------------------
def send_images():

        print ('=== Sending image 1.')


        print ('=== Sending image 2.')


        print ('=== Sending image 3.')


        print ('=== Sending image 4.')

        try:
                response = requests.get("http://luumupuu.asuscomm.com:1997/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&amp;usr=adminopticam&amp;pwd=tjkooo77Oax")
        except Exception as e:
                bot.sendMessage(chat_id, "==4= Error: %s" % str(e))

        print ('=== Sending image 5.')
        # ----------------------------------------------------------------
        # --- WLAN
        # ----------------------------------------------------------------
        try:
                response = requests.get("http://luumupuu.asuscomm.com:1994/cgi-bin/CGIProxy.fcgi?cmd=refreshWifiList&usr=adminopticam&pwd=tjkooo44Oax")
                data = (response.text)
                print ("*** data %s" % str(data))
                # --- bot.sendMessage(chat_id, str(data))
        except Exception as e:
                bot.sendMessage(chat_id, "==5= Error: %s" % str(e))
        try:
                response = requests.get("http://luumupuu.asuscomm.com:1994/cgi-bin/CGIProxy.fcgi?cmd=getWifiList&startNo=0&usr=adminopticam&pwd=tjkooo44Oax")
                data = (response.text)
                # --- print ("*** data %s" % str(data))
                # --- bot.sendMessage(chat_id, str(data))
                data =  data.replace("%2B", " ", 1)
                data =  data.replace("%2B", "-", 3)
                data =  data.replace("%3A", ":")
                data =  data.replace("%2B", " ", 1)
                data =  data.replace("%2B", "-", 3)
                data =  data.replace("%3A", ":")

                bot.sendMessage(chat_id, str(data))
        except Exception as e:
                bot.sendMessage(chat_id, "==6= Error: %s" % str(e))
        return
# ----------------------------------------------------------------
# --- Global variables (defined in handle-method)
# ----------------------------------------------------------------
update_id       = 0
current_msg_text =""
chat_id_notify =""
global chat_id
updates =""
updates_found = 0    

bot_wlan_notify = 0
update_id       = 0
chat_text       = ''

bot=""
username=""

# -------------------------------------------------------
# --- S T A R T
# -------------------------------------------------------

try:
        bot = telepot.Bot("5465711240:AAGNeCliWiInJO1TL_gM74Z5ZJyLcSubgh8")
        
        print("Guardbot v20220913 is starting..")
except Exception as e:
        print ("--- Error: %s \n" % str(e))

my_user = bot.getMe()

username = my_user['username']
print ('=== first_name: ' + my_user['first_name'])
print ('=== username:   ' + my_user['username'])
print ('=== id:         ' + str(my_user['id']))

while 1:
        #  --- the last uread message
        update_id = 0
        chat_id = 0
        updates_found = 0
        updates=""
        
        try:
                updates = bot.getUpdates()
        except Exception:
                print ('--- error: getupdates')
             
        if updates:
                print ('--- updates found')
                try:
                        update_id   = updates[-1]['update_id']
                        chat_id     = updates[-1]['message']['chat']['id']
                        chat_text   = updates[-1]['message']['text']
                        print ('--- Message updates found, msg_id: ' + str(chat_id))
                        bot.getUpdates(offset = update_id + 1)
                        updates_found = 1
                except Exception as e:
                        update_id = 0
                        updates_found = 0
                        chat_id = 0
                        print ('--- Failed to read a message')
        else:
                chat_id = 0
        # ----------------------------------------------------------------
        # ---
        # ----------------------------------------------------------------
        if chat_id == 0:
                print ('--- Nothing to read')
        else:
                print ('--- Request found')
                print ("--- Request: %s" % str(chat_text)) 

                try:
	        	# ----------------------------------------------------------------
	        	# --- Sending images to client
       			# ----------------------------------------------------------------
                        send_images()
                except Exception as e:
                        print ("--99- Error: %s \n" % str(e))

        time.sleep(20)
        
        
# ----------------------------------------------------------------  

