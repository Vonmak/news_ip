from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_sources


#views
@main.app.route('/')
def index():
    '''
    view root page function that returns the index page data
    '''
    sourceSamples = get_sources()
    
    title= 'The News center'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title= title, sourceList= sourceSamples)
