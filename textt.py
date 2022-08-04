from bs4 import BeautifulSoup
import re

def ch_var(self,path,col_val,row_val):
        #start
        sample_page = path

        dic={col_val[i]:row_val[i] for i in range(len(col_val)) }
        
        print(dic)
        for p in sample_page.paragraphs:
            inline = p.runs
            for i in range(len(inline)):
                text = inline[i].text
                for key in dic.keys():
                    if key in text:
                        text=text.replace(key,dic[key])
                        inline[i].text = text
        return sample_page


html = """<p class="description" dir="ltr">Name is salary a fine position man. <br></p>"""
dic = {
            'NAME':name,
            '[POST]':position,
            '[SALARY]' : salary,
        }

soup = BeautifulSoup(html)
target = soup.find_all(text=re.compile(r'Name'))
for v in target:
    v.replace_with(v.replace('Name','Id'))
print(soup)



