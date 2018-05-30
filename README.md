# log_analysis

AIM:
    To build a reporting tool that prints values of popular articles, popular authors, error rate greater than 1 percent

TOOLS USED:
1.virtual machine
2.vagrant
3.psql
4.data files i.e, news database
5.psycopg2 package

INSTALLATION PROCESS:
1.To install virtual box url is https://www.virtualbox.org/wiki/Downloads
2.To install vagrant url is https://releases.hashicorp.com/vagrant/2.1.1/vagrant_2.1.1_x86_64.msi
4.To install psql go to vagrant and type command 'sudo apt-get install postgresql'
5.To install python packages first we need to install pip of easy_install 'sudo apt-get install python-pip' in vagrant
6.To install a psycopg2 package 'pip install psycopg2'

PROCEDURE:
1.Install virtualbox in system which creates an environment to run another os in your system
2.Install vagrant which is an environment through which we run another os in the system
3.After installation of vagrant create a folder which acts as a sharable folder for both the operating system this is possible because of vagrant then go to that folder open terminal then download the vagrant box command: 'vagrant box add 'ubuntu/xenial64''
4.The vagrant box that is downloaded acts as a default box 
5.run vagrant init 'downloaded_box_name' like 'ubuntu/xenial64' i.e, the environment of os that is downloaded
6.Then run vagrant up command 
7.Run vagrant up command then run vagrant ssh
8.Our terminal is opened and There your environment is setup 

HOW TO RUN:
1.Go to the sharable folder then create some views the following are the queries to create views
VIEWS:
    1.KEYS AND REQUESTS VIEW - displays the slug as keys and individual article status count    as requests
    
      QUERY:
      '''create view keysnrequests as select count(l.path) as requests,replace(l.path, '/article/', '') as key from articles ar inner join log l on ar.slug=replace(l.path, '/article/', '') where l.status = '200 OK' and l.path != '/' group by l.path;'''

    2.FAILURE COUNT - displays the date and its failure count
      QUERY:
      '''create view F_Count as select count(date(time)) as failure_count,date(time) from log where status != '200 OK' group by date(time);''' 

    3.TOTAl COUNT - displays the date and per days status i.e., both success and failure requests
      QUERY:
      '''create view T_Count as select count(date(time)) as total_count,date(time) from log where status != '200 OK' or status = '200 OK' group by date(time);
      '''
2.After creating "views" go to that sharable folder and type 'python log_analysis.py'

RESULT:
1.displays the popular articles and their views, popular authors and their total article views, date and error rate which is greater than 1
2.Gained skills working with database
3.running another software in the system becomes easier with virtual box and vagrant