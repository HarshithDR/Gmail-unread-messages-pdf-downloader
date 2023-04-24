import imaplib
import os
import email

user = str(input('Enter your email address: '))
password = str(input('Enter your password: '))
imap_url = 'imap.gmail.com'

def get_var_value(filename="number_recorder.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

your_counter = get_var_value()
downloading_path = str('C:\\Gmail_pdf'+str(your_counter)+'\\')
os.mkdir(downloading_path)
attachment_dir = ('C:\\Gmail_pdf'+str(your_counter)+'\\')

def auth(user, password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    return con

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

def search(key,value,con):
    result, data = con.search(None, key,"{}".format(value))
    return data

def get_attachments(msg,total_attachments):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath, 'wb') as f:
                f.write(part.get_payload(decode=True))

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs

con = auth(user,password,imap_url)
con.select('INBOX')

msgs = get_emails(search(None,'(UNSEEN)',con))
for msg in msgs:
    raw = email.message_from_bytes(msg[0][1])
    get_attachments(raw,len(msgs))

pdf_list = os.listdir('C:\\Gmail_pdf' + str(your_counter) + '\\')
with open(attachment_dir + '.txt', "w+") as ftxt:
    for z in range(0, len(pdf_list)):
        ftxt.write(str((z + 1)) + '- ' + str(pdf_list[z])+'\n')

if os.stat('C:\\Gmail_pdf' + str(your_counter) + '\\').st_size == 0:
    os.remove('C:\\Gmail_pdf' + str(your_counter) + '\\.txt')
    os.rmdir('C:\\Gmail_pdf'+str(your_counter)+'\\')
    print('No unread messages!')
    filename = "number_recorder.dat"
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) - 1
        f.seek(0)
        f.truncate()
        f.write(str(val))

else:
    print("Successfully downloaded "+str(len(pdf_list))+" pdf's")

