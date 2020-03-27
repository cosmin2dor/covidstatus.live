import scrapy
import json
import time

codes = {'Afghanistan': 'AF', 'Åland Islands': 'AX', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR', 'British Indian Ocean Territory': 'IO', 'Brunei': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cape Verde': 'CV', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos (Keeling) Islands': 'CC', 'Colombia': 'CO', 'Comoros': 'KM', 'Congo': 'CG', 'DRC': 'CD', 'Cook Islands': 'CK', 'Costa Rica': 'CR', "Côte d'Ivoire": 'CI', 'Croatia': 'HR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czechia': 'CZ', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET', 'Falkland Islands (Malvinas)': 'FK', 'Faeroe Islands': 'FO', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Heard Island and McDonald Islands': 'HM', 'Holy See (Vatican City State)': 'VA', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', "Korea, Democratic People's Republic of": 'KP', 'S. Korea': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', "Lao People's Democratic Republic": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO', 'North Macedonia': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia, Federated States of': 'FM', 'Moldova': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestine': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Réunion': 'RE', 'Romania': 'RO', 'Russia': 'RU', 'Rwanda': 'RW', 'Saint Barthélemy': 'BL', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Martin (French part)': 'MF', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Sint Maarten (Dutch part)': 'SX', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Swaziland': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Taiwan': 'TW', 'Tajikistan': 'TJ', 'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'UAE': 'AE', 'UK': 'GB', 'USA': 'US', 'United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela': 'VE', 'Vietnam': 'VN', 'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}
population = {'BD': '166368149', 'BE': '11498519', 'BF': '19751651', 'BG': '7036848', 'BA': '3503554', 'BB': '286388', 'WF': '11683', 'BL': '8450', 'BM': '61070', 'BN': '434076', 'BO': '11215674', 'BH': '1566993', 'BI': '11216450', 'BJ': '11485674', 'BT': '817054', 'JM': '2898677', 'BV': '0', 'BW': '2333201', 'WS': '197695', 'BQ': '24548', 'BR': '210867954', 'BS': '399285', 'JE': '166083', 'BY': '9452113', 'BZ': '382444', 'RU': '143964709', 'RW': '12501156', 'RS': '8762027', 'TL': '1324094', 'RE': '883247', 'TM': '5851466', 'TJ': '9107211', 'RO': '19580634', 'TK': '1319', 'GW': '1907268', 'GU': '165718', 'GT': '17245346', 'GS': '100', 'GR': '11142161', 'GQ': '1313894', 'GP': '449173', 'JP': '127185332', 'GY': '782225', 'GG': '66502', 'GF': '289763', 'GE': '3907131', 'GD': '108339', 'GB': '66573504', 'GA': '2067561', 'SV': '6411558', 'GN': '13052608', 'GM': '2163765', 'GL': '56565', 'GI': '34733', 'GH': '29463643', 'OM': '4829946', 'TN': '11659174', 'JO': '9903802', 'HR': '4164783', 'HT': '11112945', 'HU': '9688847', 'HK': '7428887', 'HN': '9417167', 'HM': '0', 'VE': '32381221', 'PR': '3659007', 'PS': '5052776', 'PW': '21964', 'PT': '10291196', 'SJ': '2667', 'PY': '6896908', 'IQ': '39339753', 'PA': '4162618', 'PF': '285859', 'PG': '8418346', 'PE': '32551815', 'PK': '200813818', 'PH': '106512074', 'PN': '54', 'PL': '38104832', 'PM': '6342', 'ZM': '17609178', 'EH': '567421', 'EE': '1306788', 'EG': '99375741', 'ZA': '57398421', 'EC': '16863425', 'IT': '59290969', 'VN': '96491146', 'SB': '623281', 'ET': '107534882', 'SO': '15181925', 'ZW': '16913261', 'SA': '33554343', 'ES': '46397452', 'ER': '5187948', 'ME': '629219', 'MD': '4041065', 'MG': '26262810', 'MF': '33100', 'MA': '36191805', 'MC': '38897', 'UZ': '32364996', 'MM': '53855735', 'ML': '19107706', 'MO': '632418', 'MN': '3121772', 'MH': '53167', 'MK': '2085051', 'MU': '1268315', 'MT': '432089', 'MW': '19164728', 'MV': '444259', 'MQ': '385065', 'MP': '55194', 'MS': '5203', 'MR': '4540068', 'IM': '84831', 'UG': '44270563', 'TZ': '59091392', 'MY': '32042458', 'MX': '130759074', 'IL': '8452841', 'FR': '65233271', 'IO': '3000', 'SH': '4074', 'FI': '5542517', 'FJ': '912241', 'FK': '2922', 'FM': '106227', 'FO': '49489', 'NI': '6284757', 'NL': '17110161', 'NO': '5353363', 'NA': '2587801', 'VU': '282117', 'NC': '279821', 'NE': '22311375', 'NF': '2210', 'NG': '195875237', 'NZ': '4749598', 'NP': '29624035', 'NR': '11312', 'NU': '1624', 'CK': '17411', 'CI': '24905843', 'CH': '8544034', 'CO': '49464683', 'CN': '1415045928', 'CM': '24678234', 'CL': '18197209', 'CC': '628', 'CA': '36953765', 'CG': '5399895', 'CF': '4737423', 'CD': '84004989', 'CZ': '10625250', 'CY': '1189085', 'CX': '2205', 'CR': '4953199', 'CW': '161577', 'CV': '553335', 'CU': '11489082', 'SZ': '1391385', 'SY': '18284407', 'SX': '40552', 'KG': '6132932', 'KE': '50950879', 'SS': '12919053', 'SR': '568301', 'KI': '118414', 'KH': '16245729', 'KN': '55850', 'KM': '832347', 'ST': '208818', 'SK': '5449816', 'KR': '51164435', 'SI': '2081260', 'KP': '25610672', 'KW': '4197128', 'SN': '16294270', 'SM': '33557', 'SL': '7719729', 'SC': '95235', 'KZ': '18403860', 'KY': '62348', 'SG': '5791901', 'SE': '9982709', 'SD': '41511526', 'DO': '10882996', 'DM': '74308', 'DJ': '971408', 'DK': '5754356', 'VG': '31719', 'DE': '82293457', 'YE': '28915284', 'DZ': '42008054', 'US': '326766748', 'UY': '3469551', 'YT': '259682', 'UM': '300', 'LB': '6093509', 'LC': '179667', 'LA': '6961210', 'TV': '11287', 'TW': '23694089', 'TT': '1372598', 'TR': '81916871', 'LK': '20950041', 'LI': '38155', 'LV': '1929938', 'TO': '109008', 'LT': '2876475', 'LU': '590321', 'LR': '4853516', 'LS': '2263010', 'TH': '69183173', 'TF': '140', 'TG': '7990926', 'TD': '15353184', 'TC': '35963', 'LY': '6470956', 'VA': '801', 'VC': '110200', 'AE': '9541615', 'AD': '76953', 'AG': '103050', 'AF': '36373176', 'AI': '15045', 'VI': '104914', 'IS': '337780', 'IR': '82011735', 'AM': '2934152', 'AL': '2934363', 'AO': '30774205', 'AQ': '0', 'AS': '55679', 'AR': '44688864', 'AU': '24772247', 'AT': '8751820', 'AW': '105670', 'IN': '1354051854', 'AX': '29013', 'AZ': '9923914', 'IE': '4803748', 'ID': '266794980', 'UA': '44009214', 'QA': '2694849', 'MZ': '30528673'}

def is_empty_string(string):
    if string is None:
        return True
    else:
        try:
            if string.strip() == "":
                return True
        except AttributeError:
            return False
    
    return False

def format_numerical(string):
    if is_empty_string(string):
        return 0
    else:
        return string.strip().replace(',', '').replace('-', '')

def sort_by_cases(data):
    sorted_keys = {}

    for k, v in data.items():
        sorted_keys[v['total_cases']] = k

    sorted_dict = {}

    for key in reversed(sorted(sorted_keys.keys())):
        k = sorted_keys[key]
        sorted_dict[k] = data[k]

    return sorted_dict

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

        global_cases = format_numerical(global_stats[0])
        gloabl_deaths = format_numerical(global_stats[1])
        global_recovered = format_numerical(global_stats[2])

        rows = {}

        for idx in range(1, 185):
            base_path = "/html/body/div[2]/div[3]/div[1]/div/div[1]/div/table/tbody[1]/tr[{}]/td[{}]//text()"
            country_name = response.xpath(base_path.format(idx, 1)).getall()

            if len(country_name) == 3:
                country_name = country_name[1].strip()
            else:
                country_name = country_name[0].strip()

            try:
                country_code = codes[country_name]
            except KeyError:
                country_code = None

            try:
                country_population = int(population[country_code])
            except KeyError:
                country_population = None

            total_cases = int(format_numerical(response.xpath(base_path.format(idx, 2)).get()))
            new_cases = int(format_numerical(response.xpath(base_path.format(idx, 3)).get()))
            total_deaths = int(format_numerical(response.xpath(base_path.format(idx, 4)).get()))
            new_deaths = int(format_numerical(response.xpath(base_path.format(idx, 5)).get()))
            total_recovered = int(format_numerical(response.xpath(base_path.format(idx, 6)).get()))
            active_cases = int(format_numerical(response.xpath(base_path.format(idx, 7)).get()))
            critical = int(format_numerical(response.xpath(base_path.format(idx, 8)).get()))
            total_cases_by_1M = float(format_numerical(response.xpath(base_path.format(idx, 9)).get()))

            try:
                total_cases_by_population = int((float(total_cases) / country_population) * 1000000.0)
            except TypeError:
                total_cases_by_population = None


            print("country={}, total_cases={}, new_cases={}, total_deaths={}, new_deaths={}, total_recovered={}, active_cases={}, critical={}, population={}, total_cases_by_1M={}, total_cases_by_population={}".format(
                country_name, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, critical, country_population, total_cases_by_1M, total_cases_by_population
            ))
            
            death_rate = float(total_deaths) / int(total_cases) * 100.0
            death_rate = "%.2f" % death_rate

            row = {
                'country_name': country_name,
                'total_cases': total_cases,
                'new_cases': new_cases,
                'total_deaths': total_deaths,
                'new_deaths': new_deaths,
                'total_recovered': total_recovered,
                'active_cases': active_cases,
                'critical': critical,
                'total_cases_by_1M': total_cases_by_1M,
                'death_rate': death_rate,
                'total_cases_by_population': total_cases_by_population,
            }

            rows[country_code] = row

        rows = sort_by_cases(rows)

        data = {
            'global_cases': global_cases,
            'gloabl_deaths': gloabl_deaths,
            'global_recovered': global_recovered,
            'countires': rows,
            'timestamp': time.time()
        }

        with open('../webapp/data.json', 'w') as outfile:
            json.dump(data, outfile)
