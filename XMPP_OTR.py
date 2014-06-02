import time
from otrxmppchannel import OTRXMPPChannel
from otrxmppchannel.connection import OTR_TRUSTED, OTR_UNTRUSTED, OTR_UNENCRYPTED, OTR_UNKNOWN

# Load the base64-encoded OTR DSA key. Constructing the object without
# a key will generate one and provide it via ValueError exception.
# privkey = open('.otrprivkey', 'r').read()

class MyOTRChannel(OTRXMPPChannel):
    def on_receive(self, message, from_jid, otr_state):
        if otr_state == OTR_TRUSTED:
            state = 'trusted'
        elif otr_state == OTR_UNTRUSTED:
            state = 'UNTRUSTED!'
        elif otr_state == OTR_UNENCRYPTED:
            state = 'UNENCRYPTED!'
        else:
            state = 'UNKNOWN OTR STATUS!'
        print('received %s from %s (%s)' % (message, from_jid, state))

if __name__ == '__main__':
    
    mychan = MyOTRChannel(
                          'test01@lens.com',
                          '123456',
                          'kenluo@lens.com',
                          '115.29.232.62',
                          #None
                          #privkey
                          'AAAAAACAgAAAAAAAAAhEhSKSD4SNwLnAvEdZsuXLvc1FKSQJD5Gif5CHc6IUbIixSr24utdFLVjovgkhuZqJw3Gt1yO0t8EMPgJeaIajM8K8fAgqwkQmsjKhDgxCuwijDUSMqaUvSQT13tGPjqKfKCV3wYHvVtebD+9Xf2Q34OzmA3/9m3MAAAAUhuHDHvKrYeqyAJNqEjxLSr7L0tkAAACAD4/eS0tQKCVwyyjhzZsIDK9YLCsyMgruT4gPJD3EKDPQe4ALM6V5FrtFzZm0xQWENQAhl5u4wrWQy3jtyPLWzqaq91m9Y0gSAr/+sjtdFb6Kx9mLix0wR8viiUhK+56DKv/5vGMSLrjAOhiQmgrxCS1GRaRyZoLiqOMMbB9R0lUAAACAJ8cZBOadrFa4dM5xxD8+cf0j8XLfP/ynnqMzfHwvyV//Gwn4WDhu+CG+hHrRdqgQ3Iwd5AQ8ztzZUvNxh6UgNm6mJV0qJAW5yI1H1tg9wn/8gEOPm59e79ktmw1OHSWLrmvyHC2yLjK3Awu2qbFn3erX5WtLJV8/V+0fpvHwkQIAAAAULp3QIiXEDbfiQmdx+XmnzaVYNB8='
                          )

    mychan.send('')  # Force OTR setup
    time.sleep(10)  # Wait a bit for OTR setup to complete
    mychan.send('This message should be encrypted')
    mychan.send('Alarm raised!!! (This is a dry run)')