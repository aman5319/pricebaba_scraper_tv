# Bfore Scraper

1. [Install Python in windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)

2. [Install Git in windows](https://hackernoon.com/install-git-on-windows-9acf2a1944f0)

3. Install all the requirements from the requirements.txt file.

   1. ```
      pip install -r requirements.txt
      ```

      

4. For runing the spider // To scrape all TV details from PriceBaba

    1. ```
       scrapy crawl tvSpider
       ```

5. For Comparison in two csv files // To check which models have been added and which ones have to be deleted from our listings

   1. ```
      python automate.py new.csv old.csv
      ```

