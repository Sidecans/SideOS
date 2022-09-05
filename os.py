import xml.etree.ElementTree as XML
import sys

tree = XML.parse("OS\\Drive\\ProgramFiles\\Sidecans\\OS\\Data\\UserData.xml")
root = tree.getroot()
print(root[0].text)
