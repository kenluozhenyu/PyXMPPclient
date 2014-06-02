import xmpp

if __name__ == '__main__':
    # username = 'luozhenyu1976@gmail.com'
    username = 'luozhenyu@chat.facebook.com'
    #password = 'lzy88888'
    password = 'Lzy12345'
    jid = xmpp.protocol.JID(username)
    client = xmpp.Client(jid.getDomain(), debug=['always'])
    # client = xmpp.Client(('gmail.com', 5222), debug=list())
    # client = xmpp.Client(('talk.google.com', 5222), debug=['always'])
    client.connect()
    client.auth(jid.getNode(), password)
    client.send(xmpp.protocol.Message("luozhenyu@gmail.com", "hello Luozhenyu!"))