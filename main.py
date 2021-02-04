
class calculator:
    def __init__(self):
        self.time = int(input("Podaj czas w minutach\n"))
        self.distance = float(input("Podaj odległość\n"))
        self.dict_result = {}
        self.call()

    def algorithm(self, company, start, km, min):
        result = round(self.time*min + self.distance*km + start, 2)
        print(company, "  ", result)
        self.dict_result[company] = result

    def call(self):
        company = ('Traficar clio', 'MiiMove Astra', 'MiiMove Ampera', 'Panek economt sta', 
            'Panek economt kil', 'Panek economt min', 'Panek comfort sta', 'Panek comfort kil', 
            'Panek comfort min', '4mobility economy', '4mobility premium')
        price_star = (2.99, 0, 0, 0, 2.89, 2.89, 0, 2.89, 2.89, 0, 0)
        price_km = (1.5, 0.8, 0, 0.8, 0, 0.99, 0.82, 0, 1.29, 0.8, 0.8)
        price_min = (0, 0.67, 1.19, 0.55, 1.49, 0, 0.8, 1.99, 0, 0.5, 0.8)

        for a in range(0,11):
            self.algorithm(company[a], price_star[a], price_km[a], price_min[a])

        self.over()

    def over(self):
        print("\nNajtaniej: ", min(self.dict_result, key=self.dict_result.get), + min(self.dict_result.values()))

if __name__ == '__main__':
    calculator()