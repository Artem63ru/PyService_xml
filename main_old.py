# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os, sys
import xml.etree.ElementTree as ET
import uuid
from DB import DB_connect

import requests
from xml.etree import ElementTree

SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
SDK_NS = 'sdkrtn'

ET.register_namespace("sdk", SDK_NS)
ET.register_namespace("soapenv", SOAP_NS)

Guid_OPO = '9A65966D-BFB7-45AA-A7A8-D9B3C0CF9868'

# Сщздание XML ОПО описание и внесение в БД РТН
def creat_opo_xml():
    OPO = DB_connect.Sel_OPO(Guid_OPO)
    sdk_record = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_record, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_record, ET.QName(SOAP_NS, 'Body'))
    sdk_create_opo = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'NewHazardousObject'),
                                   Organization = 'faebb331-1927-491f-9635-64f1f1b5cd54')
                                   # Organization = str(uuid.uuid4()))
    sdk_NewHazardousObject = ET.SubElement(sdk_create_opo, ET.QName(SDK_NS, 'HazardousObjects'),
                                           Name = str(OPO[5]),
                                           GuidOPO = str(OPO[9]),
                                           LaunchDate = str(OPO[3]),
                                           PbRegNum = str(OPO[2]),
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
        tree.write('NewHazardousObject.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True

def creat_obj_xml():
    Obj = DB_connect.sel_obj(Guid_OPO)
    print(Obj)
    sdk_obj = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_obj, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_obj, ET.QName(SOAP_NS, 'Body'))
    sdk_create_obj = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'NewInstallation'),
                                   GuidOPO = Guid_OPO,
                                   Organization = 'faebb331-1927-491f-9635-64f1f1b5cd54')
                                   # Organization = str(uuid.uuid4()))
    sdk_NewHazardousObject = ET.SubElement(sdk_create_obj, ET.QName(SDK_NS, 'Installations'),
                                            Name = str(Obj[1]),
                                            Guid = str(Obj[10]),
                                            LimitIrLow = '1',
                                            LimitIrNormal = '0.8',
                                            LimitIrHigh = '0.6',
                                            LimitIrMax = '0.2',
                                            limitTrendNormal='1',
                                            limitTrendHigh='0.8',
                                            limitTrendMax='0.6',
                                           )
    xml_str = ET.tostring(sdk_obj)
    print(xml_str)
    tree = ET.ElementTree(sdk_obj)
    try:
        tree.write('NewInstallation.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    creat_opo_xml()
    creat_obj_xml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
