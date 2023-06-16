#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# Add all the names of invited_names.txt into a list. Using method ".readlines()"
with open("Input/Names/invited_names.txt") as file:
    list_names = (file.readlines())

# f = open("Input/Names/invited_names.txt", "r")
# list_names = (f.readlines())

# Open and read the template
with open("Input/Letters/starting_letter.txt") as bbb:
    template = bbb.read()

for i in list_names:
    # Remove spaces at the begining and end of the string.
    word = i.strip()

    # Replace "[name]" in the starting_letter.txt for each name in the i iteration
    replaced = template.replace("[name]", word) 
 
    # Save the letter in Output/ReadyToSend folder:
    filename = f"Output/ReadyToSend/letter_to_{word}.txt"
    with open(filename, mode="w") as letter:
        letter.write(f"{replaced}")


