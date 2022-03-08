# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

#cols = ["ExcerptPostId", "phone", "email", "WikiPostId", "country"]
#badges_cols = ['Id','TagExcerptPostId','Count','ExcerptPostId','WikiPostId','IsModeratorOnly']
badges_cols = ['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDate','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate'
 ,'ContentLicense']
badges_rows = []

# Parsing the XML file
xmlparse = Xet.parse('/data/StackOverflow/Communityposts/data/Posts.xml')
root = xmlparse.getroot()
	
j = 0

cnt = 0
for i in root:
	if (j % 100 == 0 and  j != 0):
		print (j," row ")
	Id = i.get("Id")
	PostTypeId = i.get("PostTypeId")
	AcceptedAnswerId = i.get("AcceptedAnswerId")
	ParentId = i.get("ParentId")
	CreationDate = i.get("CreationDate")
	DeletionDate = i.find("DeletionDate")
	Score = i.find("Score")
	ViewCount = i.get("ViewCount")
	Body = i.get("Body")
	OwnerUserId = i.get("OwnerUserId")
	OwnerDisplayName = i.find("OwnerDisplayName")
	LastEditorUserId = i.find("LastEditorUserId")
	LastEditorDisplayName = i.get("LastEditorDisplayName")
	LastEditDate = i.find("LastEditDate")
	LastActivityDate = i.find("LastActivityDate")
	Title = i.find("Title")
	Tags = i.find("Tags")
	AnswerCount = i.get("AnswerCount")
	CommentCount = i.get("CommentCount")
	FavoriteCount = i.get("FavoriteCount")
	ClosedDate = i.find("ClosedDate")
	CommunityOwnedDate = i.find("CommunityOwnedDate")
	ContentLicense = i.find("ContentLicense")

	badges_rows.append(
				{"Id": Id,
				"PostTypeId": PostTypeId,
				"AcceptedAnswerId": AcceptedAnswerId,
				"ParentId": ParentId,
				"CreationDate": CreationDate,
				"DeletionDate": DeletionDate,
				"Score": Score,
				"Body": Body,
				"OwnerUserId": OwnerUserId,
				"OwnerDisplayName": OwnerDisplayName,
				"LastEditorUserId": LastEditorUserId,
				"LastEditorDisplayName": LastEditorDisplayName,
				"LastEditDate": LastEditDate,
				"LastActivityDate": LastActivityDate,
				"Title": Title,
				"Tags": Tags,
				"AnswerCount": AnswerCount,
				"CommentCount": CommentCount,
				"FavoriteCount": FavoriteCount,
				"ClosedDate": ClosedDate,
				"CommunityOwnedDate": CommunityOwnedDate,
				"ContentLicense": ContentLicense
				}

				)
	j = j + 1




print("Parsing Finished.")
df = pd.DataFrame(badges_rows, columns=badges_cols)

# Writing dataframe to csv
df.reset_index(drop = True, inplace = True)
df.to_csv('/data/StackOverflow/Communityposts/data/Posts.csv', index = False)

# SAX parser
# https://stackoverflow.com/questions/59825575/split-large-xml-into-small-chunks
from xml.sax.handler import ContentHandler

class StudentReader(ContentHandler):
    def __init__(self, callback=None):
        self.column_order = 'ID,NAME,REGNUM,COUNTRY,SHORT_STD_DESC'
        self.current_student = None
        self.current_idx = None
        self.mapping = {key: idx for idx, key in enumerate(self.column_order.split(','))}
        self.num_cols = len(self.mapping)
        self.callback = callback

    def startElement(self, tag, attrs):
        if tag == 'STUDENT':
            # new student with correct number of columns
            self.current_student = [''] * self.num_cols
        elif tag in self.mapping:
            # which column are we writing to?
            self.current_idx = self.mapping[tag]
        else:
            self.current_idx = None

    def endElement(self, tag):
        if tag == 'STUDENT':
            if self.callback is not None:
                # when we have a callback, call it
                self.callback(self.current_student)
            else:
                # without a callback, just print to console (for debugging)
                print(self.current_student)
        elif tag in self.mapping:
            self.current_idx = None

    def characters(self, data):
        if self.current_idx is not None:
            self.current_student[self.current_idx] += data