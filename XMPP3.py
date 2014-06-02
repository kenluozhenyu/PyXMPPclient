import xmpp
import otrxmppchannel


class Bot:
    #""" Jabber Bot Base Class """
    JID = ''
    PASSWORD = ''
    SERVER = ''

    client = None   

    def __init__ (self, jid, password, server):
        self.JID = xmpp.JID(jid)
        self.PASSWORD = password
        self.SERVER = server

        self.login()

    def login (self):         
        self.client = xmpp.Client(self.JID.getDomain(), debug=[])
        if self.client.connect(server= (self.SERVER, 5222)) == '':
            raise 'JabberBot not connected.'
        if self.client.auth(self.JID.getNode(), self.PASSWORD) == None:
            raise 'JabberBot authentication failed.'
        
        self.client.RegisterHandler('message', self.message_callback)
        self.client.RegisterHandler('presence', self.presence_callback)
        self.client.sendInitPresence()

    def message_callback (self, client, message):
        """ do something """

    def presence_callback (self, client, message):
        """ do something """
        type = message.getType()
        who = message.getFrom().getStripped()

        if type == 'subscribe':
            self.subscribe(who)
        elif type == 'unsubscribe':
            self.unsubscribe(who)
        elif type == 'subscribed':
            self.subscribed(who)
        elif type == 'unsubscribed':
            self.unsubscribed(who)
        elif type == 'available' or type == None:
            self.available(message)
        elif type == 'unavailable':
            self.unavailable(who)

    def subscribe (self, jid):
        """ add friend"""
        self.client.send(xmpp.Presence(to=jid, typ='subscribed'))
        self.client.send(xmpp.Presence(to=jid, typ='subscribe'))

    def unsubscribe (self, jid):
        """ cancel friend """
        self.client.send(xmpp.Presence(to=jid, typ='unsubscribe'))
        self.client.send(xmpp.Presence(to=jid, typ='unsubscribed'))

    def subscribed (self, jid):
        """ added """

    def unsubscribed (self, jid):
        """ unsubscribed """
        
    def available (self, message):
        """ online """

    def unavailable (self, jid):
        """ offline """

    def send (self, jid, message):
        """ send msg to somebody"""
        self.client.send(xmpp.protocol.Message(jid, message))

    def step (self):
        """ loop """
        try:
            self.client.Process(1)
        except KeyboardInterrupt:   # Ctrl+C to stop
            return False
        return True


#===========================
# test
#===========================
class Bott(Bot):
    def message_callback (self, cl, msg):
        fromid = msg.getFrom().getStripped()
        cont = msg.getBody()
        self.send2admin(msg)
        print('received %s from %s' % (cont, fromid))

    def send2admin (self, message):
        self.send('kenluo02@lens.com', message)

if __name__ == '__main__':
    #gb = Bott ('test01@cgc.com', '123456', '112.124.71.9')
    gb = Bott ('test02@lens.com', '123456', '115.29.232.62')
    gb.send2admin ('Daemon Started')
    gb.send2admin ('This message is NOT encrypted')
    gb.send2admin ('Alarm raised!!! (This is a dry run)')

    # start
    while (gb.step()): pass 
