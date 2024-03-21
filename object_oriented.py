class NetworkDevice :
    def __init__(self, hostname, ip_address) :
        self.hostname = hostname
        self.ip_address = ip_address
    def display_config(self) :
        print(f"Hostname: {self.hostname}, IP Address: {self.ip_address}")

router = NetworkDevice ("Router1", "192.168.1.1")
print(f"Device: {router.hostname}, IP: {router.ip_address}")

#class NetworkDevice :
#    def __init__(self, hostname, ip_address) :
#        self.hostname = hostname
#        self.ip_address = ip_address



router.display_config()

class Router(NetworkDevice) :
    def __init__(self, hostname, ip_address, routing_protocol):
        super().__init__(hostname, ip_address)
        self.routing_protocol = routing_protocol
    def display_config(self) :
        super().display_config()
        print(f"Routing Protocol: {self.routing_protocol}")


router = Router("Router1", "192.168.1.1", "OSPF")
print(f"Routing Protocol: {router.routing_protocol}")


#class Router(NetworkDevice) :
    # initialization method omittef for brevity
#    def display_config(self) :
#        super().display_config()
#        print(f"Routing Protocol: {self.routing_protocol}")

router.display_config()

