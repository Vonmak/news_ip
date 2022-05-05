from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_sources


#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page data
    '''
    sourceSamples =get_sources()
    # print(sourceList)
    
    title= 'The News center'
    
    return render_template('index.html', title= title, sourceList= sourceSamples)


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

