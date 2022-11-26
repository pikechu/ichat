import ftplib
import tempfile

ftp = ftplib.FTP()
ftp.connect('127.0.0.1', 2121)
ftp.login('rean', '123456')

print(ftp.dir())


print(ftp.nlst('/test1'))

named_tf = tempfile.NamedTemporaryFile()
named_tf.write(b'test upload file')
named_tf.flush()


with open(named_tf.name, 'rb') as f:
    cmd = 'STOR test2/uploadtest'
    ftp.storbinary(cmd, f)


ftp.quit()