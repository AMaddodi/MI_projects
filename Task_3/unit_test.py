from protocol_parser import data_parser

def test_success():
    data = b'\x02\x02\x157\xa2D\x00\xae\xf3\xaa\xd1\x08\x00E\x00\x00C\x00\x01\x00\x00\x06x<\xc0\xa8\x05\x15B\xfa\x97\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x02'
    # create data_parser object
    parser_obj = data_parser(data)
    print(parser_obj.device)
    print(parser_obj.command)

def test_failure():
    data = b'\x02\x02\x157\xa2D\x02'
    # create data_parser object
    parser_obj = data_parser(data)
    print(parser_obj.device)

