vlans = {10, 20, 30, 40, 50}
protocols = set(['OSPF', 'BGP', 'EIGRP'])
print(vlans)
print(protocols)

vlans.add(60)
print(vlans)

vlans.remove(10)
protocols.discard('EIGRP')
print(vlans)
print(protocols)

a = {1, 2, 3}
b = {3, 4, 5}
union_set = a.union(b)
print(union_set)

intersection_set = a.intersection(b)
print(intersection_set)

difference_set = a.difference(b)
print(difference_set)

ips = set()
ips.add('192.168.1.1')
ips.add('10.0.0.1')
ips.add('192.168.1.1')
print(ips)

switch1_vlans = {10, 20, 30}
switch2_vlans = {20, 30, 40}
missing_vlans = switch1_vlans.difference(switch2_vlans)
print(missing_vlans)

