import sys
import csv
import os

from flaskProject.team_rosters.roster_scraper import scrape

teams_to_import = [1,2,3,5,6,7,8,9,
                   10,11,12,15,16,21,24, 27,
                   31, 32, 33, 39,40,45,51,52,
                   66,68,69,75,78,97]
# from roster_scraper import scrape
if __name__ == '__main__':

    with open('C:/Users/Hunte/PycharmProjects/Fc24Tournament/flaskProject/teams.csv', newline='',
              encoding="utf8") as csvfile:
        filtered_rows = []
        csv_reader = csv.reader(csvfile)
        i = 0
        for row in csv_reader:
            i = i + 1
            if i % 8 == 1:
                folder_path = f"{str(i)}-{str(i+7)}"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
            name = row[1]
            if len(row) > 4 and "www.fifacm.com/24/team/" in row[4]:
                print(f'"{name}": "{row[4]}"')
            if int(row[0]) in teams_to_import and len(row) > 4:
                if "nations=208" in row[4]:
                    row[4] = "https://www.fifacm.com/players?page=1&nations=208,30,28&&sort=overallrating&order=desc"
                if "Leagues=1003|1014" in row[4]:
                    row[4] = row[4].replace("|", ",")
                players = scrape(row[4])
                with open(f"{folder_path}/{row[1]}.csv", 'w', encoding="utf-8", newline='') as csvfile2:
                    csvfile2.writelines(players)
