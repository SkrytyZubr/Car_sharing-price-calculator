from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import  Window
from kivy.properties import ObjectProperty

class calculator(Widget):

    minu, km = ObjectProperty(None), ObjectProperty(None)

    def call(self):

        minu, km = float(self.minu.text), float(self.km.text)
        self.dict_result, result_over = {}, ''

        company = ('Traficar clio', 'MiiMove Astra', 'MiiMove Ampera', 'Panek economt sta', 
            'Panek economt kil', 'Panek economt min', 'Panek comfort sta', 'Panek comfort kil', 
            'Panek comfort min', '4mobility economy', '4mobility premium')
        price_star = (2.99, 0, 0, 0, 2.89, 2.89, 0, 2.89, 2.89, 0, 0)
        price_km = (1.5, 0.8, 0, 0.8, 0, 0.99, 0.82, 0, 1.29, 0.8, 0.8)
        price_min = (0, 0.67, 1.19, 0.55, 1.49, 0, 0.8, 1.99, 0, 0.5, 0.8)

        for a in range(0,11):
            self.algorithm(minu, km, company[a], price_star[a], price_km[a], price_min[a])
        
        result_over = min(self.dict_result, key=self.dict_result.get), + min(self.dict_result.values())

        self.ids.result.text = f"{result_over[0]} {result_over[1]}"
        print(result_over)
    
    def algorithm(self, time, distance, company, start, km, min):
        alg_result = round(time*min + distance*km + start, 2)
        self.dict_result[company] = alg_result

class price_car_sharing(App):
    def build(self):
        Window.clearcolor = (182/255, 66/255, 245/255, 1)
        return calculator()

if __name__ == '__main__':
    price_car_sharing().run()