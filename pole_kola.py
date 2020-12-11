class Mathematic():
    """Klasa zawierająca działania matematyczne"""


    
    def circle(self):
        """Metoda wyświetlająca obliczenia związanie z kołem."""
        print("Jakie wybierasz działanie związane z kołem?")
        print("\n 1 - obliczanie pola"
        "\n 2 - obliczanie obwodu")
        circle_ask = input("\nWybierz cyfrę: ")
        circle_ask = int(circle_ask)
        if circle_ask == 1 :
            print("\nWartość pi ustawiona została na 3.14")
            r = input("Podaj promień:")
            r = int(r)
            field_calculation = r*r *3.14
            print(f"Pole koła o promieniu {r} wynosi {field_calculation}")
            
        if circle_ask == 2 :
            r = input("Podaj promień:")
            r = int(r)
            field_calculation = 2 * 3.14 * r
            print(f"Obwód koła o promieniu {r} wynosi {field_calculation}")
        
        if circle_ask != 1 and circle_ask != 2:
            print("Nie podałeś dobrego programu")
            

first = Mathematic()
first.circle()