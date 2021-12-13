def search_multiple_str(file_name, list_of_strings):
    
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        
        for line in read_obj:
            line_number += 1
            
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    
    return list_of_results

def main():
    print(' Check string exists  ')
    
    matched_lines = search_multiple_str('test_file.txt', ['with', 'no'])
    if (len(matched_lines) > 0):
	     print(matched_lines)
    else:
	    print("String not found")				
if __name__=='__main__':
   main()
