

#%%

import time
from googletrans import Translator
import pandas as pd
import time
from deep_translator import GoogleTranslator

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)





#%%


def translate_to_english(text_list):
    # translator = Translator(service_urls=['translate.google.com'])
    translator = Translator(service_urls=['translate.google.com'],
                            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)', proxies=None, timeout=None)
    translated_text = []
    count = 0
    for text in text_list:
        try:
            result = translator.translate(text, dest='en').text
            translated_text.append(result)
            count += 1
            if count % 1000 == 0:
                print('time to sleep 5 sec')
                time.sleep(5)
        except Exception as e:
            translated_text.append("Translation failed")
    return translated_text

#%%
keywords_df  = pd.read_csv('D:\\Tutorials\\Streamlit\\INPUT_DATA\\locatie_nl.csv', sep=',',encoding='latin-1')
df = keywords_df.copy()
df["Keyword"] = df["Keyword"].astype(str)


#%%


start_time = time.time()
my_list = df["Keyword"].to_list()
df["Keyword_eng"] = translate_to_english(my_list)
end_time = time.time()

print("Time elapsed:", end_time - start_time, "seconds")
#%%

import time

start_time = time.time()
my_list = df["Keyword"].to_list()
df["keyword_eng"] = df["Keyword"].apply(lambda x: GoogleTranslator(source='auto', target='en').translate(x))
end_time = time.time()

print("Time elapsed:", end_time - start_time, "seconds")
#%%









