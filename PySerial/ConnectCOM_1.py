import serial
import unittest
import time

class serialPort():

    @classmethod
    def setUpModule(self):
        self.ser = serial.Serial(0,9600, parity='N',bytesize=8, stopbits=1, 
                timeout=None, xonxoff=False, 
                rtscts=False, dsrdtr=False)  
        print self.ser.name      # check which port was really used
        
    @classmethod
    def tearDownModule(self):
        self.ser.close()           
        print("Disconnecting")
        
    
    @classmethod
    def Test_Com(self):
        print self.ser.name          
        self.ser.write("US 1 1 1 \n")      
        time.sleep(5)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
    
    