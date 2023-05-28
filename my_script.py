'''
    Descritption: this python script is used to generate the hex file of for Atmege32 MC
    Author: Ahmed Abdalla
    Data: MAY 28 2023
    E-Mail: ahmed.m.abdalla650@gmail.com 

    Note all source files, header files and must be in the same directory or folder including the script
    => if you are using standard libraries the object files must be within the same folder


'''

import os
import subprocess

tet = list()
tet.append(subprocess.run(["ls"]))

print(tet)
#directory = "C:\\Users\\hamad\\OneDrive\\Desktop\\New"
directory = str(os.getcwd())

all_obj = str()

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        file_name , file_extension = os.path.splitext(f)
        if file_extension == ".c" :  
            all_obj = all_obj +file_name + ".o "
            #print(f"avr-gcc" + " " + "-mmcu=atmega32 " + "-c " +  file_name + ".c " + "-o " + file_name + ".o "+"-l" )
            os.system(f"avr-gcc" + " " + "-mmcu=atmega32 " + "-c " +  file_name + ".c " + "-o " + file_name + ".o " )


print(all_obj)
os.system(f"avr-gcc " + "-Wall " +"-Os "+ "-mmcu=atmega32 " + "-o " + "Final" + ".elf "  +  all_obj)

os.system("avr-objcopy -j .text -j .data -O ihex Final.elf Final.hex")

print(os.getcwd())
