The Lab Check is to see if there is any abnormal rules especially in the perimeter firewalls that allows lab vlans reach outside world without any limitation or let traffic from internet have access to the lab network without limitation. 

About the Python script
Environment: Python 3.6 

#This script is used for extracting all rules related to Lab VLANs from the ACL

#This script can deal with all forms of IP addresses or network addresses. (eg: 192.168.0.0/24 or 192.168.1.5 or 192.168.0.1-192.168.0.10)

Input: xls files of PA-5050, 1sum_7010a,sum-asa5585-1,7cc-4500x,7cc-5540a,7cc-6509 firewalls, exported from tufin

Output: 8 files that records all ingress rules of the lab VLANs from each firewall
