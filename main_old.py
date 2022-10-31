# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os, sys
import xml.etree.ElementTree as ET
import uuid
import datetime
from datetime import timezone, timedelta
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
    now = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
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
    xml_str = ET.tostring(sdk_record)
    print(xml_str)
    tree = ET.ElementTree(sdk_record)
    try:
        tree.write('out/NewHazardousObject_' + now + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True

# Создание XML Элемента ОПО описание и внесение в БД РТН
def creat_obj_xml():
    Obj = DB_connect.sel_obj(Guid_OPO)
    now = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
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
        tree.write('out/NewInstallation_' + now + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True

# Создание   8.1.6	Отчет «События промышленной безопасности, зафиксированные автоматически» для РТН
# Частота передачи:
# -	по событиям С1-С2 – при фиксации события или смене статуса события;
# -	по событиям С3 – при фиксации события или смене статуса события;
# -	по событиям С4 – не передается в рамках данного метода.
def creat_automaticEvent_xml():
    Event = DB_connect.sel_AE(Guid_OPO)
    # print(Event)
    now = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    nowTZ = str(datetime.datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=2))))   #Вычисление времени с ТЗ для отображения когда произошло событие
    print(nowTZ)
    sdk_automaticEvent = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_automaticEvent, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_automaticEvent, ET.QName(SOAP_NS, 'Body'))
    sdk_create_AE = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'AutomaticEvent'))
    sdk_create_obj = ET.SubElement(sdk_create_AE, ET.QName(SDK_NS, 'automaticEvent'),
                                   HazardousObjectNumber = Guid_OPO,
                                   RequestGuid = str(uuid.uuid4()),         #Присвоенный ДО номер запроса
                                   Ogrn = '1023001538460',
                                   EventClass = '3',                        #Справочник «Класс события»
                                   EventDateTime = str(Event[1]),           #Дата и время события
                                   EventDescription = str(Event[2]),        #Описание события
                                   EventStatus = '3'                        #Справочник «Текущий статус события» (перечень в разделе 8.3.2)
                                )
    xml_str = ET.tostring(sdk_automaticEvent)
    print(xml_str)
    tree = ET.ElementTree(sdk_automaticEvent)
    try:
            tree.write('out/automaticEvent_' + now + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True

# 8.1.7	Отчет «События промышленной безопасности, зафиксированные вручную»
# Частота передачи:
# -	по событиям Е1-Е2 – при фиксации события или смене статуса события;
# -	по событиям Е3 – при фиксации события или смене статуса события;
# -	по событиям Е4 – не передается в рамках данного метода (передается в рамках метода EventsQD).

def creat_manualEvent_xml():
    # Event = DB_connect.sel_obj(Guid_OPO)
    # print(Event)
    now = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    nowTZ = str(datetime.datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=2))))   #Вычисление времени с ТЗ для отображения когда произошло событие
    print(nowTZ)
    sdk_manualEvent = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_manualEvent, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_manualEvent, ET.QName(SOAP_NS, 'Body'))
    sdk_create_ME = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'ManualEvent'))
    sdk_create_obj = ET.SubElement(sdk_create_ME, ET.QName(SDK_NS, 'manualEvent'),
                                   HazardousObjectNumber = Guid_OPO,
                                   RequestGuid = str(uuid.uuid4()),         #Присвоенный ДО номер запроса
                                   Ogrn = '1023001538460',
                                   EventClass = '6',                   #Справочник «Класс события»
                                   EventDateTime = nowTZ,            #Дата и время события
                                   EventStatus = '3',                #Справочник «Текущий статус события» (перечень в разделе 8.3.2)
                                   ID = 'SIGNED_BY_CONSUMER'                #Фиксированное значение: SIGNED_BY_CONSUMER
                                )
    xml_str = ET.tostring(sdk_manualEvent)
    print(xml_str)
    tree = ET.ElementTree(sdk_manualEvent)
    try:
            tree.write('out/manualEvent_' + now + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True

# 8.1.8	Отчет «Оценка интегрального показателя промышленной безопасности за сутки по ОПО»
# Частота передачи – 1 раз в сутки.
def creat_opoRoib_xml():
    opo_Roib = DB_connect.sel_opo_Roib(Guid_OPO)
    sdk_opoRoib = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_opoRoib, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_opoRoib, ET.QName(SOAP_NS, 'Body'))
    sdk_create_OpoRoib = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'OpoRoib'))
    sdk_create_obj = ET.SubElement(sdk_create_OpoRoib, ET.QName(SDK_NS, 'hazardousObjectRoib'),
                                   HazardousObjectNumber = Guid_OPO,
                                   RequestGuid = str(uuid.uuid4()),         # Присвоенный ДО номер запроса
                                   Ogrn = '1023001538460',
                                   ID='SIGNED_BY_CONSUMER',                           # Фиксированное значение: SIGNED_BY_CONSUMER
                                   RoibOpoValue = str(opo_Roib[0]),            # Значение риск-ориентированного интегрального показателя промышленной безопасности ОПО
                                   RoibOpoDateTime = str(opo_Roib[1]),         # Дата и время, за которую предоставляются сведения расчета риск-ориентированного интегрального показателя промышленной безопасности ОПО
                                  )
    tree = ET.ElementTree(sdk_opoRoib)
    try:
            tree.write('out/opoRoib_' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True


# 8.1.5	8.1.3	Справочник «Технологические блоки»

def creat_NewТеchBlock_xml():
    TB = DB_connect.sel_TB()
    sdk_NewТеchBlock = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_NewТеchBlock, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_NewТеchBlock, ET.QName(SOAP_NS, 'Body'))
    sdk_create_NewТеchBlock = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'CreateNewТеchBlock'))
    sdk_create_obj = ET.SubElement(sdk_create_NewТеchBlock, ET.QName(SDK_NS, 'NewТеchBlock'),
                                   GuidOPO = Guid_OPO,
                                   Organization='faebb331-1927-491f-9635-64f1f1b5cd54')
    sdk_TechBlocks = ET.SubElement(sdk_create_obj, ET.QName(SDK_NS, 'TechBlocks'),
                                           Name=str(TB[0]),            # Полное наименование установки
                                           Guid=str(TB[1]),           # GUID Технологического блока, присвоенный ДО
                                           GuidInst='0A634505-5AF0-4275-8A8A-E50A16DA3F21'           # GUID Технологической установки, присвоенный ДО
                                    )
    tree = ET.ElementTree(sdk_NewТеchBlock)
    try:
            tree.write('out/NewТеchBlock' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True


# 8.1.5	Справочник «Технические устройства»
# Таблица 23 – Параметры ответа запроса метода NewTechdevice

def creat_NewTechdevice_xml():
    # opo_Roib = DB_connect.sel_opo_Roib(Guid_OPO)
    # print(opo_Roib)
    now = str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    nowTZ = str(datetime.datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=2))))   # Вычисление времени с ТЗ для отображения когда произошло событие
    print(nowTZ)
    sdk_NewTechdevice = ET.Element(ET.QName(SOAP_NS, 'Envelope'))
    sdk_Header = ET.SubElement(sdk_NewTechdevice, ET.QName(SOAP_NS, 'Header'))
    sdk_Body = ET.SubElement(sdk_NewTechdevice, ET.QName(SOAP_NS, 'Body'))
    sdk_create_NewTechdevice = ET.SubElement(sdk_Body, ET.QName(SDK_NS, 'CreateNewTechdevice'))
    sdk_create_obj = ET.SubElement(sdk_create_NewTechdevice, ET.QName(SDK_NS, 'createNewTechdevice'),
                                   GuidOPO = Guid_OPO,
                                   Organization='faebb331-1927-491f-9635-64f1f1b5cd54')
    sdk_TechnicalDevices = ET.SubElement(sdk_create_obj, ET.QName(SDK_NS, 'TechnicalDevices'),
                                           Name=str(Obj[1]),            # Полное наименование ТУ
                                           Guid=str(Obj[10]),           # GUID ТУ, присвоенный ДО
                                           GuidInst=str(Obj[10]),           # GUID Технологической установки, присвоенный ДО
                                           GuidTB=str(Obj[10]),           # GUID Технологического блока, присвоенный ДО
                                           LaunchDate=str(Obj[10]),           # Дата ввода в эксплуатацию
                                           PbRegNum=str(Obj[10]),           # Регистрационный номер заключения экспертизы промышленной безопасности
                                           PbIssueDate=str(Obj[10]),           # Дата заключения экспертизы промышленной безопасности
                                           PbValidUntil=str(Obj[10]),           # Срок действия заключения экспертизы промышленной безопасности
                                           PbState=str(Obj[10]),           # Код из справочника «Вывод о соответствии требованиям промышленной безопасности»
                                           State=str(Obj[10]),           # Код из справочника «Текущее состояние»
                                           OperationMode=str(Obj[10]),           # Код из справочника «Режим работы» (перечень в разделе 8.3.4)
                                           LimitIrLow='1',
                                           LimitIrNormal='0.8',
                                           LimitIrHigh='0.6',
                                           LimitIrMax='0.2',
                                           limitTrendLow='1',
                                           limitTrendNormal='0.8',
                                           limitTrendHigh='0.5',
                                           limitTrendMax='0.2',
                                           )
    xml_str = ET.tostring(sdk_NewTechdevice)
    print(xml_str)
    tree = ET.ElementTree(sdk_NewTechdevice)
    try:
            tree.write('out/NewTechdevice_' + now + '.xml', "UTF-8")
    except EnvironmentError as err:
            print("{0}: import error: {1}".format(
            os.path.basename(sys.argv[0]), err))
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    creat_opo_xml()
    creat_obj_xml()
    creat_NewТеchBlock_xml()
    creat_automaticEvent_xml()
    creat_manualEvent_xml()
    creat_opoRoib_xml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
