from flask import Flask, render_template, request

app = Flask(__name__)

import sys

def load(file):
    #Open a text file & turn contents into a list of lowercase strings
    with open(file) as in_file:
        loaded_txt = in_file.read().strip().split('\n')
        loaded_txt = [x.lower() for x in loaded_txt]
        return loaded_txt

word_list = load('file.txt')

#Get request to load index.html
#POST request to load solver.html
@app.route('/', methods=['GET', 'POST'])
@app.route('/anagrams/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #empty list to store answers in
        anagram_list = []
        #Get user input from text form
        value = request.form['letters']
        #sort the letters and convert to lowercase
        value = ''.join(sorted(value))
        value = value.lower()
        value_sorted = sorted(value)
        #Run through the dictionary file of sorted words in list format and compare with sorted user input 
        for word in word_list:
            word = word.lower()
            if word != value:
                if sorted(word) == value_sorted:        
                    anagram_list.append(word)
        return render_template('solver.html', myWords = anagram_list)  

#Run the app on port 80
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=80)
