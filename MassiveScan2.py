import os 
import sys
import ipaddress
import socket

def check_file(filename):
	"""Checking the file. Does the file exist. Checking the size of a file."""
	check_file = os.path.exists(filename)
	if check_file == True:
		if os.path.getsize(filename) == 0:
			print('')
			print('Error.')
			print('File ips.txt is empty.') 
			print('')
			sys.exit()
	else:
		print('')
		print('Error.')
		print('Not found file ' + filename + '.')
		print('')
		sys.exit()

def convert_file(infilename, outfilename):
	""" Deletes empty lines and rewrites to a new file. """
	with open(infilename) as infile, open(outfilename, 'w') as outfile:
		for line in infile:
			if not line.strip():
				continue
			outfile.write(line)

def sum_str(filename):
	""" Counts the number of lines in a file. """
	res = sum(1 for line in open(filename, 'r'))
	return res

def start_scan(host, port, timeout):
	""" Scans the host. """
	timeout = float(timeout)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(timeout) 
	try:
		connect = sock.connect((ip,int(port)))
		print(ip)
		res.write(ip + '\n')
	except Exception as e:
		pass


# Files
infilename = 'ips.txt'
outfilename = 'output_ips.txt'
all_ips = 'all_ips.txt'
result = 'result.txt'


# Check and convent files
check_file(infilename)
convert_file(infilename, outfilename)


# Translation of networks to an ip
allips = open(all_ips, 'w')
networks = open(outfilename, "r")

for net in networks:
	net = (net.join(net.split()))
	subnet = ipaddress.ip_network(net)
	for ip in subnet:
		ip = str(ip)
		allips.write(ip + '\n')

allips.close()
networks.close()


# Users setting
# Users port
port = input("Enter port: ")
# Users timeout
timeout = input("Enter timeout (default: 0.01): ")
if timeout == '':
	timeout = str(0.01)


# Result info
# All networks
print('\n' + 'networks: ' + str(sum_str(outfilename)))

# All ips
print('ips:      ' + str(sum_str(all_ips)))

# User port 
print('port:     ' + port)

# User timeout 
print('timeout:  ' + timeout + '\n')


# Start scan
res = open(result, 'w')
ips_tmp = open(all_ips, "r")
for ip in ips_tmp:
	ip = str(ip.replace("\n",""))
	start_scan(ip, port, timeout)

res.close()
