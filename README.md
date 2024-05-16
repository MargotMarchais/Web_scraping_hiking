# Web scraping project: Building a holiday ideas database

## Context
My objective in this project was to build a database aggregating data from 3 well-known French websites dedicated to hiking and trekking trips: "Terres d'Aventures", "La Balaguère" and "Decathlon travel". It would become my personal "holiday ideas database".

To do so, I scraped the data from those sites and merged them after cleaning them.

## Methodology
Three web scraping methodologies have been applied. They were tailored to match each website's architecture.
- La Balaguère : Scrapy method
- Terres d'Aventures : Selenium method
- Decathlon travel : Requests and Beautifulsoup methods

A recap is available on my blog: https://margot-marchais-maurice.webflow.io/work/holiday-ideas-database 

## Output
Every method yielded a database that I cleaned in Dataiku DSS before merging all of them in a single database.

## Learning
This project allowed me to strengthen my Python skills (I had never done web scraping before).
I also learned how to perform data cleaning in Dataiku and manipulate the Visual Studio Code terminal.

