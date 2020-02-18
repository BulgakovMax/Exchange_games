import os
from functools import wraps

import requests
from bs4 import BeautifulSoup
from flask import session


def check_login(f):
    """
    This decorator will check your logged_in parameter from session
    if it false you will see msg "You must login to see this page"
    if it true you will see the content of your page

    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        if session.get("logged_in"):
            func = f(*args, **kwargs)
        else:
            return "You must login to see this page"
        return func

    return wrapper


def upload_image(request_files):
    if request_files:
        image = request_files
        image.save(os.path.join('static/img', image.filename))
        return image.filename
    else:
        return 'no_image.jpg'


def pars_automation():
    games = []
    for i in range(11):
        games.extend(parse_table(i))
    return games


def parse_table(value):
    html_doc = requests.get(
        f"https://boardgamegeek.com/browse/boardgame/page/{value}?sort=rank")
    soup = BeautifulSoup(html_doc.content, 'html.parser')
    collection_table = soup.find('table', {'class': 'collection_table'})
    rows = collection_table.find_all('tr')
    games = []
    for row in rows:
        collection_thumbnail = row.find(
            'td', {'class': 'collection_thumbnail'})
        if collection_thumbnail and collection_thumbnail.find('a') and collection_thumbnail.find('a').find('img'):
            image = collection_thumbnail.find('a').find('img')['src']
        td = row.find_all('td')
        if td:
            game_name = td[2].find('a').text.strip()
            game_link = td[2].find('a')['href']
        collection_bggrating = row.find_all(
            'td', {'class': 'collection_bggrating'})
        collection_rank = row.find_all(
            'td', {'class': 'collection_rank'})
        if collection_bggrating:
            geek_rating = collection_bggrating[0].text.strip()
            avg_rating = collection_bggrating[1].text.strip()
            num_voters = collection_bggrating[2].text.strip()
            games.append({
                'name': game_name,
                'link': game_link,
                'image': image,
                'rank_bgg': collection_rank[0].find('a')['name'],
                'geek_rating': geek_rating,
                'avg_rating': avg_rating,
                'num_voters': num_voters,
            })
    return games
