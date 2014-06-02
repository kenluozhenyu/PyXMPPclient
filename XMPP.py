
#!/usr/bin/python
import xmpp
import thread
import time
# from xmpp import *

def xmpp_msg_func ():

    #username = 'test01@cgc.com'
    username = 'test01@lens.com'
    password = '123456'
    
    jid = xmpp.protocol.JID(username)
    client = xmpp.Client(jid.getDomain(), debug=['always'])
    
    #client.connect(server= ('112.124.71.9',5222), secure=1)
    #if client.connect(server= ('112.124.71.9',5222), secure=None):
    if client.connect(server= ('115.29.232.62',5222), secure=None):
        print ('Connected to server.')
    else:
        print ('Cannot connect to server!!!')
            
        
    if client.auth(jid.getNode(), password):
    #if not client.auth('test01@cgc.com', password, sasl=1):
        print('Auth passed')
    else:
        raise IOError('Can not auth with server.')
    
    client.send(xmpp.protocol.Message("kenluo@lens.com", "Hello Python!"))
    
    count = 0
    while count < 5:
        client.auth(jid.getNode(), password)
        client.send(xmpp.protocol.Message("kenluo@lens.com", "Hello XMPP! " + str(count)))
        time.sleep(2)
        count+=1

def run_proc ():
    try:
        thread.start_new_thread(xmpp_msg_func, ())
    except:
        print "Error: unable to start thread"
    
    time.sleep(30)
        
if __name__ == '__main__':
    #try:
    #    thread.start_new_thread(xmpp_msg_func, ())
    #except:
    #    print "Error: unable to start thread"
    #
    #time.sleep(30)
    
    run_proc()
    