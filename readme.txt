1) Als je een nieuwe gebruiker wilt maken kunt u de volgende commando gebruiken
python3 main.py add-user --username naam --address "adress" --payment betaalmethode
Voorbeeld
python3 main.py add-user --username dirk --address "theebos 13" --payment AI

2) Als u een lijst wilt van users kunt u deze command gebruiken
python3 main.py user-list

3) Als u een lijst wilt van de producten dan kunt u deze commando gebruiken
python3 main.py product-list   

4) Als u een lijst wilt hebben van alle tags die in onze database staan dan kunt u deze commando gebruiken
python3 main.py tag-list

5) Als u een lijst wilt maken van de producten die een klant heeft dan kunt u de volgende commando gebruiken:
python3 main.py show-products-user --user-id id van user 
een voorbeeld:
python3 main.py show-products-user --user-id 1   

6) Als u een product wilt toevoegen aan de webshop kunt u de volgende commando gebruiken
python3 main.py create-catalog-product --product-name naam van het product --description "een beschrijving" --price hoeveel elk product kost --stock hoeveel we in vooraad hebben  
een voorbeeld: 
python3 main.py create-catalog-product --product-name apple --description "an amazing computer" --price 500 --stock 100   

7) Als u een product uit onze webwinkel wilt verwijderen We kunnen het product zoeken via id of naam
Om via een id te zoeken dan kunt u deze commando gebruiken:
python3 main.py remove-catalog-product --id id van het product dat u wilt verwijderen
een voorbeeld:
python3 main.py remove-catalog-product --id 5

Als u het via naam wilt zoeken en verwijderen dan kunt u deze commando gebruken
python3 main.py remove-catalog-product --product-name naam van het product dat u wilt verwijderen
een voorbeeld:
python3 main.py remove-catalog-product --product-name laptop

8) Als u een tag wilt aanmaken dan kunt u de volgende commando gebruiken:
python3 main.py create-tag --tag-name naam van de tag
een voorbeeld:
python3 main.py create-tag --tag-name stoel

9) Als u een tag wilt koppelen aan een product dan kunt u de volgende commando gebruiken:
python3 main.py pair-product-tag --product-id id van het product --tag-id id van de tag
een voorbeel :
python3 main.py pair-product-tag --product-id 1 --tag-id 4  

10) Als u een lijst van alle producten die gekoppeld zijn aan een tag dan kunt u deze commando gebruiken:
python3 main.py list-products-on-tag --tag-id een tag id
een voorbeeld:
python3 main.py list-products-on-tag --tag-id 4

U kunt ook op tag naam te zoeken omdat te doen kunt u de volgende commando gebruiken:
python3 main.py list-products-on-tag --tag-name een tag naam
Voorbeeld:
python3 main.py list-products-on-tag --tag-name fruit

11) Als u een product witl opzoeken kunt u de volgende commando gebruiken:
python3 main.py search --product naam van het product
Een voorbeeld:
python3 main.py search --product banana

Het zou rekening moeten houden met spellingsfouten maar dit is niet 100% correct
Als ik bijvoorbeeld frui opzoek dan zou het fruit moeten opzoeken

12) Als u een order voor een user wilt maken kunt u de volgende commando gebruiken:
python3 main.py buy --product-id id id van het product --buyer-id id van de user --quantity hoeveel de user wilt koppen
een voorbeeld:
python3 main.py buy --product-id 1 --buyer-id 1 --quantity 1      

13) Als een user een product wilt geven dan kunt u deze command gebruiken
python3 main.py give-product --product-id id van het product --buyer-id id van de user --quantity hoeveel we aan de user willen geven
Voorbeeld :
python3 main.py give-product --product-id 1 --buyer-id 1 --quantity 1

14) Als een product/order wilt verwijderen van de user dan kunt u deze commando gebruiken:
python3 main.py remove-product --product-id id van het product --user-id id van de user
een voorbeeld:
python3 main.py remove-product --product-id 1 --user-id 1

15) Als u de stock wilt aanpassen van een van de producten dan kunt u deze commando gebruiken:
python3 main.py update-stock --product-id id van het product --ammount-stock de hoeveelheid
een voorbeeld :
python3 main.py update-stock --product-id 1 --ammount-stock 100

15) Als u een overzicht wilt hebben van de revenue dan kunt u deze commando gebruiken:
python3 main.py revenue --startdate start datum --enddate eind datum
een voorbeeld:
python3 main.py revenue --startdate 2020-1-1 --enddate 2022-10-10

