def search_multiple_str(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results

def main():
    print('* Check if a string exists in a file * ')
    # Check if string 'is' is found in file 'sample.txt'
    matched_lines = search_multiple_str('test_file.txt', ['with', 'no'])
    if (len(matched_lines) > 0):
	     print(matched_lines)
    else:
	    print("String not found")				
if __name__=='__main__':
   main()