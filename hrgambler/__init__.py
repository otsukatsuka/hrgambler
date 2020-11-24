from hrgambler.crawler.race_result_crawler_builder import RaceResultCrawlerBuilder
from hrgambler.crawler.horse_db_crawler_builder import HorseDBCrawlerBuilder
from hrgambler.crawler.director import Director

from hrgambler.core import const

if __name__ == '__main__':
    const.HORSE_ID_URL_INDEX = 7
    const.RACE_ID_URL_INDEX = 6

    # builder = RaceResultCrawlerBuilder()
    # director = Director(builder)
    # race_id = '201905050811'
    # director.construct(output_path='{}.csv'.format(race_id), race_id=race_id)

    builder = HorseDBCrawlerBuilder()
    director = Director(builder)
    horse_id = '2014106083'
    director.construct(output_path='{}.csv'.format(horse_id), horse_id=horse_id)
