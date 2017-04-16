from flask import render_template
from app import t_app
from app.forms import ModifyImage


@t_app.route('/')
@t_app.route('/index')
def index():
    return render_template('index.html')

@t_app.route('/search', methods=['GET', 'POST'])
def search():
    info = None
    form = ModifyImage()
    if form.validate_on_submit():
        image_loc = form.image_loc.data
    return render_template('search.html', title='Image It', form=form, info=info)
