from urllib.request import urlopen
from bs4 import BeautifulSoup
def prgdbSequencefetcher(id, arg_type = None):
    """
    a custom function to fetch the dna and the 
    protein sequence from the plant resistance
    gene database and get the corresponding dna_sequence
    and the protein_sequence. provided a plant resistance
    gene id it uses the javascript fetcher to access the 
    plant resistance gene database and gives you the dna_
    sequence or the protein sequence as desired in the 
    arg_type, which is a keyworded argument. 
    id = plant resistance gene database id
    arg_type = dna or protein
    """
    if id and arg_type == "dna_sequence":
        resistancegene = id
        gene_url = urlopen(f"http://www.prgdb.org/prgdb/genes/type/reference/{resistancegene}")
        temp_gene_fetcher = list(map(lambda n: n.split(">") and n.split(";"), \
                                    (map(str,(BeautifulSoup(gene_url,"html.parser"). \
                                                          find_all(type="text/javascript")))))) 
        dna_sequence = [i[0].split(">")[1].split("(")[1]. \
                              replace(")", "") for i in temp_gene_fetcher][0]
        return dna_sequence
    if id and arg_type == "protein_sequence":
        resistancegene = id
        gene_url = urlopen(f"http://www.prgdb.org/prgdb/genes/type/reference/{resistancegene}")
        temp_gene_fetcher = list(map(lambda n: n.split(">") and n.split(";"), \
                                    (map(str,(BeautifulSoup(gene_url,"html.parser"). \
                                                          find_all(type="text/javascript"))))))
        protein_sequence = [i[0].split(">")[1].split("(")[1]. \
                                       replace(")", "") for i in temp_gene_fetcher][1] 
        return protein_sequence
