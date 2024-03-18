class data_parser():
    """
        This is a class to parse data packet to extract header elements and payload data
        
        data : data packet 
    """
    
    # init the class variables
    def __init__(self,data):
        self.data = data
        self.header_segments = {}  # header elements
        self.header_len = 0        # header length
        self.device = 'none'       # device info
        self.payload = ''          # payload data
        self.command = ''          # read write command
        
        if len(self.data) < 9:
            print( "insufficient data packet")
            return 
        self.parse()

    def parse(self):
        print(self.data)

        self.extract_header()

        self.get_device(self.header_segments['devices'])

        self.extract_payload()
        
        self.extract_command()

    # extract payload
    def extract_payload(self):
        self.payload = self.data[self.header_len:]

    # get device details
    def get_device(self, device_code):
        if device_code == b'\x00':
            self.device = 'agito'
        elif device_code == b'\x01':
            self.device = 'master'
        elif device_code == b'\x02':
            self.device = 'hub'
        else:
            self.device = 'invalid_device_code'
        return

    # extract header info
    def extract_header(self):
        self.header_segments['devices'] = self.data[0:1]
        self.header_segments['packet_len'] = self.data[1:2]
        self.header_segments['checksum'] = self.data[2:6]
        self.header_segments['data_address'] = self.data[6:8]
        self.header_segments['rw_command'] = self.data[8:9]

        # header lenght 
        self.header_len = 9
    
    def extract_command(self):
        if self.header_segments['rw_command'] == b'\x01':
            self.command = 'read'
        elif self.header_segments['rw_command'] == b'\x10':
            self.command = 'write'
        elif self.header_segments['rw_command'] == b'\x11':
            self.command = 'read_write'
        else:
            self.command = 'invalid_command'
    
     
