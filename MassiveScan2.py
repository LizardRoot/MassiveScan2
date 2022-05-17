import os 
import sys
import ipaddress

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


# Files
infilename = 'ips.txt'
outfilename = 'output_ips.txt'
all_ips = 'all_ips.txt'


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


# User port
port = input("Enter port: ")


# Result info
# All networks
print('\n' + 'networks: ' + str(sum_str(outfilename)))

# All ips
print('ips: ' + str(sum_str(all_ips)) + ' ips')

# User port 
print('port: ' + port)