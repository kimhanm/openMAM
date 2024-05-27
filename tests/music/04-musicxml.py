from lxml import etree



tree = etree.parse("./musicxml/hello-world.musicxml")
root = tree.getroot()

print(root.tag)