last_packet_collection = [
    {'packet_type': 'a1', 'data': 'hello1'},
    {'packet_type': 'a2', 'data': 'hello2'},
    {'packet_type': 'a3', 'data': 'hello3'}
]

for x in last_packet_collection:
    if x['packet_type'] == 'a1':
        x['data'] = 'world'
# p[0]['data']='world'

for last_packet in last_packet_collection:
    print(last_packet['packet_type'], last_packet['data'])

def funcB(type, *args):
    print(type, *args)

def funcA(*args):
    funcB('test',*args)

funcA('hello', 'world')


d = {'test_a1.csv':'hello world'}
d['ww']='gg'
print(d['ww'])

#self.data_dict[self.log_files[packet_type]] = self.data_dict[self.log_files[packet_type]] + str