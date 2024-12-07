import requests
from bs4 import BeautifulSoup as bs
import json
URL = "https://mgkct.minskedu.gov.by/%D0%BE-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B5/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2"
response = requests.get(URL)
if response.status_code == 200: 
    soup = bs(response.text, "html.parser")
    #print(soup.prettify())
    h3Elements = soup.find_all("h3")
    liElements = soup.select(".tss")
    inform= []
    if len(h3Elements) == len(liElements):  # Проверка на соответствие количества элементов
        for i, teacher in enumerate(h3Elements):
            print(f"{i+1}. Teacher: {teacher.text}; Post: {liElements[i].text}")
            teacher_info ={
                "Teacher": teacher.text,
                "Post": liElements[i].text
            }
            inform.append(teacher_info)

        with open("data.json", "w") as json_file:
            json.dump(inform, json_file, indent=4)

        with open("index1.html", "w") as file_html:
            file_html.write("""
<!DOCTYPE html>
<html lang="ru">

<head>
    <title>Преподаватели МГКЦТ</title>
    <style>
        body {
            font-family: 'Courier New', Courier, monospace;
            font-size: 20px;
            background-color: #FFF5EE
        }

        h1 {
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            color: #000000;
        }

        table {
            width: 100%;
            background-color: #c7a1c4;
            border: 5px double #857b7b;
            ;
        }

        th {
            padding: 8px;
            text-align: center;
            padding: 5px solid #ddd;
            border: 1px solid #857b7b;
            background-color: #eaced7;
        }
        
        td {
            padding: 8px;
            text-align: center;
            padding: 5px solid #ddd;
            border: 1px solid #857b7b;
            background-color: #FFF0F5;
        }

        p {
            padding: 15px;
            color: #cbb8cb;
        }
    </style>
</head>

<body>
    <h1>Преподавательский состав</h1>
    <table>
        <tr>
            <th>№</th>
            <th>Teacher</th>
            <th>Post</th>
        </tr>
        """)
            
            with open("data.json", "r") as input_file:
                text = json.load(input_file)
                for i,item in enumerate(text):
                    file_html.write(f"<tr><td>{i+1}</td><td>{item['Teacher']}</td><td>{item['Post']}</td></tr>\n")

                file_html.write("""
    </table>
    <p><a href = "https://mgkct.minskedu.gov.by/%D0%BE-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%B4%D0%B6%D0%B5/%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B8%D0%B2">Источник данных</a></p>
</body
</html>
        """)
        
        print("HTML файл создан.")
else:
    print(f"Ошибка: {response.status_code}")
    exit()
    
