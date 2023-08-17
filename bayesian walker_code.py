#About the script

#The script different levels of weights and generates mutants corresponding to the wild type of RBD of SARS CoV 2 and writes the outputs to 'Mutant_sequences_RBD.txt' 
main = 0 
qe = 0

while main < 100000:
    try:
        import pandas as pd
        import random

        import numpy as np


        df = pd.read_csv('1st_level_weights_for_walker.csv')

        weighted_sample = df.sample(n=1, weights="Frequency")
        #print(weighted_sample)

        res1 = weighted_sample['Residue'].tolist()


        df = pd.read_csv('2st_level_weights_for_walker.csv')

        weighted_sample = df.sample(n=100, weights="Frequency", random_state=np.random.RandomState())
        #weighted_sample = weighted_sample.sort_values('Frequency', ascending=False)
        #print(weighted_sample)
        con1 = weighted_sample['Residue'].tolist()



        residue = res1[0]

        #print(residue)

        for c in con1:
            if residue == str(c[1]):
                context = c
                #print(context)
                break
        Spike_Seq = 'TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCG'

        f5 = 0 
        indexres = []
        while f5 < len(Spike_Seq) - 1:
            dg = Spike_Seq[f5] + Spike_Seq[f5 + 1]
            if context == dg:
                indexres.append(f5)
            f5 += 1

        chosenres = random.choice(indexres)
        chosenres = chosenres + 1
        #print(chosenres)

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

        import pandas as pd


        df = pd.read_csv('3rd_level_weights_for_walker.csv')

        weighted_sample = df.sample(n=30, weights="Frequency", random_state=np.random.RandomState())


        weighted_sample = weighted_sample.sort_values('Frequency', ascending=False)

        con2 = weighted_sample['Mutation'].tolist()

        for c in con2:
            if residue == str(c[0]):
                mutation = c
                #print(mutation)
                mutated_residuelst = mutation.split('>')
                mutated_residue = mutated_residuelst[-1]
                #print(mutated_residue)
                break


        result_seq = replacer(Spike_Seq, mutated_residue , chosenres)

        fl = open('Mutant_sequences_RBD.txt', 'a+')
        
        chose2 = chosenres + 333

        
        
        

        
         fl.write(str(residue) + str(chose2) +str(mutated_residue)  + ',' + str(main)+ '\n')
    
    except:
        pass
    main += 1


