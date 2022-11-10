import Get_vna_id , socket, os, time

numpoints = 51 #value of points per sweep, will need to be user input
startfreq = 1e9 #value of lowest frequency, will need to be user input
stopfreq = 2e9 #value of highest frequency, will need to be user input

bufsize = Get_vna_id.bufsize #pulled from user interface
vna = Get_vna_id.vna #pulled from user interface

#vna.sendall('*CLS\n'.encode())
#time.sleep(.1)
vna.write('*IDN?\n'.encode())
time.sleep(.1)
print("\n" , vna.recv(bufsize))

