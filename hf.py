#this is a program to calculte the hartree-fock energy of a closed shell molecule

#read the geometry
input_file=open('geom.dat') #open the file For reading mode is by default in open() function but if you want to write then give (, 'w') explicitly 
file_content=input_file.readlines() #read the content
input_file.close() #close the file
print(file_content)

#store the input in list
temp_geom=[]
for line in file_content:
    v_line=line.rstrip() #remove white spaces after every line
    if len(v_line)>0:
        temp_geom.append(v_line.split()) #split the lines
print(temp_geom)

#NATOM
NATOM=int(temp_geom[0][0])
print('no. of atoms' +str(NATOM))
atom_symbols=[] # this list contains atom symbol
for i in range(1, NATOM+1):
    atom_symbols.append(temp_geom[i][0])
print(atom_symbols)
#no. of electrons
for i in range(len(atom_symbols)):
    k=no_of_e(atom_symbols[i])
    NE+=k
('no. of electron is '+str(NE))

