# lib
from selenium import webdriver
import time

# make driver register
driver = webdriver.Chrome('./chromedriver')

# add pandas data list
metropolitan = []

# Tokyo

driver.get('https://stopcovid19.metro.tokyo.lg.jp/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[4]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[4]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[4]/div/div/div[1]/div/span').text
print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'東京都', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('東京都情報完了')

# Kanagawa

driver.get('https://www.pref.kanagawa.jp/osirase/1369/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[3]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[3]/span').text
print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'神奈川県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('神奈川県情報完了')

# Hokkaido

driver.get('https://stopcovid19.hokkaido.dev/')
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[2]/button[1]').click()
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/div[1]/div[1]/span').text
print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'北海道', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('北海道情報完了')

# Osaka


driver.get('https://covid19-osaka.info/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/span').text
print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'大阪府', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('大阪府情報完了')

# Aichi

driver.get('https://stopcovid19.code4.nagoya/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[4]/div[2]/div/header/div/div[3]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[4]/div[2]/div/header/div/div[1]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[4]/div[2]/div/header/div/div[3]/span').text
print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'愛知県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('愛知県情報完了')

# Kyoto

driver.get('https://kyoto.stopcovid19.jp/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'京都府', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('京都府情報完了')

# Hiroshima

driver.get('https://covid19-hiroshima.netlify.com/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[1]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[1]/div/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[1]/div/div/div[1]/div[1]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'広島県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('広島県情報完了')

# Ehime

driver.get('https://ehime-covid19.com/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/header/div/div[3]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/header/div/div[1]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/header/div/div[3]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'愛媛県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('愛媛県情報完了')

# Kyushu

driver.get('https://dev-covid19-kyusyu.netlify.com/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/span').text
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'九州', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('九州情報完了')

# Nagasaki

driver.get('https://stopcovid19-nagasaki.netlify.com/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'長崎県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('長崎県情報完了')

# Aomori

driver.get('https://covid19.codeforaomori.org/')
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[3]/div/button[1]').click()
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'青森県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('青森県情報完了')

# Iwasaki
# 感染者なし

# Miyagi

driver.get('https://miyagi.stopcovid19.jp/')
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'宮城県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('宮城県情報完了')

# Akita

driver.get('https://covid19-akita.netlify.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[3]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'秋田県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('秋田県情報完了')

# Yamagata

driver.get('https://covid19-yamagata.netlify.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[2]/div/div/div[1]/div[1]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'山形県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('山形県情報完了')

# Fukushima

driver.get('https://fukushima-covid19.firebaseapp.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[1]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'福島県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('福島県情報完了')

# Ibaragi

driver.get('https://covid19-ibaraki.netlify.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'茨城県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('茨城県情報完了')

# Tochigi

driver.get('https://covid19-tochigi.netlify.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[2]/div[2]/div/div/div[1]/div[1]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'栃木県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('栃木県情報完了')

# Gunma

driver.get('https://stopcovid19-gunma.netlify.com/')
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[1]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[2]/button[2]').click()
time.sleep(3)
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/main/div/div/div[3]/div[1]/div/div/div[1]/div[1]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'群馬県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('群馬県情報完了')

# Chiba

driver.get('https://chiba-covid19.mypl.net/')
cumulative = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[3]/span').text
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[1]/div/button[1]').click()
time.sleep(3)
people = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/header/div/div[3]/span').text

print('日別陽性患者数')
print(people)
print('累計陽性患者数')
print(cumulative)

info = {'prefecture':'千葉県', 'people': people.strip(' 人'), 'cumulative': cumulative.strip(' 人')}
metropolitan.append(info)

print('千葉県情報完了')

#残りの県

# 新潟県
# 富山県
# 石川県
# 福井県
# 山梨県
# 長野県
# 岐阜県
# 静岡県
# 三重県
# 滋賀県
# 兵庫県
# 奈良県
# 和歌山県
# 鳥取県
# 島根県
# 岡山県
# 山口県
# 徳島県
# 香川県
# 高知県
# 佐賀県
# 熊本県
# 大分県
# 鹿児島県
# 沖縄県

# 今現在のデータ

import pandas as pd

Japan_pd = pd.DataFrame(metropolitan)
Japan_pd.columns = ['都道府県','日別','累計']
print(Japan_pd)
Japan_pd.to_csv('Japan-COVID-19.csv')

driver.close()
driver.quit()