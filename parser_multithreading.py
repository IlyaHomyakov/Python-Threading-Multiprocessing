import bs4
import requests
import time
import threading
import csv


# 5.3s

def main():
    link = {'main': 'https://www.imdb.com/chart/moviemeter'}
    response = requests.get(link['main']).text

    films_info = open('films.csv', mode='w')
    films_info_writer = csv.writer(films_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    films_info_writer.writerow([])

    site = bs4.BeautifulSoup(response, 'html.parser')
    genres_html_cut = site.find_all('li', attrs={'class': 'subnav_item_main'})

    genres_list = []
    for genre in genres_html_cut:
        genres_list.append(genre.find('a', recursive=False).get_text().strip())

    genres_parsers_array = []
    for genre in genres_list:
        p = threading.Thread(target=parser_, args=[genre])
        genres_parsers_array.append(p)
        p.start()

    for process in genres_parsers_array:
        process.join()


def parser_(genre):
    top_films_link = f'https://www.imdb.com/search/title/?genres={genre}&genres={genre}&explore=title_type,' \
                     'genres&ref_=adv_explore_rhs'

    films_info = open('films.csv', mode='a')
    films_info_writer = csv.writer(films_info, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    try:
        response = requests.get(top_films_link).text
        films_page = bs4.BeautifulSoup(response, 'html.parser')

        titles_html_cut = films_page.find_all('h3', attrs={'class': 'lister-item-header'})
        for titles_cut in titles_html_cut:
            year = titles_cut.find('span', attrs={'class': 'lister-item-year text-muted unbold'},
                                   recursive=False).get_text()
            title = titles_cut.find('a', recursive=False).get_text().strip()

            films_info_writer.writerow([title, genre, year])
    except:
        return films_info_writer.writerow(['Something went wrong'])


if __name__ == '__main__':
    start_time = time.time()

    main()

    duration = time.time() - start_time
    print(f"Operation took {duration} seconds")
