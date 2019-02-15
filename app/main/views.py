from flask import render_template
from . import main
from flask_login import login_required, current_user

# from app import app

@main.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/Funny',methods = ['GET', 'POST'])
@login_required
def Interview():

    pitch_form = PitchForm1()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_category('Funny')

    title = 'Funny'

    return render_template("Funny.html", pitch_form = pitch_form, pitches = all_pitches)

@main.route('/Pickuplines',methods = ['GET', 'POST'])
@login_required
def Pickuplines():

    pitch_form = PitchForm2()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_category('Pickuplines')

    title = 'Pickuplines'

    return render_template("Pickuplines.html", pitch_form = pitch_form, pitches = all_pitches)

@main.route('/Cheesy',methods = ['GET', 'POST'])
@login_required
def Cheesy():

    pitch_form = PitchForm3()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        #return redirect(url_for('index.html'))

    all_pitches = Pitch.get_category('Cheesy')

    title = 'Cheesy'

    return render_template("Cheesy.html", pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):

    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment Section'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)
