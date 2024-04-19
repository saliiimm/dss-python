import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("graphe.xml")
root = tree.getroot()

# Initialize variables to store sum of weights and count of outgoing arcs
sum_weights = 0
outgoing_arcs_count = 0

# Iterate over each <sommet> element
for sommet in root.findall('sommet'):
    if sommet.get('marqué') == 'oui':
        setiq = sommet.get('setiq')
        print(f"Vertex {setiq} is marked 'oui':")

        # Calculate sum of weights and count outgoing arcs for this vertex
        for arc in root.findall('arc'):
            if arc.get('sommet') == setiq:
                aetiq = arc.find('aetiq').text
                cout = arc.find('cout').text
                sum_weights += int(cout)
                outgoing_arcs_count += 1
                print(f"- Outgoing arc: destination={arc.get('sbut')}, weight={cout}")

# Display the calculated sum of weights and outgoing arcs count
print(f"\nTotal sum of weights for vertices marked 'oui': {sum_weights}")
print(f"Total number of outgoing arcs for vertices marked 'oui': {outgoing_arcs_count}")
