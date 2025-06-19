# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    operation = line[0]
    input_type = line[2]
    formatted_line = line.strip().replace("()", "").replace(";", "")
    formatted_line = formatted_line[2:]
    if operation == "S":
        s_output = ""
        for c in formatted_line:
            if c.isupper():
                s_output += " " + c.lower()
            else:
                s_output += c
        print(s_output.strip())
    else:
        c_output = ""
        for word in formatted_line.split(" "):
            c_output += word.capitalize()
        if input_type == "M":
            c_output += "()"
        if input_type != "C":
            c_output = c_output[0].lower() + c_output[1:]
        print(c_output)
