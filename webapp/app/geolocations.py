from geopy.geocoders import Nominatim
import numpy as np

d = {'China': {'lat': 35.000074, 'lon': 104.999927}, 'Italy': {'lat': 42.6384261, 'lon': 12.674297},
     'Iran': {'lat': 32.6475314, 'lon': 54.5643516}, 'S. Korea': {'lat': 36.638392, 'lon': 127.6961188},
     'Spain': {'lat': 39.3262345, 'lon': -4.8380649}, 'Germany': {'lat': 51.0834196, 'lon': 10.4234469},
     'France': {'lat': 46.603354, 'lon': 1.8883335}, 'USA': {'lat': 39.7837304, 'lon': -100.4458825},
     'Switzerland': {'lat': 46.7985624, 'lon': 8.2319736}, 'UK': {'lat': 54.7023545, 'lon': -3.2765753},
     'Norway': {'lat': 60.5000209, 'lon': 9.0999715}, 'Netherlands': {'lat': 52.5001698, 'lon': 5.7480821},
     'Sweden': {'lat': 59.6749712, 'lon': 14.5208584}, 'Belgium': {'lat': 50.6402809, 'lon': 4.6667145},
     'Denmark': {'lat': 55.670249, 'lon': 10.3333283}, 'Austria': {'lat': 47.2000338, 'lon': 13.199959},
     'Japan': {'lat': 36.5748441, 'lon': 139.2394179}, 'Diamond Princess': {'lat': 53.8953584, 'lon': 27.5554078},
     'Malaysia': {'lat': 4.5693754, 'lon': 102.2656823}, 'Qatar': {'lat': 25.3336984, 'lon': 51.2295295},
     'Canada': {'lat': 61.0666922, 'lon': -107.9917071}, 'Greece': {'lat': 38.9953683, 'lon': 21.9877132},
     'Australia': {'lat': -24.7761086, 'lon': 134.755}, 'Portugal': {'lat': 40.0332629, 'lon': -7.8896263},
     'Finland': {'lat': 63.2467777, 'lon': 25.9209164}, 'Singapore': {'lat': 1.357107, 'lon': 103.8194992},
     'Slovenia': {'lat': 45.8133113, 'lon': 14.4808369}, 'Israel': {'lat': 31.5313113, 'lon': 34.8667654},
     'Brazil': {'lat': -10.3333333, 'lon': -53.2}, 'Iceland': {'lat': 64.9841821, 'lon': -18.1059013},
     'Ireland': {'lat': 52.865196, 'lon': -7.9794599}, 'Hong Kong': {'lat': 22.2793278, 'lon': 114.1628131},
     'Philippines': {'lat': 12.7503486, 'lon': 122.7312101}, 'Egypt': {'lat': 26.2540493, 'lon': 29.2675469},
     'Poland': {'lat': 52.215933, 'lon': 19.134422}, 'Iraq': {'lat': 33.0955793, 'lon': 44.1749775},
     'Saudi Arabia': {'lat': 25.6242618, 'lon': 42.3528328}, 'Thailand': {'lat': 14.8971921, 'lon': 100.83273},
     'India': {'lat': 22.3511148, 'lon': 78.6677428}, 'Kuwait': {'lat': 29.2733964, 'lon': 47.4979476},
     'Lebanon': {'lat': 33.8750629, 'lon': 35.843409}, 'UAE': {'lat': 49.4871968, 'lon': 31.2718321},
     'Luxembourg': {'lat': 49.8158683, 'lon': 6.1296751}, 'Peru': {'lat': -6.8699697, 'lon': -75.0458515},
     'Russia': {'lat': 64.6863136, 'lon': 97.7453061}, 'Slovakia': {'lat': 48.7411522, 'lon': 19.4528646},
     'South Africa': {'lat': -28.8166236, 'lon': 24.991639}, 'Vietnam': {'lat': 13.2904027, 'lon': 108.4265113},
     'Pakistan': {'lat': 30.3308401, 'lon': 71.247499}, 'Bulgaria': {'lat': 42.6073975, 'lon': 25.4856617},
     'Croatia': {'lat': 45.5643442, 'lon': 17.0118954}, 'Algeria': {'lat': 28.0000272, 'lon': 2.9999825},
     'Serbia': {'lat': 44.024322850000004, 'lon': 21.07657433209902}, 'Panama': {'lat': 8.559559, 'lon': -81.1308434},
     'Mexico': {'lat': 19.4326296, 'lon': -99.1331785}, 'Albania': {'lat': 41.000028, 'lon': 19.9999619},
     'Ecuador': {'lat': -1.3397668, 'lon': -79.3666965}, 'Costa Rica': {'lat': 10.2735633, 'lon': -84.0739102},
     'Colombia': {'lat': 2.8894434, 'lon': -73.783892}, 'Georgia': {'lat': 32.3293809, 'lon': -83.1137366},
     'Hungary': {'lat': 47.1817585, 'lon': 19.5060937}, 'Latvia': {'lat': 56.8406494, 'lon': 24.7537645},
     'Morocco': {'lat': 31.1728205, 'lon': -7.3362482}, 'Armenia': {'lat': 40.7696272, 'lon': 44.6736646},
     'Senegal': {'lat': 14.4750607, 'lon': -14.4529612},
     'Bosnia and Herzegovina': {'lat': 44.3053476, 'lon': 17.5961467},
     'Moldova': {'lat': 47.2879608, 'lon': 28.5670941}, 'Oman': {'lat': 21.0000287, 'lon': 57.0036901},
     'Malta': {'lat': 35.8885993, 'lon': 14.4476911}, 'Tunisia': {'lat': 33.8439408, 'lon': 9.400138},
     'Sri Lanka': {'lat': 7.5554942, 'lon': 80.7137847}, 'Turkey': {'lat': 38.9597594, 'lon': 34.9249653},
     'Venezuela': {'lat': 8.0018709, 'lon': -66.1109318}, 'Lithuania': {'lat': 55.3500003, 'lon': 23.7499997},
     'Maldives': {'lat': 4.7064352, 'lon': 73.3287853}, 'Cambodia': {'lat': 13.5066394, 'lon': 104.869423},
     'Dominican Republic': {'lat': 19.0974031, 'lon': -70.3028026},
     'Faeroe Islands': {'lat': 62.0448724, 'lon': -7.0322972}, 'Jordan': {'lat': 31.1667049, 'lon': 36.941628},
     'Jamaica': {'lat': 18.1152958, 'lon': -77.1598454610168}, 'Martinique': {'lat': 14.6113732, 'lon': -60.9620777},
     'Kazakhstan': {'lat': 47.2286086, 'lon': 65.2093197}, 'New Zealand': {'lat': -41.5000831, 'lon': 172.8344077},
     'Liechtenstein': {'lat': 47.1416307, 'lon': 9.5531527}, 'Paraguay': {'lat': -23.3165935, 'lon': -58.1693445},
     'Réunion': {'lat': -21.1309332, 'lon': 55.5265771}, 'Uruguay': {'lat': -32.8755548, 'lon': -56.0201525},
     'Andorra': {'lat': 42.5407167, 'lon': 1.5732033}, 'Bangladesh': {'lat': 24.4768598, 'lon': 90.2932299},
     'Rwanda': {'lat': -1.9646631, 'lon': 30.0644358}, 'Guyana': {'lat': 4.8417097, 'lon': -58.6416891},
     'Cameroon': {'lat': 4.6125522, 'lon': 13.1535811}, 'Cuba': {'lat': 23.0131338, 'lon': -80.8328748},
     'Ethiopia': {'lat': 10.2116702, 'lon': 38.6521203}, 'Uzbekistan': {'lat': 41.32373, 'lon': 63.9528098},
     'Ukraine': {'lat': 49.4871968, 'lon': 31.2718321}, 'Channel Islands': {'lat': 60.6167942, 'lon': -145.7996671}
}

codes = {'Afghanistan': 'AF', 'Åland Islands': 'AX', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia, Plurinational State of': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR', 'British Indian Ocean Territory': 'IO', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cape Verde': 'CV', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos (Keeling) Islands': 'CC', 'Colombia': 'CO', 'Comoros': 'KM', 'Congo': 'CG', 'Congo, the Democratic Republic of the': 'CD', 'Cook Islands': 'CK', 'Costa Rica': 'CR', "Côte d'Ivoire": 'CI', 'Croatia': 'HR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czech Republic': 'CZ', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET', 'Falkland Islands (Malvinas)': 'FK', 'Faroe Islands': 'FO', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Heard Island and McDonald Islands': 'HM', 'Holy See (Vatican City State)': 'VA', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran, Islamic Republic of': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', "Korea, Democratic People's Republic of": 'KP', 'Korea, Republic of': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', "Lao People's Democratic Republic": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO', 'Macedonia, the Former Yugoslav Republic of': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia, Federated States of': 'FM', 'Moldova, Republic of': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestine, State of': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Réunion': 'RE', 'Romania': 'RO', 'Russian Federation': 'RU', 'Rwanda': 'RW', 'Saint Barthélemy': 'BL', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Martin (French part)': 'MF', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Sint Maarten (Dutch part)': 'SX', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Swaziland': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Taiwan, Province of China': 'TW', 'Tajikistan': 'TJ', 'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates': 'AE', 'United Kingdom': 'GB', 'United States': 'US', 'United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela, Bolivarian Republic of': 'VE', 'Viet Nam': 'VN', 'Virgin Islands, British': 'VG', 'Virgin Islands, U.S.': 'VI', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}


# import csv
#
# with open('../data_csv.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     d = {}
#
#     for row in readCSV:
#         d[row[0]] = row[1]
#
#     print(d)


def geolocate(city=None, country=None):
    '''
    Inputs city and country, or just country. Returns the lat/long coordinates of
    either the city if possible, if not, then returns lat/long of the center of the country.
    '''

    geolocator = Nominatim()

    # If the city exists,
    if city != None:
        # Try
        try:
            # To geolocate the city and country
            loc = geolocator.geocode(str(city + ',' + country))
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
    # If the city doesn't exist
    else:
        # Try
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
