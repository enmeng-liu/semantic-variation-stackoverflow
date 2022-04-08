import xml.etree.ElementTree as ET
import csv

xml_path = '/data/StackOverflow/Communityposts/data/Posts.xml'
csv_path = "/data/StackOverflow/Communityposts/data/Posts.csv"
bunch_size = 1000000
# csv_path = "Posts.csv"
# bunch_size = 10

cols = ['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDate','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','Tags','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate'
 ,'ContentLicense']
# single_cols = ['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','ViewCount','Body','OwnerUserId', 'LastEditorDisplayName','AnswerCount','CommentCount','FavoriteCount']
# list_cols = ['DeletionDate', 'Score', 'OwnerDisplayName', 'LastEditorUserId', 'LastEditDate', 'LastActivityDate', 'Title', 'Tags', 'ClosedDate', 'CommunityOwnedDate', 'ContentLicense']

dict_list = []
with open(xml_path, mode="r") as xml_file, open(csv_path, mode="a") as csv_file:
    cnt = 0
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()

    for line in xml_file:
        cnt += 1
        if (cnt % bunch_size == 0 and cnt != 0):
            print(cnt, "row")
            writer.writerows(dict_list)
            dict_list = []

        line.strip()
        try:
            root = ET.fromstring(line)
            if root.tag == "row":
                row_dict = {}
                for col in cols:
                    row_dict[col] = root.attrib.get(col)
                dict_list.append(row_dict)
        except ET.ParseError:
            print(line)

    print("Parsing completed.")
    writer.writerows(dict_list)
    print("CSV writing completed.")

