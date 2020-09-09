from flask import Flask, render_template, flash, redirect
from forms import InsertHours

app = Flask(__name__)
app.config['SECRET_KEY'] = "tuesdays-are-whack"

@app.route('/uwu')
def main():
    return "Dab"

@app.route('/form')
def login():
    form = InsertHours()
    if form.validate_on_submit():
        flash('Change requested by user {} {}'.format(
            form.admin_first_name.data, form.admin_last_name.data))
        return redirect('/uwu')
    return render_template('form.html', title='Dab Again', form=form)