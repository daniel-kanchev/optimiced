from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('optimiced.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" CREATE TABLE IF NOT EXISTS
                         articles (title text, date text, link text, text text, lang text) """)

    def process_item(self, item, spider):

        # check for duplicates
        self.c.execute("""SELECT * FROM articles WHERE title = ? AND lang = ?""",
                       (item.get('title')[0], item.get('lang')[0],))
        duplicate = self.c.fetchall()
        if len(duplicate):
            return item

        # Insert values
        self.c.execute("INSERT INTO articles (title, date, link, text, lang) VALUES (?,?,?,?,?)", (
            item.get('title')[0], item.get('date')[0], item.get('link')[0], item.get('text')[0], item.get('lang')[0]))
        self.conn.commit()  # commit after every entry

        return item
