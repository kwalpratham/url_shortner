from datetime import datetime
from core.models import ShortUrls
from core import app, db
from flask import render_template, request, flash, redirect, url_for
from .manager import Manager

manage = Manager()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        # In case of null entry
        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))


        elif short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Please enter different custom id!')
            return redirect(url_for('index'))
        
        # known url
        url_object = ShortUrls.query.filter_by(original_url=url).first()
        if url_object is not None:
            short_id = url_object.short_id
            hits = url_object.hits
            short_url = request.host_url + short_id
            return render_template('index.html', data=[short_url, hits])

        # generate a url hash
        elif not short_id:
            short_id = manage.generate_short_id() # type: ignore

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    # if request.method == 'GET':
    #     # short_id = request.form.get('short_url')
    #     # link = ShortUrls.query.filter_by(short_id=short_id).first()
    #     link = None
    #     if link:
    #         return render_template('index.html', hits=link.hits, short_url=link.short_id, original_url=link.original_url)
        
    #     else:
    #         flash('Invalid URL')
    #         return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        link.hits += 1
        db.session.commit()
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

# @app.route('/info/<short_id>')
# def analytics(short_id):
#     link = ShortUrls.query.filter_by(short_id=short_id).first()
#     if link:
#         return render_template('index.html', hits=link.hits, short_url=link.short_id, original_url=link.original_url)
    
#     else:
#         flash('Invalid URL')
#         return redirect(url_for('index'))