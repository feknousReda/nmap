import nmap
import csv

host = input('Please enter you target : ')
argument = input('Please enter your arguments : ')
nm = nmap.PortScanner()
print('scanning ...')
nm.scan(arguments = argument , hosts = host)
var_xml = nm.get_nmap_last_output()
print(nm.command_line())
my_dict = nm.scaninfo()

#La prochaine étape consiste a éxploiter my_dict pour le rendre en format .csv
