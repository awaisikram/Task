####################################################################################################
#This script has been written to check the availability of Zabbix server and Zabbix server components
#In case of any error, this script will inform the system-adminstrator via telegram notification

#NOTE: actual IP-address , web url and telegram id is not mentioned here because of confidentiality. 
#####################################################################################################

#!/usr/bin/env python

import os

# "pirl" function has 2 checks.PING and CURL 
#ping response checks availability of zabbix server and curl response checks from inside zabbix web UI status of zabbix server.

def pirl():
    out1=int(os.popen("ping 123.123.123.123 -c 8 | grep 'received' | awk ' { print $4} ' " ).read())
    out2=os.popen("curl -s -k  --location --request GET 'https://example.com/zabbix.php?sid=82c28951e06a504a&action=widget.systeminfo.view' --header 'Cookie: PHPSESSID=f07fa83587d7jdc6ced5k40aad1d5ed7; zbx_sessionid=7c600e85f56bd8507hd84ed8511afd54' | grep 'Zabbix' | awk ' { print $8 } ' | rev | cut -c 64- | rev | cut -c 12-").read()
    if out1>2 and "Yes" in out2:
        return "successful"
    elif out1>2 and "No" in out2:
        return "Zabbix Server is Down"
    else:
        return "Other error in Zabbix server"

# "nginxcheck" function checks the availability of web server

def nginxcheck():
    out3=os.popen("curl -s -k https://example.com/ | grep 'No server is available' ").read()
    if "No server is available" in out3:
        return "No server is available to handle this request."
    else:
        return "Other Error"

# "dbcheck" fucntion checks MySQL database availability.

def dbcheck():
    out4=os.popen("curl -s -k https://example.com/ | grep 'connecting to database' | awk ' { print $11,$12,$13,$14} ' ").read()
    if "Can't connect to MySQL" in out4:
        return "Can't connect to MySQL"
    else:
        return "other DB Error"

#calling functions, server, web, or db according to the check

server=pirl()
web=nginxcheck()
db=dbcheck()

#conditions check 
if "successful" in server:
    print(server)
	
elif "Zabbix Server is Down" in server:
    print(server)
	# sending notification to telegram if zabbix server has issue
    os.system("curl -s -X POST https://api.telegram.org/bot1756020946:AAH5hj2QjeWAb9jhd--PevNCJTsy06AvdK8/sendMessage -d chat_id=971998000 -d text='Zabbix Server Problem:Zabbix Server is Down' ")
	
elif "No server is available to handle this request." in web:
    print(web)
    # sending notification to telegram if nginx web server has issue
    os.system("curl -s -X POST https://api.telegram.org/bot1756020946:AAH5hj2QjeWAb9jhd--PevNCJTsy06AvdK8/sendMessage -d chat_id=971998000 -d text='Zabbix NGINX Server Problem:No server is available to handle this request.' ")
	
elif "Can't connect to MySQL" in db:
    print(db)
    # sending notification to telegram if MySQL database has issue
    os.system("curl -s -X POST https://api.telegram.org/bot1756020946:AAH5hj2QjeWAb9jhd--PevNCJTsy06AvdK8/sendMessage -d chat_id=971998000 -d text='Zabbix Mysql Server Problem:Cannot connect to MySQL' ")
