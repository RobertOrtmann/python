try:
    result = 10 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
   print("Attempted to divide by zero. Setting result to None.")
   result = None
print(f"Result: {result}")

try:
# Code that might raise different exceptions
    network_device = {"ip": "192.168.1.1", "port": 22}
    print(network_device["hostname"]) # KeyError: 'hostname' not in dictionary
except KeyError as e:
    print(f"Missing key: {e}")
except Exception as e: # Catch all other exceptions
    print(f"An unexpected error occurred: {e}")


def validate_ip(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        raise ValueError(f"Invalid IP address format: {ip_address}")
    
    for octet in octets:
        if not octet.isdigit():  # Check if it's a valid number
            raise ValueError(f"Invalid octet '{octet}' in IP address: {ip_address}")
        
        if not (0 <= int(octet) <= 255):  # Check if the number is within the valid range
            raise ValueError(f"Octet '{octet}' out of range (0-255) in IP address: {ip_address}")

# Additional validation logic here
    return True

try:
    validate_ip("256.1.1.1") # Invalid IP, will raise ValueError
except ValueError as e:
    print(e)
