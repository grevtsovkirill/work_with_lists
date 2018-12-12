import os, math, sys, subprocess, argparse

parser = argparse.ArgumentParser(description='clean up list of derivations')
parser.add_argument('--fileToCheck','-f', type=str,
                    help='File with list of samples grid available on grid')
parser.add_argument('--grl','-g',type=str,
                    help='List of runs from grl')
parser.add_argument('--proj_name','-p',type=str,
                   help='Project name')
args = parser.parse_args()
in_file=args.fileToCheck
runs_grl=args.grl
project_name=args.proj_name

if not in_file:
    in_file = 'test.list'
    print 'empty, use test.list'

def find_dsid(list_to_look):
    dsid_list=[]
    for y in list_to_look:
        # !!!!!                                                                                                                                                                                                                               
        dsid = y[y.find('13TeV.')+8:y.find('.p')]
        #print y                                                                                                                                                                                                                              
        dsid_list.append(dsid)
        #print 'dsid=',dsid                                                                                                                                                                                                                   
    return dsid_list

def create_container_list(list_to_look,grl_list):
    container_list=[]
    for y in list_to_look:
        # !!!!!                                                                                                                                                                                                                               
        dsid = y[y.find('13TeV.')+8:y.find('.p')]
        if dsid in grl_list:
            container_list.append(y)
    return container_list

def extractList(file_name):
    list_deriv =[]
    with open(file_name) as f:
        content = f.readlines()
        for x in content:
            y= x.replace('\n','')
            if y:
                list_deriv.append(y)
                #print y                                                                                                                                                                                                                      
    list_deriv.sort()
    return list_deriv

av_list=extractList(in_file)
in_list=find_dsid(av_list)
grl_list=extractList(runs_grl)
print "Available"
print in_list

#print "Find dsid in av list"                                                                                                                                                                                                                 


print "In GRL"
print grl_list

def find_missing(grl_list,file_list):
    missing_list=[]
    for i in grl_list:
        if i not in file_list:
            missing_list.append(i)
            print i
    return missing_list



result =  all(elem in in_list  for elem in grl_list)
#print result                                                                                                                                                                                                                                 
if result:
    print "Yes, available samples contains all elements from GRL"
    final_list=create_container_list(av_list,grl_list)
    print "files for data container:"
    print final_list
else :
    print "FALSE, not satisfy GRL"
    print "missing files are: "
    mis_list=find_missing(grl_list,in_list)
    print "mis/tot_Grl=",len(mis_list),"/",len(grl_list)

