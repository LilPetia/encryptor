# encryptor
Encruptor Python MIPT 2021
Aplication runnig by comand :

python3 encryptor.py[command][parameters]


Commands:
encode - encoding text
--cipher [type of cipher] || Cipher type
--key [key] || Key to encrypt
--input [file path]  || Path to input file
--output [file path] || Path to output file


decode - decoding text
--cipher [type of cipher] || Cipher type
--key [key] || Key to encrypt
--input [file path]  || Path to input file
--output [file path] || Path to output file


train - training model
--input [file path] || Text to analyze
--output [file path] || Output model


hack - hack caesar cipher
--input [file path] || File to hack
--output [file path] || Hacked file
--model [file path] || Model file

Example: python3 main.py encode --cipher caesar --key 231 --input ./example.txt --output ./encrypted.txt   
 python3 main.py encode --cipher vernam --key 231 --input ./example.txt --output ./encrypted.txt