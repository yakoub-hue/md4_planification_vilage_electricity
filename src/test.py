import pandas as pd
import networkx as nx
#import matplotlib.pyplot as plt

df = pd.read_csv('data/processed/final_reseau_en_arbre.csv')
df = df[df["infra_etat"] != "infra_intacte"]

infra = df.drop(columns=["id_batiment","nb_maisons","type_batiment"])
infra = infra.drop_duplicates(subset=["infra_id"])

print(infra.head())

total_aerien = infra[infra["type_infra"] == "aerien"]["longueur"].sum() * 500
total_fourreau = infra[infra["type_infra"] == "fourreau"]["longueur"].sum() * 900
total_semiaerien = infra[infra["type_infra"] == "semi-aerien"]["longueur"].sum() * 750

numero_infra = infra["infra_id"].nunique()
total_ouvrier = numero_infra*4*35.2*300/8


def cout_total():
    return total_aerien + total_fourreau + total_semiaerien + total_ouvrier

cout = cout_total()
print(numero_infra)
print(cout)


