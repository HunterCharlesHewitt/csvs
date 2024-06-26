from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

teams = [
    "Argentina",
    "France",
    "Belgium",
    "Brazil",
    "England",
    "Portugal",
    "Netherlands",
    "Spain",
    "Croatia",
    "Italy",
    "Morocco",
    "USA",
    "Columbia",
    "Uruguay",
    "Mexico",
    "Germany",
    "Japan",
    "Senegal",
    "Switzerland",
    "Iran",
    "Denmark",
    "South Korea",
    "Australia",
    "Ukraine",
    "Austria",
    "France b team",
    "Poland",
    "Germany b team",
    "Italy b team",
    "Portugal b team",
    "Hungary",
    "Sweden",
    "Wales",
    "England b team",
    "Ecuador",
    "Peru",
    "Serbia",
    "Russia",
    "Czechia",
    "Qatar",
    "France c team",
    "Egypt",
    "Ivory Coast",
    "Nigeria",
    "Scotland",
    "Chile",
    "Turkey",
    "Panama",
    "Algeria",
    "Slovakia",
    "Norway",
    "Romania",
    "Canada",
    "Cameroon",
    "Mali",
    "Greece",
    "Costa Rica",
    "Jamaica",
    "Venezuela",
    "Iraq",
    "Saudi Arabia",
    "Slovenia",
    "Paraguay",
    "South Africa",
    "England c team",
    "Ireland",
    "DR Congo",
    "Finland",
    "Ghana",
    "Cape Verde",
    "Albania",
    "Spain c team",
    "Germany c team",
    "Burkina Faso",
    "Iceland",
    "Macedonia",
    "Montenegro",
    "Northern Ireland",
    "Georgia",
    "Bosnia",
    "Guinea",
    "Honduras",
    "Israel",
    "Bulgaria",
    "Gabon",
    "Bolivia",
    "Luxembourg",
    "China",
    "Equatorial Guinea",
    "Zambia",
    "Angola",
    "Palestine",
    "Armenia",
    "Trinidad & Tobago",
    "Madagascar",
    "Kosovo",
    "New Zealand",
    "Kenya",
    "North Korea",
    "China b team",
    "Congo",
    "Guinea Bissau",
    "Libya",
    "Comoros",
    "Togo",
    "India",
    "Cyprus",
    "United Baltic Republic",
    "Zimbabwe",
    "Gambia",
    "Suriname",
    "Liberia",
    "Dominican Republic",
    "China c team",
    "India b team",
    "Spain 16 year olds",
    "England 16 year olds",
    "France 16 year olds",
    "Netherlands 16 year olds",
    "Argentina 16 year olds",
    "Germany 16 year olds",
    "Poland 16 year olds",
    "Sweden 16 year olds",
    "Turkey 16 year olds",
    "Australia 16 year olds",
    "USA 16 year olds",
    "Italy 16 year olds",
    "Wales 16 year olds"
]

existing_teams = {"Argentina": " https://www.fifacm.com/24/team/1369/argentina",
                  "France": " https://www.fifacm.com/24/team/1335/france",
                  "Belgium": " https://www.fifacm.com/24/team/1325/belgium",
                  "England": " https://www.fifacm.com/24/team/1318/england",
                  "Portugal": " https://www.fifacm.com/24/team/1354/portugal",
                  "Netherlands": " https://www.fifacm.com/24/team/105035/holland",
                  "Spain": " https://www.fifacm.com/24/team/1362/spain",
                  "Croatia": " https://www.fifacm.com/24/team/1328/croatia",
                  "Italy": " https://www.fifacm.com/24/team/1343/italy",
                  "Morocco": " https://www.fifacm.com/24/team/111111/morocco",
                  "USA": " https://www.fifacm.com/24/team/1387/united-states",
                  "Mexico": " https://www.fifacm.com/24/team/1386/mexico",
                  "Germany": " https://www.fifacm.com/24/team/1337/germany",
                  "Denmark": " https://www.fifacm.com/24/team/1331/denmark",
                  "Ukraine": " https://www.fifacm.com/24/team/1366/ukraine",
                  "Poland": " https://www.fifacm.com/24/team/1353/poland",
                  "Hungary": " https://www.fifacm.com/24/team/1886/hungary",
                  "Sweden": " https://www.fifacm.com/24/team/1363/sweden",
                  "Wales": " https://www.fifacm.com/24/team/1367/wales",
                  "Czechia": " https://www.fifacm.com/24/team/1330/czech-republic",
                  "Qatar": " https://www.fifacm.com/24/team/111527/qatar",
                  "Scotland": " https://www.fifacm.com/24/team/1359/scotland",
                  "Norway": " https://www.fifacm.com/24/team/1352/norway",
                  "Romania": " https://www.fifacm.com/24/team/1356/romania",
                  "Ireland": " https://www.fifacm.com/24/team/1355/republic-of-ireland",
                  "Finland": " https://www.fifacm.com/24/team/1334/finland",
                  "Ghana": " https://www.fifacm.com/24/team/111462/ghana",
                  "Iceland": " https://www.fifacm.com/24/team/1341/iceland",
                  "Northern Ireland": " https://www.fifacm.com/24/team/110081/northern-ireland"
                  }

flags = [
    "https://www.worldometers.info//img/flags/small/tn_ar-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_fr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_be-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_br-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_po-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_nl-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sp-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_hr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_it-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_mo-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_us-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_co-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uy-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_mx-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ja-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sg-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sz-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ir-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_da-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ks-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_as-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_up-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_au-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_fr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_pl-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_it-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_po-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_hu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sw-flag.gif",
    "https://cdn.britannica.com/62/4962-050-E0A65F01/Flag-Wales.jpg",
    "https://www.worldometers.info//img/flags/small/tn_uk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ec-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_pe-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ri-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_rs-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ez-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_qa-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_fr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_eg-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_iv-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ni-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sc-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ci-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_tu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_pm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ag-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_lo-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_no-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ro-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ca-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_cm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ml-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_cs-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_jm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ve-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_iz-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sa-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_si-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_pa-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sf-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ei-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_congo-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_fi-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gh-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_cv-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_al-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sp-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uv-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ic-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_mk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_mj-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gg-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_bk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gv-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ho-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_is-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_bu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gb-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_bl-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_lu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ch-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ek-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_za-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ao-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_palestine-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_am-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_td-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ma-flag.gif",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Flag_of_Kosovo.svg/238px-Flag_of_Kosovo.svg.png",
    "https://www.worldometers.info//img/flags/small/tn_nz-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ke-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_kn-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ch-flag.gif",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_the_Republic_of_the_Congo.svg/255px-Flag_of_the_Republic_of_the_Congo.svg.png",
    "https://www.worldometers.info//img/flags/small/tn_pu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ly-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_cn-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_to-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_in-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_cy-flag.gif",
    "https://www.worldometers.info/img/flags/small/tn_lg-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_zi-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ga-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ns-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_li-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_dr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ch-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_in-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sp-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_uk-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_fr-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_nl-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_ar-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_gm-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_pl-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_sw-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_tu-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_as-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_us-flag.gif",
    "https://www.worldometers.info//img/flags/small/tn_it-flag.gif",
    "https://cdn.britannica.com/62/4962-050-E0A65F01/Flag-Wales.jpg"
]

def scroll_page(driver, pause_time=0.1, scroll_increment=500):
    """Scroll down the page incrementally."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    new_height = 0

    while new_height < last_height:
        driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
        time.sleep(pause_time)
        new_height += scroll_increment
        current_height = driver.execute_script("return document.body.scrollHeight")
        if new_height >= current_height:
            break
        last_height = current_height


def extract_player_info(row):
    player_info = {}
    name_div = row.find('div', class_='player-name')
    if name_div:
        player_info['name'] = name_div.text.strip()
        href = name_div.find('a')['href']
        player_info['id'] = href.split('/')[2]
    player_info['name'] = row.find('div', class_='player-name').text.strip()
    player_info['overall'] = row.find('div', class_='player-overall').text.strip()
    # player_info['team'] = row.find('div', class_='mb-1').find('img').get('data-original-title')
    player_info['team'] = ""
    position_div = row.find('div', class_='player-position-cln')
    player_info['position'] = position_div.text.split('|')[0].strip() if position_div else None
    if "," in player_info['position']:
        player_info['position'] = player_info['position'].replace(",", " |")
    img_url = row.find('img', class_='player-img-info')['src']
    player_info['img_url'] = img_url
    if "/imgs/fc24/players/notfound_player.png" in img_url or "notfound_0.png" in img_url:
        player_info['img_url'] = "https://www.fifacm.com/content/media/imgs/fc24/players/notfound_player.png"
    return player_info


url = "https://www.fifacm.com/players?page=1&player_rating=81-99&real_face=1&nations=54&sort=overallrating&order=desc"
if __name__ == "__main__":
# def scrape(url):
    webdriver_path = 'C:/Users/Hunte/chromedriver.exe'  # Update this to the correct path

    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    time.sleep(1)
    scroll_page(driver)

    html_content = driver.page_source

    soup = BeautifulSoup(html_content, 'html.parser')
    player_rows = soup.find_all('tr', class_='player-row')

    players = []
    i = 0
    for row in player_rows:
        player_info = extract_player_info(row)
        players.append(player_info)
    ret_players = []
    for player in players:
        str = f"{player['id']}, {player['name']}, {player['overall']}, {player['position']}, {player['team']}, {player['img_url']}"
        print(str)
        ret_players.append(str)

    # return ret_players
