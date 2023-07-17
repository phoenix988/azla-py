# Imports all the kivy classes
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.lang import Builder

# Imports question Class
from src.mainQuestion import Question
from src.function.start import start_azla

# Import colors
from src.colors import Colors, Size

# Sets word files options
option_widgets = Question.word_options()

# Class for default options
class Default():
    # some default values
    choice_name = "basic"
    choice = Question.run("basic")
    labels_widgets, correct, word = Question.widget(choice)
    correct_count = Question.correct
    incorrect_count = Question.incorrect


# The main class for the main Screen
class AzlaMain(BoxLayout):
    # Keep track of the number of questions
    count = 0
    last = 0
    
    # Create boxes
    box_layout = BoxLayout(orientation='vertical', spacing = 40)
    box_setting = BoxLayout(orientation='vertical')
    box_question = BoxLayout(orientation='vertical', spacing = 100,)
    box_label = BoxLayout(orientation='horizontal', spacing = 100,)
    
    # Create buttons
    start_button = Button(text='Start',  background_color=get_color_from_hex(Colors.bg), font_size = Size.normal)
    exit_button = Button(text='Exit',  background_color=get_color_from_hex(Colors.bg), font_size = Size.normal)
    next_button = Button(text='Next', size_hint=(0.3, 0.05), pos_hint={'center_x': 0.5, 'center_y': 1}, background_color=get_color_from_hex(Colors.bg))
    back_button = Button(text='Back', background_color=get_color_from_hex(Colors.bg))
    result_button = Button(text='Show Result', size_hint=(0.3, 0.05), pos_hint={'center_x': 0.5, 'center_y': 1}, background_color=get_color_from_hex(Colors.bg))
    submit_button = Button(text='Submit', size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 1}, background_color=get_color_from_hex(Colors.bg))
    setting_button = Button(text='Setting', background_color=get_color_from_hex(Colors.bg), font_size = Size.normal)
    
    # Create entry box
    entry_box = TextInput(multiline=False, size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1},
                          font_size = Size.normal, border = (2, 2, 2, 2), size=(200,30))
    
    # Create correct label
    correct_label = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, color=get_color_from_hex(Colors.correct), font_size= Size.normal)
    incorrect_label = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, color=get_color_from_hex(Colors.incorrect), font_size= Size.normal)
    end_label = Label(text='You have reached the end', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, color=get_color_from_hex(Colors.incorrect), font_size= Size.normal)
    end_label_correct = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, color=get_color_from_hex(Colors.incorrect), font_size= Size.normal)
    end_label_incorrect = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1}, color=get_color_from_hex(Colors.incorrect), font_size= Size.normal)
    
    # Create seperator widgets
    seperator = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
    seperator2 = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})
    seperator3 = Label(text='', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})

    # Create a drop-down widget
    dropdown = DropDown()

    # Create images
    main_image = Image(source='images/flag.jpg')
    sec_image = Image(source='images/flag.jpg', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})

    # Create grid layout
    grid_layout = GridLayout(cols=1)
    grid_layout_main = GridLayout(cols=1, spacing = 5)
    grid_layout_question = GridLayout(cols=1, spacing = 10)
    grid_layout_end = GridLayout(cols=1, spacing = 0)

    # Default function for the class
    def __init__(self, **kwargs):
        super(AzlaMain, self).__init__(**kwargs)
        Window.clearcolor = get_color_from_hex(Colors.bg)
        # Create drop down button
        self.dropdown_word = Button(text='Choose WordList',on_release=self.open_dropdown_word, background_color=get_color_from_hex(Colors.bg), font_size= Size.normal)
        self.dropdown_word.text=f'{Default.choice_name} wordlist selected'

        # Create a label widget to display the selected item
        self.selected_label = Label(text='Selected:')

        # Create a start button
        self.start_button.bind(on_press=self.start_button_pressed)
        self.exit_button.bind(on_press=self.exit_button_pressed)
        self.next_button.bind(on_press=self.next_button_pressed)
        self.entry_box.bind(on_text_validate=self.on_enter)
        self.submit_button.bind(on_press=self.submit_button_pressed)
        self.result_button.bind(on_press=self.result_button_pressed)
        self.setting_button.bind(on_press=self.setting_button_pressed)
        

        # Add the items to the drop-down
        for key, value in option_widgets.items():
            value.background_color=(get_color_from_hex(Colors.bg))
            value.color=(get_color_from_hex(Colors.label))
            value.bind(on_release=lambda btn: self.select_word(btn.text))
            self.dropdown.add_widget(value)

        # Loop through all values in the Colors class
        # Creating setting panel
        for color_name, color_value in vars(Colors).items():
            if not color_name.startswith("__"):  # Exclude built-in attributes
                label = Label(text=color_name, size_hint=(None, None), size=(100, 30),  pos_hint={'center_x': 0.5, 'center_y': 0.1})
                label.color=(get_color_from_hex(Colors.label))
                label.font_size = Size.normal
                entry = TextInput(multiline=False,
                          font_size = Size.normal, border = (2, 2, 2, 2), size=(100, 30))
                entry.text = color_value
                self.grid_layout.add_widget(label)
                self.grid_layout.add_widget(entry)
 
        self.grid_layout.add_widget(self.back_button)

        self.grid_layout_main.add_widget(self.main_image)
        self.grid_layout_main.add_widget(self.dropdown_word)
        self.grid_layout_main.add_widget(self.start_button)
        self.grid_layout_main.add_widget(self.setting_button)
        self.grid_layout_main.add_widget(self.exit_button)

        self.grid_layout_question.add_widget(self.sec_image)

        self.box_layout.add_widget(self.grid_layout_main)

        # Add the start button to the layout
        self.add_widget(self.box_layout)

    # Runs when you press enter after writing your answer
    def on_enter(self, instance):
        # This method is called when the user presses the Enter key in the entry box
        print('Entered text:', self.entry_box.text)

    # Function to open dropdown menu for diffrent word lists
    def open_dropdown_word(self, instance):
        self.dropdown.open(instance)

    # Function to run when you select word option
    def select_word(self, item_text):
        self.selected_label.text = f"Selected: {item_text}"
        Default.choice = Question.run(item_text)
        Default.labels_widgets, Default.correct, Default.word = Question.widget(Default.choice)
        self.dropdown_word.text=f'{item_text} wordlist selected'

        self.dropdown.dismiss()

    # Start button function
    def start_button_pressed(self, instance):
        # This method is called when the start button is pressed
        start_azla(self, Default, Colors)

    def setting_button_pressed(self, instance):
        self.remove_widget(self.box_layout)
        self.add_widget(self.box_setting)
        self.box_setting.add_widget(self.grid_layout)
        

    # Exit button function
    def exit_button_pressed(self, instance):
        print("Exit button pressed!")

    # Submit button function
    def submit_button_pressed(self, instance):
        self.grid_layout_question.remove_widget(self.submit_button)
        self.grid_layout_question.remove_widget(self.entry_box)
        self.grid_layout_question.remove_widget(self.seperator2)
        self.grid_layout_question.add_widget(self.next_button)
        self.grid_layout_question.add_widget(self.seperator2)
        for index, (key, value) in enumerate(Default.correct.items()):
            if index == self.count:
                correct = value

        for index, (key, value) in enumerate(Default.labels_widgets.items()):
            if index == self.count:
               self.grid_layout_question.remove_widget(value)
               last = index + 1


        # Gets your choice
        choice = self.entry_box.text
 
        # Empty the entry box for the next question
        self.entry_box.text = ''

        if choice == correct:
            Default.correct_count = Default.correct_count + 1
            self.correct_label.text="Answer is correct!"
            self.correct_label.color=get_color_from_hex(Colors.correct)
        else:
            Default.incorrect_count = Default.incorrect_count + 1
            self.correct_label.text=f"Answer is incorrect!\nCorrect answer is {correct}"
            self.correct_label.color=get_color_from_hex(Colors.incorrect)


        # Prints your result in the end
        if self.count == self.last:
            self.grid_layout_question.remove_widget(self.correct_label)
            self.grid_layout_question.remove_widget(self.next_button)
            self.grid_layout_question.remove_widget(self.seperator)
            self.grid_layout_question.remove_widget(self.seperator2)
            self.grid_layout_question.add_widget(self.seperator)
            self.grid_layout_question.add_widget(self.correct_label)
            self.grid_layout_question.add_widget(self.result_button)
            self.grid_layout_question.add_widget(self.seperator2)
            print(f'Correct answers: {Default.correct_count}')
            print(f'Incorrect answers: {Default.incorrect_count}')

        self.count = self.count + 1


    # Function when you click on the next button
    def next_button_pressed(self, instance):
        self.grid_layout_question.remove_widget(self.next_button)
        self.grid_layout_question.remove_widget(self.entry_box)
        self.grid_layout_question.remove_widget(self.seperator2)
        self.correct_label.text=""
        self.incorrect_label.text=""

        # shows the next question
        for index, (key, value) in enumerate(Default.labels_widgets.items()):
            if index == self.count:
               self.grid_layout_question.add_widget(value)
               value.color=(get_color_from_hex(Colors.label))
               value.font_size=25

               # If you have reached the last question then it will show no entry box and buttons
               if value == None:
                  self.grid_layout_question.remove_widget(self.entry_box)
                  self.grid_layout_question.remove_widget(self.submit_button)
                  self.grid_layout_question.remove_widget(self.seperator2)
               else:
                  self.grid_layout_question.add_widget(self.entry_box)
                  self.grid_layout_question.add_widget(self.submit_button)
                  self.grid_layout_question.add_widget(self.seperator2)
    
    def result_button_pressed(self, instance):
        self.grid_layout_question.remove_widget(self.correct_label)
        self.grid_layout_question.remove_widget(self.result_button)
        self.grid_layout_question.remove_widget(self.seperator)
        self.grid_layout_question.remove_widget(self.seperator2)
        
        self.grid_layout_question.add_widget(self.seperator)
        self.grid_layout_question.add_widget(self.end_label_correct)
        self.grid_layout_question.add_widget(self.end_label_incorrect)
        

        self.end_label_correct.text = f'Correct: {Default.correct_count}\nIncorrect: {Default.incorrect_count}'
        self.end_label_correct.color = get_color_from_hex(Colors.label)



# Builder.load_file('azlamain.kv')

# Class to start the app
class Azla(App):
    def build(self):
        return AzlaMain()

# Starts the main application
if __name__ == '__main__':
    Azla().run()
