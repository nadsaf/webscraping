# Webscraping Digimon using Beautifulsoup


Simple python project saving digimon data from webscraping [Wikilist of Digimon ](https://wikimon.net/Visual_List_of_Digimon) to MySQL


## Activate MySQL server, create a database with a table inside: 
```bash
$ mysql -u username -p
$ Enter password: *******
$ create database digimon;
$ use digimon;
$ create table digimon(
    id int auto_increment,
    nama varchar(200),
    gambar varchar(200),
    primary key (id));
```

## To run digimon.py file, you need to install:
- BeautifulSoup
- MySQL connector
```
$ pip install beautifulsoup4 MySQL-connector-python
```

