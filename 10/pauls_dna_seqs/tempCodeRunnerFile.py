def third_column():
    header_changes_knife = open('header_changes.csv','r')
    for i in header_changes_knife:
        third_column_read = [line.split(',')[2] for line in header_changes_knife]
        pass_to_print = my_print(third_column_read)

def my_print(my_header_list):
    print(my_header_list)

third_column()