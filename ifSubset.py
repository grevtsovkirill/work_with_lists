import os, math, sys, subprocess, argparse

parser = argparse.ArgumentParser(description='clean up list of derivations')
parser.add_argument('--fileToCheck','-f', type=str,
                    help='File with list of samples grid available on grid')
parser.add_argument('--grl','-g',type=str,
                    help='List of runs from grl')
args = parser.parse_args()
in_file=args.fileToCheck
runs_grl=args.grl

if not in_file:
    in_file = 'test.list'
    print 'empty, use test.list'

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

in_list=extractList(in_file)
grl_list=extractList(runs_grl)
print "Available"
print in_list
print "In GRL"
print grl_list

result =  all(elem in in_list  for elem in grl_list)
print result
