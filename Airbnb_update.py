import json
import os

import pandas as pd
import requests
from lxml import html
from datetime import datetime
today = datetime.today()

def get_data(i,id):
        item = {}
        try:
            try:
                item['Property ID'] = id
            except:
                item['Property ID'] = ''
            try:
                item['Date'] = today.strftime("%d/%m/%y")
            except:
                item['Date'] = ''
            try:
                item['Time'] = today.strftime("%H:%M:%S")
            except:
                item['Time'] = ''
            try:
                item['Building type'] = 'Home'
            except:
                item['Building type'] = ''
            try:
                item['City'] = i['listing']['locationTitle'].split(',')[0]
            except:
                item['City'] = ''
            try:
                item['State'] = i['listing']['locationTitle'].split(',')[1]
            except:
                item['State'] = ''
            try:
                item['Country'] = 'United States'
            except:
                item['Country'] = ''
            try:
                item['Property Title'] = i['listing']['name']
            except:
                item['Property Title'] = ''
            try:
                item['Guest'] = i['listing']['homeDetails'][0]['title'].replace('guests', '')
            except:
                item['Guest'] = ''
            try:
                item['Beds'] = i['listing']['homeDetails'][2]['title'].replace('bed', '').replace('s', '').strip()
            except:
                item['Beds'] = ''
            try:
                item['Bedrooms'] = i['listing']['homeDetails'][1]['title'].replace('bedroom', '').replace('s', '').strip()
            except:
                item['Bedrooms'] = ''
            try:
                item['Bathrooms'] = i['listing']['homeDetails'][3]['title'].replace('bath', '').replace('s', '').strip()
            except:
                item['Bathrooms'] = ''
            try:
                item['Night Rate'] = i['pricingQuote']['structuredStayDisplayPrice']['primaryLine']['price'].replace('\xa0',
                                                                                                                     '')
            except:
                item['Night Rate'] = ''
            try:
                item['Room Type'] = i['listing']['roomTypeCategory']
            except:
                item['Room Type'] = ''
            try:
                item['checkin'] = i['listingParamOverrides']['checkin']
            except:
                item['checkin'] = ''
            try:
                item['checkout'] = i['listingParamOverrides']['checkout']
            except:
                item['checkout'] = ''
            try:
                item['Booking rate per night'] = i['listing']['avgRating']
            except:
                item['Booking rate per night'] = ''
            try:
                item['Cleaning fee'] = ''
            except:
                item['Cleaning fee'] = ''
            img_list = []
            img = i['listing']['contextualPictures']
            for j in img:
                image = j['picture']
                img_list.append(image)
            try:
                item['Property Photos'] = ','.join(img_list)
            except:
                item['Property Photos'] = ''
            print(item)
            save_data = []
            save_data.append(item)
            file_name = 'Airbnb_data5555.csv'
            df = pd.DataFrame(save_data)
            if os.path.exists(file_name):
                df.to_csv(file_name, mode='a', index=False, header=False)
            else:
                df.to_csv(file_name, mode='a', index=False, header=True)
        except:
            pass

def link_data():
    today = datetime.today()
    offset = 0
    next = True
    while next:
        url = 'https://www.airbnb.com/api/v3/ExploreSections'
        print(url,offset)

        headers = {
            'authority': 'www.airbnb.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            # 'cookie': 'bev=1669979452_ZDBlMzYwZDJkZTY2; cdn_exp_e34f8847ee4f0c14f=control; cdn_exp_875ac2fa405b6da87=treatment; everest_cookie=1669979453.jyXHmS6P5fqD6zD5VfCQ.d5Krbmz6rdDHKfK43V-4in-hVYJ4Pe8-dJh2bD2RDD4; frmfctr=wide; tzo=330; _gcl_au=1.1.1250331843.1669979580; _gid=GA1.2.1795661960.1669979580; cdn_exp_9cbf277ff04e35316=control; cdn_exp_759647797802a2888=treatment; country=US; ak_bmsc=2439A7BA5F0F3F55FEA4C3AE7B287839~000000000000000000000000000000~YAAQJUcjF0BxgJuEAQAA4d2i4BJdLwQ1xveEeykiuwOxqc3RP5VCCvCv0uuh7xlz4kLjBbPx7mWNkLe3voJDlEt4ZNHP/P1hkoLsKVi9ql4x0XZMcok39grCy7Gn/P08/3D83I0x03cu54tV/2o4epe9+Sjh8VDm+sXPfEOmxsD3qg880KceEv1o69T4PoySTR92K0bArvp47tnU3jMZ1PYf8AP0/FZ77JiiGZH16QgQgL6mulJAaUoq6rTdjVzBLla7kOVDsjxXUH5rEptvkavq/7rCIUHvcsqOwW9TAcLB/SRhQRrzQBfnV/v4G5pKItk+NIfh9vbQnxgvtYs2DQE7gid1B7nKRWZ1/P//68pLWe3NWvmBExzcDENtGXAmsjag9fBDcYw=; OptanonAlertBoxClosed=NR; _csrf_token=V4%24.airbnb.com%240XDtFo0jiS0%24LbgbtrOscVAzu1a5z-TRnXQVjo4yvkcUNZC0b2o_eeU%3D; jitney_client_session_id=2289ee5f-3e9b-4628-8bfd-af53f811c9d2; jitney_client_session_created_at=1670216082; flags=0; AMP_TOKEN=%24NOT_FOUND; cfrmfctr=MOBILE; cbkp=2; _user_attributes=%7B%22curr%22%3A%22EUR%22%2C%22guest_exchange%22%3A0.94873%2C%22device_profiling_session_id%22%3A%221669979453--04d6cc219065fa505bf1bff9%22%2C%22giftcard_profiling_session_id%22%3A%221670219792--c2753c17a53481fde0d81af8%22%2C%22reservation_profiling_session_id%22%3A%221670219792--2eede030a397bc0800049a37%22%7D; jitney_client_session_updated_at=1670219884; _ga_2P6Q8PGG16=GS1.1.1670216223.9.1.1670219897.37.0.0; _ga=GA1.1.1405059705.1669979580; _uetsid=4c4c2320723211edb722bd7fa6fdf05b; _uetvid=4c4c7190723211eda58493f336e4f4cf; bm_sv=CC9458E572A85AF7F2117EEC89587101~YAAQP0cjFzFbn32EAQAA70Xd4BKVDVTtjGzMMy/1dEykIPE3MHECjbjkIWfUdGI2fVHdz3Z5Dc6jdkzJh26wadLRrTl80Bm+FvSyxLwymZpEsuMNEfL9gWwX7ptfxg4hjcto2TI+Ht06ULPNgOQ9DodIwCGVmr1uZch5f0f+81y/l/IzSme4HCnCzh77MqALLdyOc11q2qZsvav0+zQfI5qZOSNqaBFy98xAFi+1DCN+gBZzgwKBUrT0tsfhgMYmug==~1; previousTab=%7B%22id%22%3A%22db184380-fe77-4835-a703-cbb33523ece3%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.com%2F%22%7D',
            'device-memory': '8',
            'dpr': '1.25',
            'ect': '3g',
            'referer': 'https://www.airbnb.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'viewport-width': '943',
            'x-airbnb-api-key': 'd306zoyjsyarp7ifhu67rjxn52tv0t20',
            'x-airbnb-graphql-platform': 'web',
            'x-airbnb-graphql-platform-client': 'minimalist-niobe',
            'x-airbnb-supports-airlock-v2': 'true',
            'x-client-request-id': '1ld2rqp0hia4z91vovwqw1jv7nob',
            # 'x-csrf-token': f'V4{.airbnb.com$0XDtFo0jiS0$LbgbtrOscVAzu1a5z-TRnXQVjo4yvkcUNZC0b2o_eeU=}',
            'x-csrf-without-token': '1',
            'x-niobe-short-circuited': 'true',
        }

        params = {'operationName': 'ExploreSections', 'locale': 'en', 'currency': 'EUR','variables': '{"isInitialLoad":true,"hasLoggedIn":false,"cdnCacheSafe":false,"source":"EXPLORE","exploreRequest":{"metadataOnly":false,"version":"1.8.3","tabId":"all_tab","refinementPaths":["/homes"],"searchMode":"flex_destinations_search","itemsPerGrid":20,"cdnCacheSafe":false,"treatmentFlags":["flex_destinations_june_2021_launch_web_treatment","merch_header_breakpoint_expansion_web","flexible_dates_12_month_lead_time","storefronts_nov23_2021_homepage_web_treatment","lazy_load_flex_search_map_compact","lazy_load_flex_search_map_wide","im_flexible_may_2022_treatment","im_flexible_may_2022_treatment","flex_v2_review_counts_treatment","search_add_category_bar_ui_ranking_web","decompose_stays_search_m2_treatment","flexible_dates_options_extend_one_three_seven_days","super_date_flexibility","micro_flex_improvements","micro_flex_show_by_default","search_input_placeholder_phrases","pets_fee_treatment"],"screenSize":"large","isInitialLoad":true,"hasLoggedIn":false,"flexibleTripLengths":["one_week"],"locationSearch":"MIN_MAP_BOUNDS","categoryTag":"Tag:8528","priceFilterInputType":5,"priceFilterNumNights":5,"itemsOffset":"' + str( offset) + '","sectionOffset":0,"federatedSearchSessionId":"08fb97d5-ec45-4ced-adda-58747cd6b4cc"},"gpRequest":{"expectedResponseType":"INCREMENTAL"}}','extensions': '{"persistedQuery":{"version":1,"sha256Hash":"466ebcc4cd6d8eb8a6b982b2515223a2f3001879afde5807bc94a1976a5b6f20"}}', }

        response = requests.get(url, params=params, headers=headers)
        j_data = json.loads(response.text)
        try:
            data = j_data['data']['presentation']['explore']['sections']['responseTransforms']['transformData'][0]['sectionContainer']['section']['child']['section']['items']
        except:
            data = ''
        if not data:
            next = False
            continue
        for i in data:

            try:
                id = i['listing']['id']
            except:
                id = ''
            url = f'https://www.airbnb.com/rooms/{id}?adults=1&category_tag=Tag%3A8536&children=0&infants=0&search_mode=flex_destinations_search&check_in=2023-01-08&check_out=2023-01-13&federated_search_id=a6460462-65ad-4d27-8f5a-8474b1f2c500&source_impression_id=p3_1669990343_IdGdCVNsOD6l5Kn5'
            get_data(i,id)
        offset += 20

if __name__ == "__main__":
    link_data()

