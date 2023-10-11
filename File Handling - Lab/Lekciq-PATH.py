import os

WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(WORKING_DIRECTORY, "my_dir", "Emil.txt")

file = open(file_path, "w")

file.write("Hzxcaszddfa")
file.close()