#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# question 1
Query1 = """select title, count(log.path)
            from articles, log
            where log.path = '/article/' || articles.slug
            group by articles.title
            order by count desc
            limit 3;
            """

# question 2
Query2 = """create view name_slug
            as
            select authors.name, articles.slug
            from authors join articles
            on articles.author = authors.id;
            """
Query3 = """
            select name_slug.name, count(path)
            from name_slug, log
            where log.path = '/article/' || name_slug.slug
            group by name_slug.name
            order by count desc;
            """

# question 3
Query4 = """create view day_status
            as
            select time::date as day,
            count(log.status) as status
            from log
            group by Day
            order by Day;
            """
Query5 = """create view day_error
            as
            select DATE_TRUNC('day', log.time) as Day,
            count(log.status) as error
            from log
            where log.status = '404 NOT FOUND'
            group by Day
            order by Day;
            """
Query6 = """create view day_status_error
            as
            select day_status.Day, day_status.status, day_error.error
            from day_status join day_error
            on day_status.Day = day_error.Day;
            """
Query7 = """Select * from(
            select day,
            round((error::decimal/status)* 100,2) as percentage
            from day_status_error
            order by percentage desc) as day_error_percentage
            where percentage > 1;
            """


try:
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
except:
    print("Failed to Connect to the Database")

def three_most_popular_articles():
    c.execute(Query1)
    results = c.fetchall()
    print("What are the most popular three articles of all time?")
    for title, views in results:
        print('"{}" : {} views'.format(title, views))


def most_popular_article_authors():
    c.execute(Query2)
    c.execute(Query3)
    results = c.fetchall()
    print("Who are the most popular article authors of all time?")
    for author, views in results:
        print('"{}" : {} views'.format(author, views))


def days_with_more_than_1_percent_error():
    c.execute(Query4)
    c.execute(Query5)
    c.execute(Query6)
    c.execute(Query7)
    results = c.fetchall()
    print("On which days did more than 1% of requests lead to errors?")
    for day, error_percentage in results:
        print('"{}" : {} "%"'.format(day, error_percentage))

def main():
    three_most_popular_articles()
    most_popular_article_authors()
    days_with_more_than_1_percent_error()
    db.close()

if __name__ == '__main__':
    main()
