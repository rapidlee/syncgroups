import re

# Read the OpenGrok file and save it to a var
with open('open_grok.txt', 'r') as f:
    print(f'The filename you are searching from is: {f.name}')
    file_contents = f.read()
    
# Test input for @yelp domain or @ sign, if not then add the @yelp domain to the input
def test_domain_input(original_input):
    stripped_input = original_input.strip()
    lowercased_input = stripped_input.lower()
    clean_input = lowercased_input
    if re.search(r'\@yelp.com', clean_input):
        return clean_input
    elif clean_input.endswith('@'):
        clean_input += 'yelp.com'
        return clean_input
    else:
        # bprint('There is no @ sign')
        clean_input += '@yelp.com'
        return clean_input

# Find the pattern in file_contents using the final_input var
def find_pattern(final_input):
    list_output = []
    # If input pattern is found, split results in 2 and search 2nd group for pattern
    if re.search(final_input, file_contents):
        first_result = re.search(f'({final_input})(.+)', file_contents)
        first_result_2nd_group = first_result.group(2)
        # Now that we have the 2nd group we search for =cn=g patterns and iterate it through
        matches = re.findall(r'g-.+?,', first_result_2nd_group)
        # print(f'Below are restricted groups in AD for {final_input}:')
        for match in matches:
            list_output.append(match[:-1])
        return list_output
        #print(first_result.group(2))
    else:
        return False

hey = test_domain_input('nys-office@')
print(hey)