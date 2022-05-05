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

@main.route('/science')
def science():
    science_news = get_articles('science')
    
    return render_template('science.html', science = science_news)

@main.route('/health')
def health():
    health_news = get_articles('health')
    
    return render_template('health.html', health = health_news)

@main.route('/general')
def general():
    general_news = get_articles('general')
    
    return render_template('general.html', general = general_news)

@main.route('/entertainment')
def entertainment():
    entertainment_news = get_articles('entertainment')
    
    return render_template('entertainment.html', entertainment = entertainment_news)