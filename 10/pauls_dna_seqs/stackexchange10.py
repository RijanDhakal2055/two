import csv

def read_csv(filename):
    """ Returns a list of rows, where each row is a dict """
    print(f'Reading csv file {filename}')
    with open(filename) as f:
        return list(csv.DictReader(f))

def read_fasta_file(filename):
    """ Returns a string tuple (header, rest_of_the_file) """
    print(f'Reading fasta file {filename}')
    with open(filename) as f:
        content = f.read()
    lines = content.spltlines()
    
    # header is the first line
    # data is the rest of the file
    header, data = lines[0], '\n'.join(lines[1:])
    return header, data


# Assumption: We have at least the columns
# target_file: The file you want to update
# new_header: The updated header
updates = read_csv('header_changes.csv')

fasta_files = ['0.fasta', '10.fasta']
# This is dict of the form
# {
#   'data1.fasta': ('TCTCG', '...'),
#   'data2.fasta': ('TCTCG', '...'),
# }
fasta_files = {filename: read_fasta_file(filename) for filename in fasta_files}

# Produce a new dict with the same format, but updated header values
updated_files = {}
for update in updates:
    target_filename = updates['target_file']
    old_header, data = fasta_files[target_filename]
    new_header = updates['new_header']
    updated_files[target_filename] = (new_header, data)

# Write the changes to disk
for filename, (header, data) in updated_files:
    print(f'Outputting to updated_{filename}')
    content = header + '\n' + data
    with open(f'updated_{filename}', 'w') as f:
        f.write(content)