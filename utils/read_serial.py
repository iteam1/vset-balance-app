import serial

# input com port
my_com = input("Enter your serial-com (Default COM3): ") 
if my_com == "": my_com = "COM3"

try:
    my_serial = serial.Serial(my_com)
    print(f"Serial COM = {my_serial.name} Connected!") # check com port
except Exception as e:
    print(e)
    exit() # exit if error
    
if __name__ == "__main__":
    while True:
        comming_data = my_serial.read(14) # read():read on byte, read(14): read up to 14 bytes, readline() readline
        my_string = comming_data.decode()
        print(my_string.strip()) 

#ser.write(b'hello')     # write a string decode to bytes .decode()