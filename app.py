from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
    else:
        user = request.args.get('nm', default="Guest")  # Default to "Guest" if no name is provided
    
    if user:
        return redirect(url_for('success', name=user))
    else:
        return "Name is required!", 400  # Bad Request error if name is missing

if __name__ == '__main__':
    app.run(debug=True)
