from kivy.utils import get_color_from_hex

# function for starting the main questions
def start_azla(self, Default, Colors):
# This method is called when the start button is pressed
     self.remove_widget(self.box_layout)

     # add the box for questions
     self.add_widget(self.box_question)
     self.box_question.add_widget(self.grid_layout_question)

     self.grid_layout_question.add_widget(self.seperator)
     self.grid_layout_question.add_widget(self.correct_label)
     # self.box_question.add_widget(self.incorrect_label)


     # Shows the first question
     for index, (key, value) in enumerate(Default.labels_widgets.items()):
         if index == 0:
            self.grid_layout_question.add_widget(value)
            value.color=(get_color_from_hex(Colors.label))
            value.font_size=25

         self.last = index

     # Adds the entry box and submit button to the window
     self.grid_layout_question.add_widget(self.entry_box)
     self.grid_layout_question.add_widget(self.submit_button)
     self.grid_layout_question.add_widget(self.seperator2)
