import os
import ftplib
import tempfile
import configparser


class FTPClient(object):
    def __init__(self) -> None:
        self.ftp = ftplib.FTP()
        self._is_conn = False

    def _conn(self, host: str, port: int):
        self._is_conn = (len(self.ftp.connect()) > 0)   # welcome

    def _disconn(self):
        self.ftp.close()
        self._is_conn = False


    

cp = configparser.RawConfigParser()
cp.read(os.getcwd() + '/client.ini')
ftp.connect('127.0.0.1', 2121)
ftp.login('anonymous', '123456')

print(ftp.dir())


print(ftp.nlst('/test1'))

# named_tf = tempfile.NamedTemporaryFile()
# named_tf.write(b'test upload file')
# named_tf.flush()


# with open(named_tf.name, 'rb') as f:
#     cmd = 'STOR test2/uploadtest'
#     ftp.storbinary(cmd, f)


ftp.quit()