from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Amreeta'}
    listings = [
        {'title': 'RTX 5080', 'price': '£1,030'},
        {'title': 'Nikon D6 camera', 'price': '£1,800'},
        {'title': 'Samsung S22 Ultra', 'price': '£300'},
        {'title': '32GB (2x16GB) Corsair Vengeance DDR5 6000MHz CL32', 'price': '£69.95'},
        ]
    return render_template('index.html', title='Home', listings=listings, user=user)
