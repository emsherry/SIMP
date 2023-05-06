import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import csv


urls = ['https://www.brecorder.com/markets', 
        'https://www.brecorder.com/business-finance',
        'https://www.geo.tv/category/business',
        'https://www.dawn.com/business',
        'https://thefinancialdaily.com/category/stock-review/',
        'https://arynews.tv/category/business/']


keywords = ['Pakistan Stock Exchange', 'PSX', 'Karachi Stock Exchange', 'KSE', 'economy of Pakistan', 'GDP of Pakistan', 
            'IMF Pakistan', 'Pakistan economy growth', 'Pakistan stock market', 'Pakistan currency', 'Pakistan rupee', 'Pakistan inflation', 
            'Pakistan trade deficit', 'Pakistan exports', 'Pakistan imports', 'Pakistan budget', 'Pakistan taxes', 'Pakistan debt', 'Pakistan FDI', 
            'Pakistan remittances', 'Pakistan forex reserves', 'Pakistan foreign exchange', 'Pakistan exchange rate', 'Pakistan interest rate', 
            'Pakistan monetary policy', 'Pakistan fiscal policy', 'Pakistan budget deficit', 'Pakistan current account deficit', 'Pakistan energy crisis', 
            'Pakistan electricity', 'Pakistan oil', 'Pakistan gas', 'Pakistan coal', 'Pakistan renewables', 'Pakistan agriculture', 'Pakistan textile', 
            'Pakistan pharmaceuticals', 'Pakistan cement', 'Pakistan steel', 'Pakistan automobile', 'Pakistan telecommunications', 'Pakistan IT', 
            'Pakistan startups', 'Pakistan e-commerce', 'Pakistan digital economy', 'Pakistan banking', 'Pakistan microfinance', 'Pakistan insurance', 
            'Pakistan real estate', 'Pakistan housing', 'Pakistan construction', 'Pakistan infrastructure', 'Pakistan transport', 'Pakistan logistics', 
            'Pakistan aviation', 'Pakistan tourism', 'Pakistan hospitality', 'Pakistan education', 'Pakistan health', 'Pakistan sanitation', 'Pakistan water', 
            'Pakistan climate change', 'Pakistan disaster management', 'Pakistan security', 'Pakistan defense', 'Pakistan foreign policy', 
            'Pakistan international trade', 'Pakistan regional cooperation', 'Pakistan SAARC', 'Pakistan CPEC', 'Pakistan Belt and Road', 'Pakistan China', 
            'Pakistan USA', 'Pakistan UK', 'Pakistan EU', 'Pakistan Middle East', 'Pakistan Afghanistan', 'Pakistan India', 'Pakistan Bangladesh', 'Pakistan Iran',
            'Pakistan Gulf', 'Pakistan Saudi Arabia', 'Pakistan UAE', 'Pakistan Qatar', 'Pakistan Oman', 'Pakistan Kuwait', 'Pakistan Bahrain', 'Pakistan Turkey', 
            'Pakistan Russia', 'Pakistan China-Pakistan Economic Corridor', 'Pakistan One Belt One Road', 'Pakistan Economic Outlook', 'Pakistan Economic Survey', 
            'Pakistan Economic Indicators', 'Pakistan Economic Growth Rate', 'Pakistan Stock Market News', 'Pakistan Business News', 'Pakistan Financial News', 
            'Pakistan Economic Policy', 'Pakistan Economic Reforms', 'Paksitan', 'Economy']

# keywords = ['Pakistan']

scraped_data = []

def get_sentiment(sentence):
    blob = TextBlob(sentence)
    return blob.sentiment.polarity


for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        sentences = article.text.split('.')
        link = article.find('a')['href'] if article.find('a') else ''
        for sentence in sentences:
            if any(keyword in sentence for keyword in keywords):
                sentiment = get_sentiment(sentence)
                scraped_data.append((sentence.strip(), link, sentiment))

with open('scrapes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sentence', 'Link', 'Sentiment Score'])
    for data in scraped_data:
        writer.writerow([data[0], data[1], data[2]])
