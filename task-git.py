shopping_list = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"],
    "apteka" : ["ibuprofen", "witaminy", "bandaż"]
}
ilosc = 0
print("Lista zakupów:")

for sklep in shopping_list:
    print("Idę do", sklep.title(), "i kupuję tam:",", ".join(element.title() for element in shopping_list[sklep]) + ".")
    ilosc += len(shopping_list[sklep])

print("W sumie kupuję", ilosc, "produktów.")
