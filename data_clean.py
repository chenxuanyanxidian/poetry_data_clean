# -*- coding: utf-8 -*-
import codecs
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def read_data(input_file,out_file):
	input_data = codecs.open(input_file, 'r', 'utf-8' )
	output_data = codecs.open(out_file,'a', 'utf-8')
	poetrys = []  
	for line in input_data.readlines():
		try:  
			line1 = line.decode('UTF-8')
			line2 = line1.strip(u'\n')
			# print(line2)
			title, content = line2.strip(u' ').split(u':')
			content = content.replace(u' ',u'')
			if u'_' in content or u'(' in content or u'（' in content or u'《' in content or u'[' in content:  
				continue  
			if len(content) < 5 or len(content) > 79:  
				continue
			content = u'[' + content + u']'  
			poetrys.append(content)			 
			output_data.write(content + '\n')
			 
		except Exception as e:   
			pass  
	input_data.close()
    #output_data.close()
   
if __name__ == '__main__':

    read_data('./poetry.txt', './poetry_result.txt')
