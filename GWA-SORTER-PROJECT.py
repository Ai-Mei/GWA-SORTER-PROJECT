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

# Sort the dictionary from highest to lowest gwa.
    sorted_gwa = sorted(name_gwa.items(), key = lambda x:x[1])
    

# Save the data to arranged-list.txt.
    output_file.write("Name - GWA\n")
    output_file.write("\n")
    print("The list of students from highest to lowest GWA: \n")

# Make the dictionary print line by line. 
    for x in sorted_gwa:
        print(str(x).replace("'", "").replace("(", "").replace(")", "").replace(", ", "  "))
        output_file.write(str(x).replace("'", "").replace("(", "").replace(")", "").replace(", ", " - ") + "\n")

# Output the name with higest gwa and the higest gwa.
    print("\nThe student with the higest GWA is:", sorted_gwa[0][0] + "\n" + "The higest GWA is:", sorted_gwa[0][1])
    output_file.write("\nThe student with the higest GWA is:" + sorted_gwa[0][0] + "\n" + "The higest GWA is:" + sorted_gwa[0][1])