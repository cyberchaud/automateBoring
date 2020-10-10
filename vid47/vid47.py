import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#conn.login() conn.login(username, password)

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 20-Aug-2015'])
rawMessage = conn.fetch([UIDs], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessaage.factory(rawMessage[UIDs][b'BODY[]'])
message.get_subject()