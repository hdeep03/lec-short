from flask import Flask, render_template, request, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
from process import process
from secrets import token_hex

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)


class ProcessForm(FlaskForm):
    ytlink = StringField('Youtube Link', validators=[DataRequired(), URL()])
    speed  = FloatField('Speed')
    cratio = SelectField('Selectivity', choices=[(0.3, 'High'), (0.5, 'Mid'), (0.7, 'Low')])
    submit = SubmitField('Shorten!')
    

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProcessForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)

    url = form.ytlink.data
    speed = form.speed.data
    cratio = float(form.cratio.data)
    print(f'Request: url = {url}| speed = {speed}| cratio={cratio}')

    try:
        result = process(url, cratio, speed)
    except:
        form = ProcessForm()
        return render_template('index.html', form=form, error='An error has occured. Please check parameters')

    return send_file(result, as_attachment=True)

if __name__ == '__main__':
    app.run(port=3001, debug=True)
