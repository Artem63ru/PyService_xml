# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os, sys
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
import datetime


def creat_xml():
    # sdk_record = ET.Element ('s:Envelope', xmlns="http://schemas.xmlsoap.org/soap/envelope/")
    # sdk_Header = ET.SubElement(sdk_record, 's:Header')
    # sdk_RequestHeader = ET.SubElement(sdk_Header, 'h:RequestHeader', xmlns="http://dom.gosuslugi.ru/schema/integration/8.5.0.4/")
    # sdk_Body = ET.SubElement(sdk_record, 's:Body')
    # xml_str = ET.tostring(sdk_record)
    # # ET.C14NWriterTarget('country_data.xml')
    # print(xml_str)
    # tree = ET.ElementTree(sdk_record)
    # try:
    #     tree.write('out.xml', "UTF-8")
    # except EnvironmentError as err:
    #         print("{0}: import error: {1}".format(
    #         os.path.basename(sys.argv[0]), err))
    #         return False
    # return True
    tree = ET.parse('OPORoi.xml')
    root = tree.getroot()
    element = root[1][0][0]
    # for RoibOpoValue in root.iter('RoibOpoValue'):
    #     print(RoibOpoValue.attrib)
    # for neighbor in root.iter('hazardousObjectRoib'):
    element.set('RoibOpoValue', '1.0')
    element.set('RoibOpoDateTime', datetime.datetime.now().isoformat())
    element.set('RoibOpoDescription', 'Работа штатно')
    tree.write('OPORoi.xml', "UTF-8")
    print(element)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    creat_xml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
