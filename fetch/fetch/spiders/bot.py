import scrapy
import json
import time


def format_numerical(string):
    try:
        if string.strip() == "":
            return "0"
        else:
            return string.strip().replace(',', '')
    except AttributeError:
        return "NAN"


class Bot(scrapy.Spider):
    name = "bot"

    def start_requests(self):
        urls = [
            'https://www.worldometers.info/coronavirus/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        global_stats = response.css("div.maincounter-number span::text").getall()

        # global_cases = format_numerical(global_stats[0])
        # gloabl_deaths = format_numerical(global_stats[1])
        # global_recovered = format_numerical(global_stats[2])

        global_cases = 0
        gloabl_deaths = 0
        global_recovered = 0

        rows = {}

        for idx in range(1, 121):
            base_path = "/html/body/div[2]/div[3]/div/div[1]/table/tbody[1]/tr[{}]/td[{}]//text()"
            country = response.xpath(base_path.format(idx, 1)).getall()

            if len(country) == 3:
                country = country[1].strip()
            else:
                country = country[0].strip()

            if country == "Vatican City":
                continue

            total_cases = format_numerical(response.xpath(base_path.format(idx, 2)).get())
            new_cases = format_numerical(response.xpath(base_path.format(idx, 3)).get())
            total_deaths = format_numerical(response.xpath(base_path.format(idx, 4)).get())
            new_deaths = format_numerical(response.xpath(base_path.format(idx, 5)).get())
            total_recovered = format_numerical(response.xpath(base_path.format(idx, 6)).get())
            active_cases = format_numerical(response.xpath(base_path.format(idx, 7)).get())
            critical = format_numerical(response.xpath(base_path.format(idx, 8)).get())
            total_cases_by_1M = format_numerical(response.xpath(base_path.format(idx, 9)))
            death_rate = float(total_deaths) / int(total_cases) * 100.0
            death_rate = "%.2f" % death_rate

            global_cases += int(total_cases)
            gloabl_deaths += int(total_deaths)
            global_recovered += int(total_recovered)

            row = {
                'total_cases': total_cases,
                'new_cases': new_cases,
                'total_deaths': total_deaths,
                'new_deaths': new_deaths,
                'total_recovered': total_recovered,
                'active_cases': active_cases,
                'critical': critical,
                'total_cases_by_1M': total_cases_by_1M,
                'death_rate': death_rate,
            }

            rows[country] = row

        data = {
            'global_cases': global_cases,
            'gloabl_deaths': gloabl_deaths,
            'global_recovered': global_recovered,
            'countires': rows,
            'timestamp': time.time()
        }

        with open('../webapp/data.json', 'w') as outfile:
            json.dump(data, outfile)
