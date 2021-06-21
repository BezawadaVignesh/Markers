from django import forms
'''
FILTER_CHOICES= (
('Afghanistan', 'AF'),
('Albania', 'AL'),
('Åland Islands', 'AX'),
('American Samoa', 'AS'),
('Algeria', 'DZ'),
('Andorra', 'AD'),
('Angola', 'AO'),
('Anguilla', 'AI'),
('Antigua and Barbuda', 'AG'),
('Antarctica', 'AQ'),
('Australia', 'AU'),
('Austria', 'AT'),
('Bahrain', 'BH'),
('Bangladesh', 'BD'),
('Benin', 'BJ'),
('Belize', 'BZ'),
('Argentina', 'AR'),
('Armenia', 'AM'),
('Bosnia and Herzegovina', 'BA'),
('Aruba', 'AW'),
('Azerbaijan', 'AZ'),
('Bahamas', 'BS'),
('Brunei ', 'BN'),
('Bonaire, Sint Eustatius and Saba', 'BQ'),
('Belarus', 'BY'),
('Barbados', 'BB'),
('British Indian Ocean Territory', 'IO'),
('Bermuda', 'BM'),
('Belgium', 'BE'),
('Cameroon', 'CM'),
('Bhutan', 'BT'),
('Bolivia', 'BO'),
('Cambodia', 'KH'),
('CAR', 'CF'),
('Botswana', 'BW'),
('Chad', 'TD'),
('Bulgaria', 'BG'),
('Bouvet Island', 'BV'),
('Brazil', 'BR'),
('Cocos (Keeling) Islands', 'CC'),
('Colombia', 'CO'),
('Canada', 'CA'),
('Burkina Faso', 'BF'),
('Burundi', 'BI'),
('Costa Rica', 'CR'),
('Cape Verde', 'CV'),
('Cayman Islands', 'KY'),
('Cook Islands', 'CK'),
('China', 'CN'),
('Curaçao', 'CW'),
('Cyprus', 'CY'),
('Christmas Island', 'CX'),
('Chile', 'CL'),
('Dominican Republic', 'DO'),
('Comoros', 'KM'),
('Congo', 'CG'),
('DRC', 'CD'),
('Dominica', 'DM'),
('Equatorial Guinea', 'GQ'),
('Côte d'Ivoire', 'CI'),
('Croatia', 'HR'),
('Cuba', 'CU'),
('Eritrea', 'ER'),
('Czechia', 'CZ'),
('Denmark', 'DK'),
('Djibouti', 'DJ'),
('Fiji', 'FJ'),
('Faroe Islands', 'FO'),
('El Salvador', 'SV'),
('Egypt', 'EG'),
('French Southern Territories', 'TF'),
('French Polynesia', 'PF'),
('Ecuador', 'EC'),
('Ghana', 'GH'),
('Estonia', 'EE'),
('Ethiopia', 'ET'),
('Germany', 'DE'),
('Falkland Islands', 'FK'),
('Finland', 'FI'),
('Grenada', 'GD'),
('France', 'FR'),
('Guadeloupe', 'GP'),
('Gabon', 'GA'),
('French Guiana', 'GF'),
('Guinea', 'GN'),
('Gambia', 'GM'),
('Guinea-Bissau', 'GW'),
('Honduras', 'HN'),
('Gibraltar', 'GI'),
('Georgia', 'GE'),
('Greece', 'GR'),
('Greenland', 'GL'),
('Vatican City', 'VA'),
('Guatemala', 'GT'),
('Indonesia', 'ID'),
('Guernsey', 'GG'),
('India', 'IN'),
('Guam', 'GU'),
('Isle of Man', 'IM'),
('Israel', 'IL'),
('Guyana', 'GY'),
('Hong Kong', 'HK'),
('Haiti', 'HT'),
('Heard Island and McDonald Islands', 'HM'),
('Jersey', 'JE'),
('Hungary', 'HU'),
('Iceland', 'IS'),
('Iran', 'IR'),
('Iraq', 'IQ'),
('Ireland', 'IE'),
('Italy', 'IT'),
('Jamaica', 'JM'),
('Japan', 'JP'),
('Latvia', 'LV'),
('Liechtenstein', 'LI'),
('Madagascar', 'MG'),
('Malta', 'MT'),
('Mayotte', 'YT'),
('Mongolia', 'MN'),
('Myanmar', 'MM'),
('New Caledonia', 'NC'),
('Niue', 'NU'),
('Jordan', 'JO'),
('S. Korea', 'KR'),
('Lebanon', 'LB'),
('Lithuania', 'LT'),
('Malawi', 'MW'),
('Marshall Islands', 'MH'),
('Kenya', 'KE'),
('Mexico', 'MX'),
('Kyrgyzstan', 'KG'),
('Montenegro', 'ME'),
('Kiribati', 'KI'),
('Liberia', 'LR'),
('Laos', 'LA'),
('Macao', 'MO'),
('Libya', 'LY'),
('Maldives', 'MV'),
('North Macedonia', 'MK'),
('Mauritania', 'MR'),
('Mali', 'ML'),
('Mauritius', 'MU'),
('Namibia', 'NA'),
('Pakistan', 'PK'),
('Moldova', 'MD'),
('New Zealand', 'NZ'),
('Morocco', 'MA'),
('Norfolk Island', 'NF'),
('Nepal', 'NP'),
('Paraguay', 'PY'),
('Niger', 'NE'),
('Monaco', 'MC'),
('Mozambique', 'MZ'),
('Netherlands', 'NL'),
('Norway', 'NO'),
('Nigeria', 'NG'),
('Portugal', 'PT'),
('Oman', 'OM'),
('Russia', 'RU'),
('Saint Lucia', 'LC'),
('San Marino', 'SM'),
('Palau', 'PW'),
('Seychelles', 'SC'),
('Peru', 'PE'),
('Slovenia', 'SI'),
('Puerto Rico', 'PR'),
('South Sudan', 'SS'),
('Rwanda', 'RW'),
('Svalbard and Jan Mayen', 'SJ'),
('Saint Martin', 'MF'),
('Taiwan', 'TW'),
('Sao Tome and Principe', 'ST'),
('Togo', 'TG'),
('Sierra Leone', 'SL'),
('Turkey', 'TR'),
('Solomon Islands', 'SB'),
('Ukraine', 'UA'),
('Spain', 'ES'),
('Uruguay', 'UY'),
('Swaziland', 'SZ'),
('British Virgin Islands', 'VG'),
('Tajikistan', 'TJ'),
('Tokelau', 'TK'),
('Turkmenistan', 'TM'),
('United Arab Emirates', 'AE'),
('Uzbekistan', 'UZ'),
('U.S. Virgin Islands', 'VI'),
('Zimbabwe', 'ZW'),
('Kazakhstan', 'KZ'),
('Kuwait', 'KW'),
('Lesotho', 'LS'),
('Luxembourg', 'LU'),
('Malaysia', 'MY'),
('Martinique', 'MQ'),
('Micronesia, Federated States of', 'FM'),
('Montserrat', 'MS'),
('Nauru', 'NR'),
('Nicaragua', 'NI'),
('Northern Mariana Islands', 'MP'),
('Panama', 'PA'),
('Pitcairn', 'PN'),
('Réunion', 'RE'),
('Saint Helena, Ascension and Tristan da Cunha', 'SH'),
('Saint Vincent Grenadines', 'VC'),
('Senegal', 'SN'),
('Sint Maarten', 'SX'),
('South Africa', 'ZA'),
('Sudan', 'SD'),
('Switzerland', 'CH'),
('Thailand', 'TH'),
('Trinidad and Tobago', 'TT'),
('Tuvalu', 'TV'),
('USA', 'US'),
('Venezuela', 'VE'),
('Papua New Guinea', 'PG'),
('Poland', 'PL'),
('Romania', 'RO'),
('Saint Kitts and Nevis', 'KN'),
('Samoa', 'WS'),
('Serbia', 'RS'),
('Slovakia', 'SK'),
('South Georgia and the South Sandwich Islands', 'GS'),
('Suriname', 'SR'),
('Syria', 'SY'),
('Timor-Leste', 'TL'),
('Tunisia', 'TN'),
('Uganda', 'UG'),
('United States Minor Outlying Islands', 'UM'),
('Vietnam', 'VN'),
('Palestine', 'PS'),
('Philippines', 'PH'),
('Qatar', 'QA'),
('Saint Barth', 'BL'),
('Saint Pierre Miquelon', 'PM'),
('Saudi Arabia', 'SA'),
('Singapore', 'SG'),
('Somalia', 'SO'),
('Sri Lanka', 'LK'),
('Sweden', 'SE'),
('Tanzania', 'TZ'),
('Tonga', 'TO'),
('Turks and Caicos', 'TC'),
('UK', 'GB'),
('Vanuatu', 'VU'),
('Wallis and Futuna', 'WF'),
('Zambia', 'ZM'),
('Western Sahara', 'EH'),
('Yemen', 'YE'))
class FilterForm(forms.Form):
    filter_by = forms.ChoiceField(choices= FILTER_CHOICES)'''


class ConactForm(forms.Form):
    sender = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)