import hashlib
import getpass

print("Tell me a secret:")
# I don't love that this gives the prompt as "password:", but whatever
inp = getpass.getpass()

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


m = hashlib.sha256()

gib_list = [
'\u2020','\u2022','\u2023','\u203B','\u203F',
'\u2053','\u22C4','\u22C5','\u2218','\u2234',
'\u2235','\u2236','\u2238','\u2239','\u22B6',
'\u22B7','\u22B8','\u22B9','\u22C4','\u233D',
'\u233E','\u2300','\u2311','\u2393','\u23D2']

m.update(bytes(inp, 'utf-8'))
o = m.digest()
to = ''
for i in o:
	to += gib_list[i%len(gib_list)] + ' ' + '..*  '[i%5] + ' '
	# break up some visual repetition
	if(i%3>1):
		to += ' '
# fill in the last gap with a repeat of the start, kind of a lazy fix
rem = len(to) % 16
for i in range(0, 16 - rem):
	to += to[i]
for i in chunks(to, 16):
	print(i)
