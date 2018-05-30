import psycopg2


connection = psycopg2.connect(database="news", host="localhost",
                              password="vagrant", port="5432")
cur_object = connection.cursor()


def popular_articles():
    print '\nPopular Articles:\n'
    '''Function To display the popular three articles with their views'''
    myQuery = '''select a.title, count(a.slug) as views
    from articles a inner join log l on a.slug =
    replace(l.path, '/article/', '')
    where l.status = '200 OK' and l.path != '/'
    group by l.path, a.title
    order by count(l.path) Desc limit(3);'''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '\n'
    print '------------------------------------------------------------'


def popular_authors():
    ''' Function to display popular authors with their article views '''
    print '\nPopular Authors:\n'
    myQuery = '''select name, sum(requests) as total_article_views
    from keysnrequests k inner join articles ar on ar.slug = k.key
    inner join authors au on au.id = ar.author
    group by name
    order by total_article_views Desc;'''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '\n'
    print '------------------------------------------------------------'


def error_rate():
    ''' Function to display the error rate greater than 1 '''
    print '\nError Rate:\n'
    myQuery = '''select t.date, round(f.failure_count*100.00/t.total_count, 2)
    as rate
    from F_Count f inner join T_count t on f.date = t.date
    where f.failure_count*100.00/t.total_count > 1 ; '''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '%', 'errors\n'
popular_articles()
popular_authors()
error_rate()
cur_object.close()
connection.close()
