from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
   return ("To use this api go to https://armstrong-nbr-finder.herokuapp.com/armstrong/ put whatever number you want to check for armstrong number after the / ")

@app.route('/armstrong/<int:n>')
def arm(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10
    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        return "True"
    else:
        print(f"{copy_n} is not an armstrong number")
        return "False"

    



if __name__ == "__main__":
    app.run(debug=False,port=8000)
   
    