import xml.dom.minidom

domtree = xml.dom.minidom.parse("group.xml")

root = domtree.documentElement

persons = root.getElementsByTagName("person")

for person in persons:
    print("--person--")

    if person.hasAttribute("id"):
        print(f"ID: {person.getAttribute('id')}")

    name = person.getElementsByTagName("name")[0]
    age = person.getElementsByTagName("age")[0]
    weight = person.getElementsByTagName("weight")[0]
    height = person.getElementsByTagName("height")[0]


persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = name = "New name"