import xml.etree.cElementTree as ET
def main():
    ET.register_namespace('', 'http://www.tei-c.org/ns/1.0')
    tree = ET.ElementTree(file="/Users/pubintern4/Documents/tlg0616.tlg001.1st1K-grc1.xml")
    root = tree.getroot()
    # no prefix, thus the blank first argument 
    my_iter = root.iter('{http://www.tei-c.org/ns/1.0}div')
    next(my_iter)
    next(my_iter)
    for item in my_iter:
        if item.attrib['subtype'] == 'section':
            item.attrib['subtype'] = 'chapter'
            i = 1
            for child in item:
                if child.tag == '{http://www.tei-c.org/ns/1.0}p':
                   # content = ???
                    
                    child.tag = '{http://www.tei-c.org/ns/1.0}div'
                    child.attrib['subtype'] = 'section'
                    child.attrib['n'] = str(i)
                    child.attrib['type'] = 'textpart'
                    paragraph = ET.SubElement(child, 'r')                    
                    i+=1
  #  for r_tag in root.iter('{http://www.tei-c.org/ns/1.0}r'):
   #     r_tag.tag = '{http://www.tei-c.org/ns/1.0}p'
    tree.write('/Users/pubintern4/output_with_r_tags.xml', encoding='utf-8', xml_declaration = True, method='xml')
def tester_2():
    ET.register_namespace('', 'http://www.tei-c.org/ns/1.0')
    tree = ET.ElementTree(file="/Users/pubintern4/Documents/tlg0616.tlg001.1st1K-grc1.xml")
    tree.write('/Users/pubintern4/output2.xml', encoding='utf-8', xml_declaration = True, method='xml')
    
'''
from pathlib import Path 
import xml.etree.cElementTree as ET
def parse(xml_file):
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    print(root)
    for div in root.iter('{http://www.tei-c.org/ns/1.0}div'):
        try:
            div.set('subtype', 'chapter')
        except Exception as e:
            print(e)
        print(div.attrib)
def main():
    parse("tlg0616.tlg001.1st1K-grc1.xml")
main()
'''
    
main()
tester_2()

        
