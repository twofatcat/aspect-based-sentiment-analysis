from xml.dom import minidom

xmldoc = minidom.parse('./Assignment3/Restaurants_Train.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
# print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.value)

