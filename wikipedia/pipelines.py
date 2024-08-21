# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from dotenv import load_dotenv
import os


class WikipediaPipeline:
    def __init__(self):
        load_dotenv()
        self.conn = mysql.connector.connect(
            host = os.getenv("HOST")
            user = os.getenv("USER")
            password = os.getenv("PASSWORD")
        )
        self.cur = self.conn.cursor()

        with open(code.sql, 'r') as file :
            create_db_table = file.read()

        self.cur.execute(create_db_table)

            

    def process_item(self, item, spider):
        self.cur.execute("SELECT * FROM User WHERE product_name = %s ", (item['product_name']))
        result = self.cur.fetchone()

        if result:
            result.logger.warn('Item already exist in database : %s' % item['product_name'])
        else:
            self.cur.execute('INSERT INTO User(product_name, member_price, retail_price, date_now, last_date) VALUE(%s, %s, %s, NOW(), NOW()) DUPLICATE KEY UPDATE last_date = NOW()', (str(item['product_name']), float(item['member_price']), float(item['retail_price'])))

        self.connection.commit()
        return item
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
