"# optimiced" 

Script to scrape from both blogs on http://www.optimiced.com/
All the information is recorded into optimiced.db

Notes: 
- Articles from both blogs are in the same table, their origin is indicated in the language column
- Dates are formatted to be sortable
- Dates are in a yy/mm/dd format to be in chronological order when sorted.

DB Schema:
- Title: title of the article
- Date: date the article was posted, format: yy/mm/dd (hh/mm in bg articles) 
- Link: link to the article
- Text: Full text content of the article
- Lang: bg/en, indicates language/source
