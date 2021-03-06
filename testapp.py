

import re
import os
from datetime import datetime

# Read the OpenGrok file and save it to var f
with open('open_grok.txt', 'r') as f:
    # print(f'The filename you are searching from is: {f.name}')
    file_contents = f.read()
    
# Test input for @yelp domain or @ sign, if not then add the @yelp domain to the input
def test_domain_input(original_input):
    # strip spaces
    clean_input = original_input.strip()
    if re.search(r'\@yelp.com', clean_input):
        return clean_input
    elif clean_input.endswith('@'):
        clean_input += 'yelp.com'
        return clean_input
    else:
        clean_input += '@yelp.com'
        return clean_input

# Find the pattern in file_contents using the final_input var
def find_pattern(final_input):
    list_output = []
    # If input pattern is found, split results in 2 and search 2nd group for pattern
    if re.search(f'(^{final_input})', file_contents, re.IGNORECASE | re.MULTILINE):
        first_result = re.search(f'^({final_input})(.+)', file_contents, re.IGNORECASE | re.MULTILINE)
        first_result_2nd_group = first_result.group(2)
        # Now that we have the 2nd group, we search for =cn=g patterns and iterate it through
        matches = re.findall(r'memberof=cn=.+?,', first_result_2nd_group, re.IGNORECASE)
        for match in matches:
            list_output.append(match[12:-1])
        return list_output
    # Making a one off exception for salesmanagers which does not have @yelp domain attached to it
    elif final_input == 'salesmanagers@yelp.com':
        first_result = re.search(f'(salesmanagers)(.+)', file_contents, re.IGNORECASE | re.MULTILINE)
        first_result_2nd_group = first_result.group(2)
        # Now that we have the 2nd group we search for =cn=g patterns and iterate it through
        matches = re.findall(r'memberof=cn=.+?,', first_result_2nd_group, re.IGNORECASE)
        for match in matches:
            list_output.append(match[12:-1])
        return list_output
    else:
        return False
        
# This f() is the same as find_pattern but instead looks for department
def find_dept(final_input):
    dept_list_output = []
    # If input pattern is found, split results in 2 and search 2nd group for pattern
    if re.search(f'(^{final_input})', file_contents, re.IGNORECASE | re.MULTILINE):
        first_result = re.search(f'^({final_input})(.+)', file_contents, re.IGNORECASE | re.MULTILINE)
        first_result_2nd_group = first_result.group(2)
        # Now that we have the 2nd group, we search for department= and iterate it through
        matches = re.findall(r'department=.+?\)', first_result_2nd_group, re.IGNORECASE)
        for match in matches:
            dept_list_output.append(match[11:-1])
        return dept_list_output

# Get the last modified date of open_grok file
def get_file_lastmod_date():
    # last_updated = os.stat('open_grok.txt').st_mtime
    a = os.path.getmtime('open_grok.txt')
    b = datetime.fromtimestamp(a)
    last_modified = str(b)
    return last_modified[:10]
