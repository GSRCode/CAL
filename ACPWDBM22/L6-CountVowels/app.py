from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate" , methods=['POST' , 'GET'])

def calculate():
    if request.method == 'POST' and 'input_string' in request.form:
        
        input_string = request.form.get('input_string')
        number_of_vowels = 0
        input_string.lower()
        
        for i in input_string.split():
            print(i)
            if(i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u'):
                number_of_vowels +=1
			
        return render_template('index.html',number_of_vowels=number_of_vowels)

@app.route('/')
def index():
	return render_template('index.html')