import pandas as pd

first_day_of_selection = pd.to_datetime('01.01.2023', format='%d.%m.%Y')
last_day_of_selection = pd.to_datetime('01.01.2026', format='%d.%m.%Y')
# last_day_of_selection = pd.to_datetime('01.01.2034', format='%d.%m.%Y')
eto_start_point = pd.to_datetime('01.01.2023_8', format='%d.%m.%Y_%H')

# initial_start_status = "operation_start_date"
initial_start_status = "31.12.2022"
start_point = pd.to_datetime('31.12.2022', format='%d.%m.%Y')

period_dict = {'1_2023': "янв 2023", '2_2023': "фев 2023", '3_2023': "мар 2023", '4_2023': "апр 2023", '5_2023': "май 2023", '6_2023': "июн 2023", '7_2023': "июл 2023", '8_2023': "авг 2023", '9_2023': "сен 2023", '10_2023': "окт 2023", '11_2023': "ноя 2023", '12_2023': "дек 2023", '1_2024': "янв 2024", '2_2024': "фев 2024", '3_2024': "мар 2024", '4_2024': "апр 2024", '5_2024': "май 2024", '6_2024': "июн 2024", '7_2024': "июл 2024", '8_2024': "авг 2024", '9_2024': "сен 2024", '10_2024': "окт 2024", '11_2024': "ноя 2024", '12_2024': "дек 2024", '1_2025': "янв 2025", '2_2025': "фев 2025", '3_2025': "мар 2025", '4_2025': "апр 2025", '5_2025': "май 2025", '6_2025': "июн 2025", '7_2025': "июл 2025", '8_2025': "авг 2025", '9_2025': "сен 2025", '10_2025': "окт 2025", '11_2025': "ноя 2025", '12_2025': "дек 2025", 
               '1_2026': "янв 2026", '2_2026': "фев 2026", '3_2026': "мар 2026", '4_2026': "апр 2026", '5_2026': "май 2026", '6_2026': "июн 2026", '7_2026': "июл 2026", '8_2026': "авг 2026", '9_2026': "сен 2026", '10_2026': "окт 2026", '11_2026': "ноя 2026", '12_2026': "дек 2026",
              '1_2027': "янв 2027", '2_2027': "фев 2027", '3_2027': "мар 2027", '4_2027': "апр 2027", '5_2027': "май 2027", '6_2027': "июн 2027", '7_2027': "июл 2027", '8_2027': "авг 2027", '9_2027': "сен 2027", '10_2027': "окт 2027", '11_2027': "ноя 2027", '12_2027': "дек 2027",
               '1_2028': "янв 2028", '2_2028': "фев 2028", '3_2028': "мар 2028", '4_2028': "апр 2028", '5_2028': "май 2028", '6_2028': "июн 2028", '7_2028': "июл 2028", '8_2028': "авг 2028", '9_2028': "сен 2028", '10_2028': "окт 2028", '11_2028': "ноя 2028", '12_2028': "дек 2028",
               '1_2029': "янв 2029", '2_2029': "фев 2029", '3_2029': "мар 2029", '4_2029': "апр 2029", '5_2029': "май 2029", '6_2029': "июн 2029", '7_2029': "июл 2029", '8_2029': "авг 2029", '9_2029': "сен 2029", '10_2029': "окт 2029", '11_2029': "ноя 2029", '12_2029': "дек 2029",
               '1_2030': "янв 2030", '2_2030': "фев 2030", '3_2030': "мар 2030", '4_2030': "апр 2030", '5_2030': "май 2030", '6_2030': "июн 2030", '7_2030': "июл 2030", '8_2030': "авг 2030", '9_2030': "сен 2030", '10_2030': "окт 2030", '11_2030': "ноя 2030", '12_2030': "дек 2030",
               '1_2031': "янв 2031", '2_2031': "фев 2031", '3_2031': "мар 2031", '4_2031': "апр 2031", '5_2031': "май 2031", '6_2031': "июн 2031", '7_2031': "июл 2031", '8_2031': "авг 2031", '9_2031': "сен 2031", '10_2031': "окт 2031", '11_2031': "ноя 2031", '12_2031': "дек 2031",
               '1_2032': "янв 2032", '2_2032': "фев 2032", '3_2032': "мар 2032", '4_2032': "апр 2032", '5_2032': "май 2032", '6_2032': "июн 2032", '7_2032': "июл 2032", '8_2032': "авг 2032", '9_2032': "сен 2032", '10_2032': "окт 2032", '11_2032': "ноя 2032", '12_2032': "дек 2032",
               '1_2033': "янв 2033", '2_2033': "фев 2033", '3_2033': "мар 2033", '4_2033': "апр 2033", '5_2033': "май 2033", '6_2033': "июн 2033", '7_2033': "июл 2033", '8_2033': "авг 2033", '9_2033': "сен 2033", '10_2033': "окт 2033", '11_2033': "ноя 2033", '12_2033': "дек 2033",
               '1_2034': "янв 2034", '2_2034': "фев 2034", '3_2034': "мар 2034", '4_2034': "апр 2034", '5_2034': "май 2034", '6_2034': "июн 2034", '7_2034': "июл 2034", '8_2034': "авг 2034", '9_2034': "сен 2034", '10_2034': "окт 2034", '11_2034': "ноя 2034", '12_2034': "дек 2034",
              }

period_sort_index = {'1_2023':1, '2_2023': 2, '3_2023': 3, '4_2023': 4, '5_2023': 5, '6_2023': 6, '7_2023': 7, '8_2023': 8, '9_2023': 9, '10_2023': 10, '11_2023': 11, '12_2023': 12, '1_2024':13, '2_2024': 14, '3_2024': 15, '4_2024': 16, '5_2024': 17, '6_2024': 18, '7_2024': 19, '8_2024': 20, '9_2024': 21, '10_2024': 22, '11_2024': 23, '12_2024': 24, '1_2025':25, '2_2025': 26, '3_2025': 27, '4_2025': 28, '5_2025': 29, '6_2025': 30, '7_2025': 31, '8_2025': 32, '9_2025': 33, '10_2025': 34, '11_2025': 35, '12_2025': 36,
                     '1_2026':37, '2_2026': 38, '3_2026':39, '4_2026': 40, '5_2026': 41, '6_2026': 42, '7_2026': 43, '8_2026': 44, '9_2026': 45, '10_2026': 46, '11_2026': 47, '12_2026': 48,
                     '1_2027':49, '2_2027': 50, '3_2027':51, '4_2027': 52, '5_2027': 53, '6_2027': 54, '7_2027': 55, '8_2027': 56, '9_2027': 57, '10_2027': 58, '11_2027': 59, '12_2027': 60,
                    '1_2028':61, '2_2028': 62, '3_2028':63, '4_2028': 64, '5_2028': 65, '6_2028': 66, '7_2028': 67, '8_2028': 68, '9_2028': 69, '10_2028': 70, '11_2028': 71, '12_2028': 72,
                     '1_2029':73, '2_2029': 74, '3_2029':75, '4_2029': 76, '5_2029': 77, '6_2029': 78, '7_2029': 79, '8_2029': 80, '9_2029': 81, '10_2029': 82, '11_2029': 83, '12_2029': 84,
                     '1_2030':85, '2_2030': 86, '3_2030':87, '4_2030': 88, '5_2030': 89, '6_2030': 90, '7_2030': 91, '8_2030': 92, '9_2030': 93, '10_2030': 94, '11_2030': 95, '12_2030': 96,
                     '1_2031':97, '2_2031': 98, '3_2031':99, '4_2031': 100, '5_2031': 101, '6_2031': 102, '7_2031': 103, '8_2031': 104, '9_2031': 105, '10_2031': 106, '11_2031': 107, '12_2031': 108,
                     '1_2032':109, '2_2032': 110, '3_2032':111, '4_2032': 112, '5_2032': 113, '6_2032': 114, '7_2032': 115, '8_2032': 116, '9_2032': 117, '10_2032': 118, '11_2032': 119, '12_2032': 120,
                     '1_2033':121, '2_2033': 122, '3_2033':123, '4_2033': 124, '5_2033': 125, '6_2033': 126, '7_2033': 127, '8_2033': 128, '9_2033': 129, '10_2033': 130, '11_2033': 131, '12_2033': 132,
                     '1_2034':133, '2_2034': 134, '3_2034':135, '4_2034': 136, '5_2034': 137, '6_2034': 138, '7_2034': 139, '8_2034': 140, '9_2034': 141, '10_2034': 142, '11_2034': 143, '12_2034': 144
                    }

months_list = ['1_2023', '2_2023', '3_2023', '4_2023', '5_2023', '6_2023', '7_2023', '8_2023', '9_2023', '10_2023', '11_2023', '12_2023', '1_2024', '2_2024', '3_2024', '4_2024', '5_2024', '6_2024', '7_2024', '8_2024', '9_2024', '10_2024', '11_2024', '12_2024', '1_2025', '2_2025', '3_2025', '4_2025', '5_2025', '6_2025', '7_2025', '8_2025', '9_2025', '10_2025', '11_2025', '12_2025',
              '1_2026', '2_2026', '3_2026', '4_2026', '5_2026', '6_2026', '7_2026', '8_2026', '9_2026', '10_2026', '11_2026', '12_2026',
               '1_2027', '2_2027', '3_2027', '4_2027', '5_2027', '6_2027', '7_2027', '8_2027', '9_2027', '10_2027', '11_2027', '12_2027',
               '1_2028', '2_2028', '3_2028', '4_2028', '5_2028', '6_2028', '7_2028', '8_2028', '9_2028', '10_2028', '11_2028', '12_2028',
               '1_2029', '2_2029', '3_2029', '4_2029', '5_2029', '6_2029', '7_2029', '8_2029', '9_2029', '10_2029', '11_2029', '12_2029',
               '1_2030', '2_2030', '3_2030', '4_2030', '5_2030', '6_2030', '7_2030', '8_2030', '9_2030', '10_2030', '11_2030', '12_2030',
               '1_2031', '2_2031', '3_2031', '4_2031', '5_2031', '6_2031', '7_2031', '8_2031', '9_2031', '10_2031', '11_2031', '12_2031',
               '1_2032', '2_2032', '3_2032', '4_2032', '5_2032', '6_2032', '7_2032', '8_2032', '9_2032', '10_2032', '11_2032', '12_2032',
               '1_2033', '2_2033', '3_2033', '4_2033', '5_2033', '6_2033', '7_2033', '8_2033', '9_2033', '10_2033', '11_2033', '12_2033',
               '1_2034', '2_2034', '3_2034', '4_2034', '5_2034', '6_2034', '7_2034', '8_2034', '9_2034', '10_2034', '11_2034', '12_2034',
               
              ]


rename_columns_dict = {"year":"Год","month":"Месяц", "downtime":"Простой, час", 'level_1_description':"БЕ","eo_main_class_description": "Класс ЕО", 'eo_class_description':"Класс ЕО", "constr_type": "Тип конструкции", "teh_mesto": "Техместо",'mvz':"МВЗ", "eo_model_name": "Модель ЕО", "eo_code": "ЕО", "eo_description": "Наименоваание ЕО", "operation_start_date":"Дата начала эксплуатации", "operation_finish_date": "Дата завершения эксплуатации", "avearage_day_operation_hours_updated": "Среднесуточная наработка", "maintanance_start_datetime": "Дата время начала работ", "maintanance_finish_datetime": "Дата время завершения работ", "maintanance_name": "Вид ТОИР", "downtime_plan": "Время простоя, час", "eto": "ЕТО", "overhaul_total": "КР", "to1000":"ТО-1000", "to12000": "ТО-12000", "to2000": "ТО-2000", "to4000": "ТО-4000", "to500": "ТО-500", "to6000": "ТО-6000", "to_suppl_systems": "ТО доп систем", "tr":"ТР", "tr_middle": "Трсред", "tr_suppl_systems":"Трдоп.сист.", "tyre_repl":"Замена колес (6 шт)", "eng_repl": "Кдвс (Замена)", "tr_susp": "ТР подвески", "gen_overhaul": "Кген(Замена)", "kmk_overhaul": 'Кмк (Замена)', 'tr_mo': 'ТРмо (Замена)', 'lining_partitial': "СВч (частичная футеровка)", 'lining_full': "СВп (полная футеровка)"}





