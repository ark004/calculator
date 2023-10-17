from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CalculatorApp(App):                        #frame of kivy app
    def build(self):
        self.icon="calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = BoxLayout(orientation='vertical')

        
        self.solution = Button(
            # text="",
            background_color="black",
            size_hint=(1, .75),
            font_size=32,
            
        )
        self.result.add_widget(self.solution)    #keypad of calculator
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    
                    text=label,font_size=30, background_color="grey",
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.result.add_widget(h_layout)
        equals_button = Button(
            text="=",font_size=30, background_color="grey",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        self.result.add_widget(equals_button)
        return self.result

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if current == "0":
            self.solution.text = ""
        if button_text == "C":
            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

    def on_solution(self, instance):
        text = self.solution.text
        try:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
        except Exception:
            self.solution.text = "Error thambi "

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
