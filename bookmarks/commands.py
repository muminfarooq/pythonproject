import sys
from datetime import datetime

from database import DatabaseManager

db=DatabaseManager('bookmarks.db')

class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table('bookmarks',{
            'id':'integer primary key autoincrement',
            'title':'text not null',
            'url':'text not null',
            'notes':'text',
            'date_added':'text not null',
        })
class AddBookmarkCommand:
    def execute(self,data):
        data['date_added']=datetime.utcnow().isoformat()
        print(type(data))
        db.add('bookmarks',data)
        return 'Bookmark Added!!'
class ListBookmarksCommand:
    def __init__(self,order_by='date_added'):

       self.order_by=order_by
    def execute(self):
        return db.select('bookmarks',order_by=self.order_by).fetchall()
class DeleteBookmarkCommand:
    def execute(self,data):
        db.delete('bookmarks',{'id':data})
        return 'bookmarks deleted!!'
class QuitCommand:
    def execute(self):
        sys.exit()        

        