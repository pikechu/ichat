from Crypto import Random
from Crypto.PublicKey import RSA

def gen(private_key_path, public_key_path):
    random_generator = Random.new().read  # 生成随机偏移量
    # print(random_generator)
    rsa = RSA.generate(2048, random_generator)  # 生成一个私钥
    # print(rsa)
    # 生成私钥
    private_key = rsa.exportKey()  # 导出私钥
    # print(private_key.decode())
    # 生成公钥
    public_key = rsa.publickey().exportKey()  # 生成私钥所对应的公钥
    # print(public_key.decode())

    with open('rsa_private_key.pem', 'wb')as f:
        f.write(private_key)  # 将私钥内容写入文件中
        f.flush()

    with open('rsa_public_key.pem', 'wb')as f:
        f.write(public_key)  # 将公钥内容写入文件中
        f.flush()

if __name__ == '__main__':
    private_key_path, public_key_path = '', ''
    print('please input rsa_private_key generate path, such like ./rsa_private_key.pem')
    input(private_key_path)
    print('please input rsa_public_key generate path, such like ./rsa_public_key.pem')
    input(public_key_path)
    print('start generating')
    gen(private_key_path, public_key_path)
    print('generating finished')
