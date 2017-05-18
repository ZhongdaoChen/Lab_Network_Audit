The Lab Check is to see if there is any abnormal rules especially in the perimeter firewalls that allows lab vlans reach outside world without any limitation or let traffic from internet have access to the lab network without limitation. 

About the Python script # This script is used for extracting all rules related to Lab VLANs from the firewall ACL.

#This script is used to extracting all rules related to Lab VLANs from the ACL

#This script can deal with all forms of IP addresses or network addresses.

#The input is xls files of PA-5050, 1sum_7010a,sum-asa5585-1,7cc-4500x,7cc-5540a,7cc-6509 firewalls

#The output is 8 files that records all ingress rules of the lab VLANs from each firewall

FYI: In most cases there is no need to read the code. Reading the report is enough. There are too many details about how to deal with the ACL files in the script. No fun at all believe me. 
