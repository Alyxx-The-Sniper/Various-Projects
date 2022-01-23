from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://alyxmandario.com/blog/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

#########################################################
#SOUP.FIND ( FOR TESTING ONLY )

# blog = soup.find('div', class_ = 'blog-entry-inner clr')
# blog_continue = soup.find('div', class_ = 'blog-entry-readmore clr')
#
#
# blog_title = blog.h2.text             # blog title
# blog_paragraph = blog.p.text          # blog partial paragraph
# blog_link = blog_continue.a['href']   # link to the full blog
#
#
#
# print(blog_title)
# print(blog_paragraph)
# print(blog_link)


##########################################################
# SOUP.FIND_ALL
# NOW WE BEGIN TO ITERATE TO GET ALL THE NEEDED DETAILS USING 'FIND_ALL' METHOD

with open('BLOG_CSV_toto.csv', 'w', newline='') as bl:
    blog_writter = csv.writer(bl)
    blog_writter.writerow(['title', 'paragraph', 'link'])


    for article in soup.find_all('article'):

        title = article.h2.text
        print(title)
        paragraph = article.p.text
        print(paragraph)
        blog_continue = soup.find('div', class_='blog-entry-readmore clr')
        link = blog_continue.a['href']
        print(link)
        blog_writter.writerow([title, paragraph, link])





