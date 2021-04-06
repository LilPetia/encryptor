# encryptor
Encruptor Python MIPT 2021
Aplication runnig by comand :
python3 encryptor.py[command][parameters]


Commands:
encode - ecoding text
--cipher [type of cipher] || Cipher type
--key [key] || key to encrypt
--input [file path]  || Path to input file
--output [file path] || Path to output file


decode - decoding text
--cipher [type of cipher] || Cipher type
--key [key] || key to encrypt
--input [file path]  || Path to input file
--output [file path] || Path to output file


Example: python3 main.py encode --cipher caesar --key 3 --input ./example.txt --output ./encrypted.txt   