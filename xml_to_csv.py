from xml.sax.handler import ContentHandler
import xml.sax


xml_path = '/data/StackOverflow/Communityposts/data/Posts.xml'
csv_path = "/data/StackOverflow/Communityposts/data/Posts.csv"

cols = ['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDate','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate'
 ,'ContentLicense']
single_cols = ['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','ViewCount','Body','OwnerUserId', 'LastEditorDisplayName','AnswerCount','CommentCount','FavoriteCount']
list_cols = ['DeletionDate', 'Score', 'OwnerDisplayName', 'LastEditorUserId', 'LastEditDate', 'LastActivityDate', 'Title', 'Tags', 'ClosedDate', 'CommunityOwnedDate', 'ContentLicense']


class PostsParser(ContentHandler):
    def __init__(self, callback=None):
        self.columns = cols
        self.current_row = None
        self.current_index = None
        self.mapping = {key: i for i, key in enumerate(self.columns)}
        self.num_columns = len(self.mapping)
        self.callback = callback

    def startElement(self, tag, attrs):
        if tag == 'row':
            self.current_row = [''] * self.num_columns
        elif tag in self.mapping:
            self.current_index = self.mapping[tag]
        else:
            self.current_index = None
    
    def endElement(self, tag):
        if tag == 'row':
            if self.callback is not None:
                self.callback(self.current_row)
            else:
                #  write to csv file
                # print(self.current_row)
                pass
        elif tag in self.mapping:
            self.current_index = None
    
    def characters(self, data):
        print("get data: " + data)
        if self.current_index is not None:
            self.current_row[self.current_index] += data


handler = PostsParser()
xml.sax.parse(xml_path, handler)