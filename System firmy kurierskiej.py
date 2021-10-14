import sys
# Przywitanie i poproszenie o wybranie pozycji
print("Witaj w systemie Firmy kurierskiej Maxi!")

print("Co chcesz zrobić?")

print("1 - Wyślij paczkę")

print("2 - Zaloguj się")
# wybór pozycji
wybór = input()


if wybór == '1':
    print("Podaj dane paczki")

    input("Adres: ")

    input("Kod pocztowy: ")

    input("Miasto: ")
    
    skończenieWpisywaniaAdresu = input("Gdy wypełnisz już wszystkie dane napisz wybierz 1:  ")

    if skończenieWpisywaniaAdresu == '1':
        print("Ok, twoja paczka zostanie wkrótce nadana! Dziękujemy i zapraszamy ponownie!")
        print("                                                                            ")
        print("Co chcesz zrobić?")
        print("0 - Wyjdź z aplikacji")
        zakończenie = input()
        if zakończenie == '0':
            sys.exit()

if wybór == '2':
    print("Wprowadź dane!")
    login = input("Wprowadź login: ")
    hasło = input("Wprowadź hasło: ")
    if hasło == '123' and login == 'Kurier':
        print("Zalogowano!")
    else:print("                                                                            ")
    print("Wprowadzono błędne dane!")
    print("                                                                            ")
    print("Co chcesz zrobić?")
    print("                                                                            ")
    print("0 - Wyjdź z aplikacji")
    zakończenie2 = input()
    if zakończenie2 == '0':
        sys.exit()