from RamachanDraw import fetch, phi_psi, plot
data=open('question6.txt','r')

for i in data.readlines():
    l=list()
    l=i.split()

    # PDB id to be downloaded
    PDB_id = l[3]

    # Drawing the Ramachandran plot
    plot(fetch(PDB_id),out='./RMAP-Projects/'+PDB_id+'.png')

    # Generating a dictionary to store the phi and psi angles
    # And returning the ignored aminoacid residues
    phi_psi_dict, ignored_res = phi_psi(fetch(PDB_id), return_ignored=True)
print('All Maps have been printed')

