#XML is eXtensive markup language
import requests
import xml.etree.ElementTree as ET

api_url = "https://example.com/api/get_xml_data"

response = requests.get(api_url)
xml_data = ET.fromstring(response.text)
print(xml_data)
