from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import time
import threading

def get_price(siteUrl, f_all, fin):
  html = urlopen(siteUrl)
  obj = bs(html.read(), features='html.parser')
  all_divs = obj.find_all('div', {'class':f_all}) 
  for i in all_divs:
    price = i.find('span', {'class':fin}).get_text()
    print ('Ціна зі сайту:', price)

start_time = time.time()
for i in range(5):
  get_price('https://nashformat.ua/products/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu-912095', 'product-price', 'fn-price') 

  get_price('https://dumka.top/nehudozhnya-literatura/biografiyi-j-memuary/polityky-istorichni-diyachy/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu-dzhonson-boris-9789669427960', 'price-cart', 'integer') 

  get_price('https://book-ye.com.ua/catalog/biohrafiyi-vidomykh-lyudej/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7yk0nXJTP_MYymuzRmExivezZRj3VcqvPPSYJpWYZe28zUxZC1u2Lu0aAticEALw_wcB', 'card__price', 'card_price-current-real') 

  get_price('https://book24.ua/product/faktor-cherchillya-yak-odna-lyudina-zminila-istoriyu/?gclid=Cj0KCQiAnaeNBhCUARIsABEee8U1Ep8HkdHb6MV65Xu1kV4-wU0EUU-jzZkEqxx8H8tlwUcFELozQeYaAmloEALw_wcB', 'price font-bold font_mxs', 'price_value') 
  print('---------------------------------')
end_time = time.time() - start_time
average_time = end_time/5
print("Час виконання усіх запитів 5 разів:", end_time)
print("\nСередній час виконання запиту:", average_time)

print('---------------------------------')
start_time2 = time.time()

th1 = threading.Thread(target=get_price, args=('https://nashformat.ua/products/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu-912095', 'product-price', 'fn-price'))

th2 = threading.Thread(target=get_price, args=('https://dumka.top/nehudozhnya-literatura/biografiyi-j-memuary/polityky-istorichni-diyachy/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu-dzhonson-boris-9789669427960', 'price-cart', 'integer'))

th3 = threading.Thread(target=get_price, args=('https://book-ye.com.ua/catalog/biohrafiyi-vidomykh-lyudej/faktor-cherchyllya-yak-odna-lyudyna-zminyla-istoriyu/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7yk0nXJTP_MYymuzRmExivezZRj3VcqvPPSYJpWYZe28zUxZC1u2Lu0aAticEALw_wcB', 'card__price', 'card_price-current-real'))

th4 = threading.Thread(target=get_price, args=('https://book24.ua/product/faktor-cherchillya-yak-odna-lyudina-zminila-istoriyu/?gclid=Cj0KCQiAnaeNBhCUARIsABEee8U1Ep8HkdHb6MV65Xu1kV4-wU0EUU-jzZkEqxx8H8tlwUcFELozQeYaAmloEALw_wcB', 'price font-bold font_mxs', 'price_value'))

th1.start()
th2.start()
th3.start()
th4.start()

end_time2 = time.time() - start_time2

print("Час виконання запитів (threading):", end_time2)

print('---------------------------------')
print("Середній час виконання запитів зменшився на:", average_time - end_time2)