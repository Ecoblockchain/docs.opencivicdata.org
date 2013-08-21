from pupa.scrape import Jurisdiction

from .people import PersonScraper


class Example(Jurisdiction):
    jurisdiction_id = 'ocd-jurisdiction/country:us/state:nm/place:albequerque/council'

    def get_metadata(self):
        return {
            'name': 'Albequerque City Council',
            'legislature_name': 'Albequerque City Council',
            'legislature_url': 'http://www.cabq.gov/council/',
            'terms': [{
                'name': '2013-2015',
                'start_year': 2013,
                'end_year': 2015,
                'sessions': ['2013'],
                }],
            'provides': ['people'],
            'session_details': {
                '2013': {'_scraped_name': '2013'}
                },
            'feature_flags': [],
               }

    def get_scraper(self, term, session, scraper_type):
        if scraper_type == 'people':
            return PersonScraper

    def scrape_session_list(self):
        return ['2013']

