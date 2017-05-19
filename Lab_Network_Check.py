"""
Input : lab_vlan.txt which include the network addresses to be checked.
        ACL file from Tufin
Output: xls files which records all rules related to the lab machines.

"""


import ipaddress
import xlrd
import xlwt

global_m = 0

def get_value():
    global global_m
    return global_m

def set_value():
    global global_m
    global_m += 1

def set_zero():
    global global_m
    global_m = 0

def ip2num(ip):
    ip=[int(x) for x in ip.split('.')]
    return ip[0] <<24 | ip[1]<<16 | ip[2]<<8 |ip[3]
def num2ip(num):
    return '%s.%s.%s.%s' %( (num & 0xff000000) >>24,
                            (num & 0x00ff0000) >>16,
                            (num & 0x0000ff00) >>8,
                            num & 0x000000ff)
def get_ip(ip):
    start,end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start,end+1) if num & 0xff]

def extract_related_rules(ip,file):
    n = 0
    for i in range(0,sh.nrows):
        temp_line = sh.cell_value(i, 14)    #context. For source address, 12. For destination address, 14
        ip_index = sh.cell_value(i, 14).find(ip)    #index
        if(ip_index>=0 and len(temp_line)==len(ip)+ip_index):
            for j in range(12,19):
                string = str(sh.cell_value(i, j))
                worksheet.write(get_value(),n,sh.cell_value(i,j))
                if j ==12:
                    source_ip = str(sh.cell_value(i,j))
                    if "-" in source_ip:
                        source_ip = str(source_ip.split("-")[1])
                        print(source_ip, ip)
                    elif "/" in source_ip:
                        source_ip = str(source_ip.split("/")[0])
                n += 1
            with open('./mhl.txt') as file_object: #for one acl rule, check the source IP and Dest IP in MHL file
                flag = 0
                for line in file_object:
                    if(str(ip) in line) and flag != 1:
                        worksheet.write(get_value(), n, line)
                        flag += 1
                        n += 1
                        print("Dest:" + str(ip))
                        continue

                    elif(source_ip in line and flag != 2):
                        worksheet.write(get_value(), 12, line)
                        flag += 2
                        print("Source:" + source_ip)
                        continue
                    elif(flag ==3):
                        break
                    else:
                        continue
            set_value()
            n = 0
    workbook.save("./Ingress ACL From all firewalls/ACL_from_"+file +".xls")
fp_ips = open('./all_lab_ips.txt','w')
ACL_file = ["PA-5050", "1sum-7010a","1sum-asa5585-1","7cc-4500x", "7cc-5540a", "7cc-6509", "50ib-7010a", "320c-6513"]
for file in ACL_file:
    set_zero()
    bk = xlrd.open_workbook(file + ".xlsx")
    sh = bk.sheet_by_name(file + ".csv")
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('ACL related to LAB')
    with open('./lab_vlan.txt') as file_object: #read all networks need to be check
        for line in file_object:
            line = line[:-1]
            if line.find('-') >= 0:     #network like 192.168.0.1-192.168.0.10
                iplist = get_ip(line)
                for ip in iplist:
                    fp_ips.write(ip)
                    fp_ips.write('\n')
                    extract_related_rules(ip,file)
            elif line.find('/') >= 0:           #network like 192.168.1.0/24
                for ip in ipaddress.ip_network(line).hosts():
                    fp_ips.write(str(ip))
                    fp_ips.write('\n')
                    extract_related_rules(str(ip),file)
            else:
                fp_ips.write(str(line))
                fp_ips.write('\n')
                extract_related_rules(str(line),file)
fp_ips.close()