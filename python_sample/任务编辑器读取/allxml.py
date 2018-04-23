#coding:utf-8
from xml.etree import ElementTree  
import re

root = ElementTree.parse("10191001.xml")
inner = root.find('regtask').find('rt_taskid').text

root = ElementTree.parse("ring.xml")
print root.find('regtask').find('rt_cname2').text.encode('utf-8')
print root.find('taskproc').find('tp_ring').text

root = ElementTree.parse("noring.xml")
print root.find('regtask').find('rt_cname2').text.encode('utf-8')
print root.find('taskproc').find('tp_ring').text



