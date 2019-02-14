from List_of_index import *

def json_output(header, subdict):
	
	
	
	for key, value in json_dict.items():
		for keys, values in subdict.items():
			
			if key == keys:
			
				if header == 'openports':
					json_dict[key][0][header]= values
					
				elif header == 'waybackurls':
					json_dict[key][0][header]= values
				

				elif header == 'interestedurls':
					json_dict[key][0][header]= values
					
				else:
					
					if type(values) == list:
						
						list1 = filter(None, values)
						
						json_dict[key][0][header] = list(set(list1))
						
					else:
						
						json_dict[key][0][header]= values