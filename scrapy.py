#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from redisworks import Root
import random
import threading
import dryscrape
import time
color = ["#D1F1FE", "#FEEBD1", "#FED1D1", "#E4FED1",
         "#D1FEFA", "#D1D1FE", "#FED1F9", "#FCFED1", ]
root = Root(host='0.0.0.0', port=6379, db=0)


class FetchData(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G"
        self.session = dryscrape.Session()

    def run(self):
        try:
            while True:
                self.session.visit(self.url)
                page = self.session.body()
                soup = BeautifulSoup(page, "html.parser")
                table = soup.find('table', id="topGainers")
                tbody = table.find('tbody')
                rows = tbody.find_all('tr')
                heading = [th.text for th in rows[0].find_all('th')]
                data = list()
                for row in rows:
                    cols = {head: cell.text.strip()
                            for head, cell in zip(heading, row.find_all('td'))}
                    cols['color'] = random.choice(color)
                    if len(cols) > 1:
                        data.append(cols)
                root.data = data
                time.sleep(300)
        except Exception as e:
            print "Cannot fetch data"
            print str(type(e).__name__), str(e)
