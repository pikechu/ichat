import os
import ftplib
import tempfile
import configparser


class FTPClient(object):
    def __init__(self) -> None:
        self.ftp = ftplib.FTP()
        self._is_conn = False
        self._is_login = False

    def conn(self, host: str, port: int):
        self._is_conn = (len(self.ftp.connect(host, port)) > 0)  # welcome

    def disconn(self):
        self.ftp.close()
        self._is_conn = False

    def _pwd(self):
        return self.ftp.pwd()

    def login(self, usr, passwd) -> bool:
        if not self._is_conn:
            return False
        try:
            self.ftp.login(usr, passwd)
        except Exception as e:
            return False
        self._is_login = True
        return True

    def upload_file(self, content: bytes, remote_path: str = '') -> bool:
        if not self._is_login:
            return False
        try:
            named_tf = tempfile.NamedTemporaryFile()
            named_tf.write(content)
            named_tf.flush()

            with open(named_tf.name, 'rb') as f:
                cmd = 'STOR {}'.format(remote_path)
                self.ftp.storbinary(cmd, f)
        except Exception as e:
            return False
        return True

    def get_file_list(self, path: str = '.') -> list:
        if not self._is_login:
            return []
        return [path + '/' + x for x in self.ftp.nlst(path)]

    def download_file(self, local_path: str, remote_path: str) -> bool:
        if not self._is_login:
            return False
        try:
            with open(local_path, 'wb') as f:
                cmd = 'RETR {}'.format(remote_path)
                self.ftp.retrbinary(cmd, f.write)
        except Exception as e:
            return False
        return True

    def quit(self):
        self.ftp.quit()
        self._is_conn = False
        self._is_login = False


if __name__ == '__main__':
    client = FTPClient()
    client.conn('127.0.0.1', 2121)
    client.login('rean', '123456')
    print(client.get_file_list())
    client.upload_file(b'hello', 'hello.txt')
    client.download_file('hello.txt', '/hello.txt')
    print(client.get_file_list())


