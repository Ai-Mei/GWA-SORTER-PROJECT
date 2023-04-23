# Open name-and-gwa-list.txt (read) and open aranged-list.txt (append)
with open("NAMES-AND-GWA-LIST.txt") as input_file, open("ARANGED-LIST.txt", "a") as output_file:
# Make a dictionary of the file content.
    lines = input_file.readlines()
    name_gwa = {}
    for line in lines: 
        # Split the line into key-value pairs 
        name, gwa = line.strip().split(' - ') 
        # Store the key-value pairs in the name_gwa dictioanry 
        name_gwa[name] = gwa

    print(name_gwa)
# Sort the dictionary from highest to lowest gwa.
# Output the name with higest gwa and the higest gwa.

