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

# https://stackoverflow.com/questions/16669428/process-very-large-20gb-text-file-line-by-line

'<row Id="4" PostTypeId="1" AcceptedAnswerId="7" CreationDate="2008-07-31T21:42:52.667" Score="709" ViewCount="55543" Body="&lt;p&gt;I want to use a &lt;code&gt;Track-Bar&lt;/code&gt; to change a &lt;code&gt;Form&lt;/code&gt; opacity.&lt;/p&gt;&#xA;&lt;p&gt;This is my code:&lt;/p&gt;&#xA;&lt;pre class=&quot;lang-cs prettyprint-override&quot;&gt;&lt;code&gt;decimal trans = trackBar1.Value / 5000;&#xA;this.Opacity = trans;&#xA;&lt;/code&gt;&lt;/pre&gt;&#xA;&lt;p&gt;When I build the application, it gives the following error:&lt;/p&gt;&#xA;&lt;blockquote&gt;&#xA;&lt;pre class=&quot;lang-none prettyprint-override&quot;&gt;&lt;code&gt;Cannot implicitly convert type decimal to double&#xA;&lt;/code&gt;&lt;/pre&gt;&#xA;&lt;/blockquote&gt;&#xA;&lt;p&gt;I have tried using &lt;code&gt;trans&lt;/code&gt; and &lt;code&gt;double&lt;/code&gt;, but then the &lt;code&gt;Control&lt;/code&gt; doesnt work. This code worked fine in a past VB.NET project.&lt;/p&gt;&#xA;" OwnerUserId="8" LastEditorUserId="3072350" LastEditorDisplayName="Rich B" LastEditDate="2021-02-26T03:31:15.027" LastActivityDate="2021-02-26T03:31:15.027" Title="How to convert a Decimal to a Double in C#?" Tags="&lt;c#&gt;&lt;floating-point&gt;&lt;type-conversion&gt;&lt;double&gt;&lt;decimal&gt;" AnswerCount="14" CommentCount="3" FavoriteCount="51" CommunityOwnedDate="2012-10-31T16:42:47.213" ContentLicense="CC BY-SA 4.0" />'