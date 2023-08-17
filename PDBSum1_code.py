#Guideliens for use
#Install a local installation of PDBSum1 as per instructions on PDBSum site and place the input PDB files in the 'inputfiles' folder and execute the code

import os
import shutil
import os

directory1 = './inputfiles/'
    
files_in_directory = os.listdir(directory1)
    
filtered_files = [file for file in files_in_directory if file.endswith(".pdb")]


for file in filtered_files:

    #path_to_file = os.path.join(directory, file)
    
    cmd1 = './exe_linux/pdbsum1' + ' ' + './inputfiles/'+file

    os.system(cmd1)
    
    pathres1 = os.listdir('./03/')
    
    for pa in pathres1:
        if pa != 'css':
            if pa != 'gif':
                if pa != 'runs':
                    
                    
    
                    path_to_file2 = os.path.join('./03/', str(pa))

                    path_to_file3 = path_to_file2 + '/a001' + '/protprot/'

                    files_in_directory3 = os.listdir(path_to_file3)

                    filtered_files3 = [file3 for file3 in files_in_directory3 if file3.endswith(".txt")]

                    for fv in filtered_files3:
                        if fv.startswith("iface"):
                            store = fv

                    fb = open(path_to_file3+store, 'r')

                    alll = fb.readlines()
                    fbb = open('ppi_hace2.txt', 'a+')
                    fbb.write(file)
                    for a in alll:
                        if 'Number of' in a:
                            a = a.replace('\n', '')
                            fbb.write( ',' + a )
            
    fbb.write('\n')
    fbb.close()
    pathres10 = os.listdir('./03/')
    
    for pa1 in pathres10:
    
        path_to_file20 = os.path.join('./03/', str(pa1))

        try:
            shutil.rmtree(path_to_file20)
        except:
            pass




