import pandas as pd

# Path to the input Bookmarks file
inFile = ""

with open(inFile, encoding='utf-8') as file:

    lines = file.readlines()
    
    bookmarks = []
    folder = ""
    subfolder1 = ""
    subfolder2 = ""

    for txt1 in lines:
        if "<H3 " in txt1 and "Bookmarks" not in txt1:
            if folder == "":
                folder = txt1.split('">')[1].split('</')[0]
            else:
                if subfolder1 == "":
                    subfolder1 = txt1.split('">')[1].split('</')[0]
                else:
                    subfolder2 = txt1.split('">')[1].split('</')[0]
        elif "<A " in txt1 and "Bookmarks" not in txt1:
            url = [item.replace('HREF="', '').replace('"', '') for item in txt1.split() if 'HREF="' in item][0]
            bookmarks.append({
                'Folder': folder,
                'Subfolder1': subfolder1,
                'Subfolder2': subfolder2,
                'URL': url
            })

df = pd.DataFrame(bookmarks)
df['Subfolder2'].unique()

df.to_excel("Bookmarks Classification.xlsx", index=False)
