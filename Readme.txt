This program analyzes the a PostgreSQL database for a fictional news website.

A better view of the data has been prepared in an excel file.
(Note: The excel file is big and may take some time to load)

Programs Needed

Python3, Vagrant, Oracle VM VirtualBox (gitbash as well if you have a windows operating system)

Instructions to Run

Open the "FSND-Virtual-Machine" folder that has been provided

go to the vagrant directory.
should be (fsnd-virtual-machine\FSND-Virtual-Machine\vagrant)
put the python file: "log analysis.py" and "newsdata.sql" here

open the the bash prompt on the vagrant folder by right clicking and finding the terminal option.
(this will be the "git bash here" option for windows users)

type: "vagrant up". This will set up the ubuntu virtual machine and "turn on" the virtual machine
note: this may take a while as it downloads ubuntu 16.04

type: "vagrant ssh" to log in

type: "cd /vagrant" to access the directory that has the folders we uploaded

type: "psql -d news -f newsdata.sql" to load tables of the sql data

type: "python3 log_analysis.py" to execute





References

https://stackoverflow.com/questions/13674031/how-to-get-the-top-10-values-in-postgresql
http://www.sqlines.com/oracle/functions/substr
https://www.postgresql.org/message-id/FCDB9A00-31E0-48A2-98BE-39977344699D%40yahoo.com
https://stackoverflow.com/questions/24441319/postgres-like-with-column-value-as-substring
https://stackoverflow.com/questions/13274679/like-with-on-column-names
https://unix.stackexchange.com/questions/285447/delete-rows-from-postgres-database-contain-string-sentence
https://stackoverflow.com/questions/10909902/how-to-add-number-of-days-in-postgresql-datetime
http://ben.goodacre.name/tech/Group_by_day,_week_or_month_%28PostgreSQL%29
https://www.postgresql.org/docs/8.1/static/functions-math.html
https://social.msdn.microsoft.com/Forums/sqlserver/en-US/fdc3cbf3-2fa1-4d3c-952e-3da6a4094008/how-to-display-values-with-percentage-symbol-in-query-?forum=transactsql