import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app  size
Window.size = (500,700)

# Designate our .kv design file
Builder.load_file('calc.kv')	



class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'
	
	# Create a butto pressing function
	def button_press(self, button):
		#
		prior = self.ids.calc_input.text

		# Test foor Error
		if "Error" in prior:
			prior = ''

		#
		if prior == "0": 
				self.ids.calc_input.text = ''
				self.ids.calc_input.text  = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	# Create function to remove last character
	def remove(self):
		prior = self.ids.calc_input.text
		# Removr the last item
		prior = prior[:-1]
		# ouput back to text box
		self.ids.calc_input.text = prior

	# Create function to maqke text box pos or neg
	def pos_neg(self):
		prior = self.ids.calc_input.text

		# test to see if there's a - sign or + sign
		if "-" in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'


	# Create decimal function
	def  dot(self):
		prior = self.ids.calc_input.text
		# Split out text box by +
		num_list = prior.split("+")


		if "+" in prior and "." not in num_list[-1]:
			# Ass a decimel to the end
			prior = f'{prior}.'
			# Output back to the text
			self.ids.calc_input.text = prior

		elif "." in prior:
			pass
		else:
			# Ass a decimel to the end
			prior = f'{prior}.'
			# Output back to the text
			self.ids.calc_input.text = prior


	def math_sign(self, sign):
		 # create variable
		prior = self.ids.calc_input.text
		 #
		self.ids.calc_input.text  = f'{prior}{sign}'



	def equals(self):
		prior = self.ids.calc_input.text
		# Error Handling         
		try:
        	# Evaluate the math from the textbox
			answer = eval(prior)
         	# Output the answer
			self.ids.calc_input.text = str(answer)
		except:
			self.ids.calc_input.text = "Error"
		'''
		 # Addition
		 if "+" in prior:
		 	num_list = prior.split("+")
		 	answer = 0.0
		 	# loop thru our list 
		 	for number in num_list:
		 		answer = answer + float(number)

		'''

class CalculatorApp(App):
	def build(self):
		return MyLayout()


if __name__== '__main__':
	CalculatorApp().run()

