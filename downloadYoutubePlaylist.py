from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # youtube清單的網址
    driver.get('https://www.youtube.com/playlist?list=PL2zTuGitn0Y9W2xUtZLUBWi3eFARCDCal')
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,'lxml')
    titles_urls = soup.findAll('a',id = 'video-title')
    urls=[]
    for title_url in titles_urls:
        urls.append('https://www.youtube.com{}'.format(title_url.get('href')))
    print("Wait Unit download is finished")
    for url in urls:
        video = YouTube(url)
        video_filter = video.streams.filter(file_extension='mp4')
        video.streams.filter(resolution=video_filter[1].resolution).first().download("D:\新增資料夾 (2)\ytvideo\崩壞3rd 動畫第二季",skip_existing=False)
        
    print("download finish")

main()