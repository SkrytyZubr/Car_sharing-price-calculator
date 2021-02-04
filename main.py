
class dupa:
    def __init__(self):
        self.time = int(input("Podaj czas w minutach\n"))
        self.distance = float(input("Podaj odległość\n"))
        self.my_list = {}
        self.wywolanie()

    def calculator(self, firma, start, km, min):
        result = round(self.time*min + self.distance*km + start, 2)
        print(str(firma), "  ", float(result))
        self.my_list[firma] = result

    def wywolanie(self):
        firma = ('Traficar clio', 'MiiMove Astra', 'MiiMove Ampera', 'Panek economt sta', 
            'Panek economt kil', 'Panek economt min', 'Panek comfort sta', 'Panek comfort kil', 
            'Panek comfort min', '4mobility economy', '4mobility premium')
        cena_star = (2.99, 0, 0, 0, 2.89, 2.89, 0, 2.89, 2.89, 0, 0)
        cena_km = (1.5, 0.8, 0, 0.8, 0, 0.99, 0.82, 0, 1.29, 0.8, 0.8)
        cena_min = (0, 0.67, 1.19, 0.55, 1.49, 0, 0.8, 1.99, 0, 0.5, 0.8)

        for a in range(0,11):
            self.calculator(firma[a], cena_star[a], cena_km[a], cena_min[a])
            
        self.over()

    def over(self):
        print("\nNajtaniej: ", min(self.my_list, key=self.my_list.get), + min(self.my_list.values()))

if __name__ == '__main__':
    dupa()