import struct
from protocol import login_pb2
from protocol import rpc_header_pb2

def pack(header, request) -> bytes:
    p = struct.pack('!sII', b'(', header.ByteSize(), request.ByteSize())
    p += header.SerializeToString()
    p += request.SerializeToString()
    p += b')'
    return p


def unpack(data: bytes):
    l, len_head, len_req = struct.unpack('!sII', data[:9])
    if l != b'(':
        return None, None
    if len(data) - 10 != len_head + len_req:
        return None, None
    return data[9:len_head+9], data[9+len_head:9+len_head+len_req]


def check_pack(data) -> bool:
    l, len_head, len_req = struct.unpack('!sII', data)
    if data[0] != '(':
        return False
    if len(data) - 10 != len_head + len_req:
        return False


if __name__ == '__main__':
    header = rpc_header_pb2.MHead()
    header.from_addr = '127.0.0.1'
    header.from_port = 12000
    header.device = rpc_header_pb2.OS_IOS
    login_req = login_pb2.LoginReq()
    login_req.user = 'rean'
    login_req.password = '1234'
    p = pack(header, login_req)
    print(p)
    h, l = unpack(p)
    header2 = rpc_header_pb2.MHead()
    login_req2 = login_pb2.LoginReq()
    header2.ParseFromString(h)
    login_req2.ParseFromString(l)

    print(h, l)
    print(login_req2, header2)
    from google.protobuf import message
    # message.Message.




