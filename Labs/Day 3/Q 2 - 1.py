def write_numbers_to_file(filename):
    file=open(filename, "w")
    for i in range(1,6):
        file.write(str(i)+"\n")
    file.close()
    print("success")
#from my_package.file_module import
from my_package.file_module import write_numbers_to_file

write_numbers_to_file("numbers.txt")
