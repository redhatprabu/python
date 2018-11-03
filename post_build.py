import os
import subprocess
from macpath import split


def create_log_file():
    file1 = open("output.txt", "w+")
    file2 = open("error.txt", "w+")


def read_input_file():
    read1 = open("input_cmd.txt");  
    readl_in_line = read1.read()
    pnt = readl_in_line.split("\n\n")
    for x in pnt:
        out1 = x.split("\n")
        for x2 in range(1, len(out1)):
            out2 = out1[x2].split("=")
            if out2[0] == "Title":
                title = out2[1]
            elif out2[0] == "command":
                command = out2[1]
            elif out2[0] == "Expected_Output":
                output = out2[1]
        run_my_command(title, command, output)

                
def run_my_command(title, command, output):
    subprocess.call(command)

    
if __name__ == "__main__":
    create_log_file()
    read_input_file()
