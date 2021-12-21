from scrap import *

if __name__ == '__main__':
    p = Scrap()
    p.crawl()
    p.extract()
    p.format()
    p.save()