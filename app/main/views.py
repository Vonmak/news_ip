from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_sources


#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page data
    '''
    sourceList = get_sources()
    
    title= 'The News center'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title= title, sourceList= sourceList)


@main.route('/business')
def business():
    business_news = get_articles('business')
    
    return render_template('business.html', business = business_news)

@main.route('/technology')
def technology():
    technology_news = get_articles('technology')
    
    return render_template('technology.html', technology = technology_news)
     
@main.route('/sports')
def sports():
    sports_news = get_articles('sports')
    
    return render_template('sports.html', sports = sports_news)

