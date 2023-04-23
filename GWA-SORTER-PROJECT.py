import pyfiglet
# Introduction of the program.
result = pyfiglet.figlet_format("GWA SORTER", font = "bubble" )
print(result)

print("*" * 70)
input("\033[0;33mThe \033[0;31mstudent with highest GWA \033[0;33mwill be announced along with his/her GWA.\nPlease take note that the \033[0;33mcloser to 1.00, the higher the GWA.\033[1;31m\n1.00	95%-100%    Excellent\n1.25	91%-94%	    Superior\n1.50	88%-90%	    Very Good\n\033[1;35m1.5	86%-87%	    Good\n2.00	84%-85%     Very Satisfactory\n2.25	82%-83%	    High Average\n\033[1;34m2.50	79%-80%	    Average\n2.75	77%-78%	    Fair\n3.00	75% - 76%   Pass\n\033[1;33m4.00	58%-74.99%  Conditional if Pass/Failed\n5.00	58.49 below Failing Final Grade\n\033[0;33mTYPE ANY KEY HERE TO START:\n")
print()
# Loading time
import time
time.sleep(0.5)
print("\33[31mPlease wait for the names to be sorted.")
time.sleep(1.0)
print("\n\33[35mPlease wait... ")
time.sleep(1.0)
print("\n\33[33mJust a while...\n\033[0;92m\n⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️ ⭐️")
time.sleep(1.0)
result = pyfiglet.figlet_format("The list of students from highest to lowest GWA: ", font = "digital" )
print(result)
time.sleep(1.0)


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

    print("\033[0;34m")
# Make the dictionary print line by line. 
    for x in sorted_gwa:
        print(str(x).replace("'", "").replace("(", "").replace(")", "").replace(", ", "  "))
        output_file.write(str(x).replace("'", "").replace("(", "").replace(")", "").replace(", ", " - ") + "\n")

# Output the name with higest gwa and the higest gwa.
    print("\n\033[0;35mThe student with the higest GWA is:"  + "\033[1;35m" +sorted_gwa[0][0] + "\n" + "\033[0;35mThe higest GWA is:" +"\033[1;35m" + sorted_gwa[0][1])
    output_file.write("\nThe student with the higest GWA is:"+ sorted_gwa[0][0] + "\n" + "The higest GWA is:" + sorted_gwa[0][1])


print("Congratulations! 👏🏼 ")
print("\033[0;33mYou may save a copy in a form of \033[1;34mtext file\033[0;33m. Please check your directory. 💻\n ")