import os, sys
import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from datetime import datetime, timezone
from requests.structures import CaseInsensitiveDict
import uuid

def creat_xml():


    url = "https://www.w3schools.com/xml/tempconvert.asmx"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/soap+xml"
    i=1
    data = """
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sdk="sdkrtn">
   <soapenv:Header/>
      <soapenv:Body>
      <sdk:OpoRoib>
         <!--Optional:-->
         <sdk:hazardousObjectRoib RoibOpoValue="{}" RoibOpoDateTime="{}" RoibOpoDescription="Низкий риск"  HazardousObjectNumber="А38-00001-3001" RequestGuid="{}" Ogrn="1023001538460" ID="1" >
            <!--Optional:-->
            <sdk:Signature>
               <!--Optional:-->
               <sdk:SignedInfo>
                  <!--Optional:-->
                  <sdk:CanonicalizationMethod Algorithm="?"/>
                  <!--Optional:-->
                  <sdk:SignatureMethod Algorithm="?"/>
                  <!--Optional:-->
                  <sdk:Reference URI="?">
                     <!--Optional:-->
                     <sdk:Transforms>
                        <!--Zero or more repetitions:-->
                        <sdk:Transform Algorithm="?"/>
                     </sdk:Transforms>
                     <!--Optional:-->
                     <sdk:DigestMethod Algorithm="?"/>
                     <!--Optional:-->
                     <sdk:DigestValue>?</sdk:DigestValue>
                  </sdk:Reference>
               </sdk:SignedInfo>
               <!--Optional:-->
               <sdk:SignatureValue>?</sdk:SignatureValue>
               <!--Optional:-->
               <sdk:KeyInfo>
                  <!--Optional:-->
                  <sdk:X509Data>
                     <!--Optional:-->
                     <sdk:X509Certificate>?</sdk:X509Certificate>
                  </sdk:X509Data>
               </sdk:KeyInfo>
            </sdk:Signature>
         </sdk:hazardousObjectRoib>
      </sdk:OpoRoib>
   </soapenv:Body>
    </soap12:Envelope>
    """.format(i, datetime.now(timezone.utc).astimezone().isoformat(), uuid.uuid4())

    # resp = requests.post(url, headers=headers, data=data)
    with open('reqv.xml', 'w', encoding='utf-8') as f:
     f.write(data)
    print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    creat_xml()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
