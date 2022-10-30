# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os, sys
import xml.etree.ElementTree as ET
import uuid
import requests
from xml.etree import ElementTree

SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
SDK_NS = 'sdkrtn'

ET.register_namespace("sdk", SDK_NS)
ET.register_namespace("soapenv", SOAP_NS)

# def creat_xml():
#     sdk_record = ET.Element ('soapenv:Envelope', "xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sdk=\"sdkrtn")
#     sdk_Header = ET.SubElement(sdk_record, 'soapenv:Header')
#     sdk_Body = ET.SubElement(sdk_record, 'soapenv:Body')
#     xml_str = ET.tostring(sdk_record)
#     # ET.C14NWriterTarget('country_data.xml')
#     print(xml_str)
#     tree = ET.ElementTree(sdk_record)
#     try:
#         tree.write('out.xml', "UTF-8")
#     except EnvironmentError as err:
#             print("{0}: import error: {1}".format(
#             os.path.basename(sys.argv[0]), err))
#             return False
#     return True
    # tree = ET.parse('country_data.xml')
    # root = tree.getroot()
    # for child in root:
    #    print(child.tag, child.attrib)

def creat_opo_xml():

    sdk_record = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_record, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_record, ET.QName(SOAP_NS, 'Body'))
    sdk_create_opo = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'NewHazardousObject'), Organization = str(uuid.uuid4()))
    sdk_NewHazardousObject = ET.SubElement(sdk_create_opo, ET.QName(SDK_NS, 'HazardousObjects'),
                                           Name = 'Фонд Скважин',
                                           GuidOPO = str(uuid.uuid4()),
                                           LaunchDate = '2016-10-19',
                                           PbRegNum = '456789',
                                           PbIssueDate = '2019-10-19',
                                           PbValidUntil = '2023-10-19',
                                           PbState = '1',
                                           LimitIrLow = '0.2',
                                           LimitIrNormal = '0.6',
                                           LimitIrHigh = '0.8',
                                           LimitIrMax = '1.0')
    # sdk_HazardousObjects = ET.SubElement(sdk_NewHazardousObject, 'sdk:HazardousObject')
    xml_str = ET.tostring(sdk_record)
    # ET.C14NWriterTarget('country_data.xml')
    print(xml_str)
    tree = ET.ElementTree(sdk_record)
    try:
        tree.write('create.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    creat_opo_xml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
