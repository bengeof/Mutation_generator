#About script
#For the generated mutants the protein-protein complex structures were modelled using the wild-type as the template using multi-chain modelling in MODELLER



import pandas as pd
#import homelette as hm

from modeller import *
from modeller.automodel import *    # Load the automodel class


def replacer(s, newstring, index, nofail=False):
            # raise an error if index is outside of the string
        if not nofail and index not in range(len(s)):
            raise ValueError("index outside given string")

            # if not erroring, but the index is still not in the correct range..
        if index < 0:  # add it to the beginning
            return newstring + s
        if index > len(s):  # add it to the end
            return s + newstring

            # insert the new string between "slices" of the original
        return s[:index] + newstring + s[index + 1:]


dfr = pd.read_csv('DynaMut2_results.csv')

dfr






mutatnts = dfr['Mutant'].tolist()

Spike_Seq = 'TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCG/EVQLVESGGGLVQPGGSLRLSCAASGITVSSNYMNWVRQAPGKGLEWVSLIYSGGSTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYHCARDLVVYGMDVWGQGTTVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEP/EIVLTQSPGTLSLSPGERATLSCRASQSVSSSYLAWYQQKPGQAPRLLIYGASSRATGIPDRFSGSGSGTDFTLTISRLEPEDFAVYYCQQYGSSPTFGQGTKLEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC*'



k = 0 

while k < len(mutatnts):
    
    try:
        os.remove('rbdtemp.ali')     
    except:
        pass
    
    f = mutatnts[k][1] + mutatnts[k][2] + mutatnts[k][3]
    #print(f)
    fd = int(f) - 333
    #print(fd)
    fc = str(mutatnts[k][4])
    replaced = result_seq = replacer(Spike_Seq, fc , fd)
    
    save = open('rbdtemp.ali', 'a+')
    
    save.write('>P1;2abx_n' + '\n')
    
    save.write('structureX:/home/2abx_n.pdb: FIRST:@ END:  :::::' + '\n')
    
    save.write('TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCG/-VQLVESGGGLVQPGGSLRLSCAASGITVSSNYMNWVRQAPGKGLEWVSLIYSGGSTYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYHCARDLVVYGMDVWGQGTTVTVSSASTKGPSVFPLAP------SGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEP/EIVLTQSPGTLSLSPGERATLSCRASQSVSSSYLAWYQQKPGQAPRLLIYGASSRATGIPDRFSGSGSGTDFTLTISRLEPEDFAVYYCQQYGSSPTFGQGTKLEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC*' + '\n')


    wt1 = '>P1;1hc9' 
    
    wt1 = wt1.replace('1hc9', str(mutatnts[k]))
                     
    save.write(wt1 + '\n')
    
    wt2 = 'sequence:1hc9: FIRST:@ END:  :::::'
    
    
    wt2 = wt2.replace('1hc9', str(mutatnts[k]))
    
    save.write(wt2 + '\n')
                      
                      
    save.write(replaced + '\n')
                      
    save.close()
                      
                      
    env = Environ()
    # directories for input atom files
    env.io.atom_files_directory = ['.', '../atom_files']

    # Be sure to use 'MyModel' rather than 'AutoModel' here!
    a = AutoModel(env,
                alnfile  = 'rbdtemp.ali' ,     # alignment filename
                knowns   = '2abx_n',              # codes of the templates
                sequence = str(mutatnts[k]))              # code of the target

    a.starting_model= 1                # index of the first model
    a.ending_model  = 1                # index of the last model
                                       # (determines how many models to calculate)
    a.make()                           # do comparative modeling
                      
            
            
    rm1 = str(mutatnts[k]) +'.ini'
    rm2 = str(mutatnts[k]) + '.rsr'
    rm3 = str(mutatnts[k]) + '.sch'
    
    
    try:
        os.remove(rm1)
        os.remove(rm2)
        os.remove(rm3)
        
    except:
        pass
    k += 1
    
    
    
    
    
    
    


# In[ ]:





# In[ ]:




