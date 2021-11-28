import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

kivy.require('2.0.0')

def alcohol_in_g(alcohol_in_ml):
    return alcohol_in_ml * 0.789

class MyGridLayout(Widget):

    bodyweight = ObjectProperty(None)
    normal_beer = ObjectProperty(None)
    strong_beer = ObjectProperty(None)
    shots = ObjectProperty(None)
    wine = ObjectProperty(None)
    cocktail = ObjectProperty(None)
    hours = ObjectProperty(None)
    button = ObjectProperty(None)

    def calculate(self):
        
        # Get the values from the text boxes
        try:
            bodyweight = int(self.bodyweight.text)
        except:
            bodyweight = 0
        try:
            beer = int(self.normal_beer.text)
        except:
            beer = 0
        try:
            strong_beer = int(self.strong_beer.text)
        except:
            strong_beer = 0
        try:
            shot = int(self.shots.text)
        except:
            shot = 0
        try:
            wine = int(self.wine.text)
        except:
            wine = 0
        try:
            cocktail = int(self.cocktail.text)
        except:
            cocktail = 0
        try:
            rtd = int(self.rtd.text)
        except:
            rtd = 0
        try: 
            hours = int(self.hours.text)
        except:
            hours = 0
        
        try:
            # Calculate the alcohol in grams
            if (self.ids.spinner_id.text) == "Man":
                procent = 0.70
            elif (self.ids.spinner_id.text) == "Woman":
                procent = 0.60

            alcohol = (alcohol_in_g(beer * (3.3*4.6)) + 
            alcohol_in_g(strong_beer*(3.3*5.8)) + 
            alcohol_in_g(wine*(1.2*12)) + 
            alcohol_in_g(cocktail*(3.3*4.5)) + 
            alcohol_in_g(shot*(0.4*40)) + 
            alcohol_in_g(rtd*(27.5*5)))

            alcohol_consumed = round(alcohol / (bodyweight*procent)-(0.15*hours), 2)
            if alcohol_consumed < 0:
                alcohol_consumed = 0

            # Show result on the button
            self.ids.button.text = str(alcohol_consumed)
        except Exception:
            self.ids.button.text = "Error, please correct your input"

class HowDrunkAmIApp(App):
    def build(self):
        HowDrunkAmIApp.title = "How Drunk Am I?"
        return MyGridLayout()

if __name__ == "__main__":
    HowDrunkAmIApp().run()