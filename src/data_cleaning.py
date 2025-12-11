import pandas as pd
import os 

reseau_en_arbre = pd.read_excel('data/raw/reseau_en_arbre.xlsx')
reseau_en_arbre.to_csv('data/raw/reseau_en_arbre.csv', index=False)

batiments = pd.read_csv('data/raw/batiments.csv')

infra = pd.read_csv('data/raw/infra.csv')

reseau_en_arbre = reseau_en_arbre.drop(columns=["nb_maisons"])
reseau_en_arbre = reseau_en_arbre.rename(columns={"infra_type": "infra_etat"})
reseau_en_arbre.to_csv('data/raw/reseau_en_arbre.csv', index=False)

print(reseau_en_arbre.head())

new_reseau_en_arbre = pd.merge(reseau_en_arbre, batiments, on="id_batiment")
print(new_reseau_en_arbre.head())


final_reseau_en_arbre = pd.merge(new_reseau_en_arbre, infra, left_on=["infra_id"], right_on=["id_infra"]) 
final_reseau_en_arbre = final_reseau_en_arbre.drop(columns="id_infra")
final_reseau_en_arbre.to_csv('data/processed/final_reseau_en_arbre.csv', index=False)
print(final_reseau_en_arbre.head())


