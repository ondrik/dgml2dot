#!/usr/bin/env python3
import re
import sys
import xml.etree.ElementTree as ET


###########################################
def to_dot(fd):
    '''TODO
    '''

    xml_in = ""
    while True:
        line = fd.readline()
        if not line: break
        xml_in += line + "\n"

    xml_in = re.sub(' xmlns="[^"]+"', '', xml_in, count=1)
    root = ET.fromstring(xml_in)

    print("Digraph G {")
    for node in root.findall("Nodes/Node[@Category='State']"):
        # print(node.attrib)
        print('{} [label=\"{}"];'.format(node.attrib['Id'], node.attrib['Label']))

    for link in root.findall("Links/Link[@Category='NonepsilonTransition']"):
        # print(link.attrib)
        print('{} -> {} [label="{}"];'.format(
            link.attrib['Source'], link.attrib['Target'], link.attrib['Label']))

    # for link in root.findall("Links/Link[@Category='StartTransition']"):
    #     print(link.attrib)

    print('}')
    return


###############################
if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 1:
        fd = sys.stdin
    elif argc == 2:
        fd = open(sys.argv[1], "r")
    else:
        print("Invalid number of arguments: either 0 or 1 required")
        sys.exit(1)

    to_dot(fd)
    if argc == 2:
        fd.close()
