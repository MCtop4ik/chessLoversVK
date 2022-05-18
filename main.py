import random
import time

from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from decouple import config


def write_msg(user_id, message, key=None):
    post = {'user_id': user_id, "random_id": random.randint(1, 1000), 'message': message}
    if key is not None:
        post["keyboard"] = key.get_keyboard()
    else:
        pass
    vk_session.method('messages.send', post)


vk_session = vk_api.VkApi(token=config('TOKEN', default=''))
links = ["http://vismyt-001-site1.htempurl.com/tabl_glavnay_kom.php?turnir=Blitzkarixera-besenniuysezon2022",
         "http://vismyt-001-site1.htempurl.com/tabl_glavnay_kom.php?turnir=Bulletkarixera-besenniuysezon2022",
         "https://lichess.org/tournament/1lbnZe5e", "https://lichess.org/tournament/kI4JoWQP",
         "https://lichess.org/tournament/38blW90w", "https://lichess.org/tournament/H9smyPan",
         "https://lichess.org/tournament/1lbnZe5e", "https://lichess.org/tournament/95DR0AJ8",
         "https://lichess.org/tournament/GmsuyFUB", "https://lichess.org/tournament/95DR0AJ8"]

teams = ["sonysergeeva", "AleksandraYezerskaya", "GornyiA", "shubin_miroslav", "OstapTuzhilkin",
         "Gazzaeva_Liyana", "Sofia_Salakhova08", "Panteleev_Oleg", "GuskovaMarya2010", "M9_999",
         "Zaynutdinov_Roman", "Fedor_Chekhovskikh", "Mikhail_Chekhovskikh", "mtm009", "Batikyan_Rafael",
         "Maksim_Khomik", "Gleb_Tuhzilkin", "Maksim_Rezyapkin", "Nikita_RezyapkiN", "jonibek23",
         "polinaSergeeva", "EgorkkG", "NuvaltsevVlad", "Arsenii_Zakharov ✓", "Artem_Burdin_2",
         "Loshpedrus", "Ivanov_Maxim-63", "RomanStarkov", "T_44", "ArtemLazunin",
         "Shibanov-Konstantin1", "Saraev_Iliya", "Saraeva_Maya", "GlebF10", "Guskov-E_2012",
         "GordeyG", "Bogdanov_Makar", "OstapTuzhilkin", "svyatoslav_bokov", "Stas121213"]

link_site_ruChess = ["385658", "AleksandraYezerskaya", "72314", "shubin_miroslav", "385660",
                     "385654", "414493", "Panteleev_Oleg", "GuskovaMarya2010", "M9_999",
                     "129511", "350678", "Mikhail_Chekhovskikh", "90810", "350665",
                     "410636", "362722", "350675", "350676", "430503",
                     "390002", "EgorkkG", "267753", "410635", "362721",
                     "385652", "273823", "385659", "267815", "350661",
                     "Shibanov-Konstantin1", "Saraev_Iliya", "Saraeva_Maya", "GlebF10", "Guskov-E_2012",
                     "GordeyG", "Bogdanov_Makar", "385660", "svyatoslav_bokov", "350658"]

shortInfo = ["sonysergeeva",
             "AleksandraYezerskaya", "GornyiA", "shubin_miroslav", "OstapTuzhilkin",
             "Gazzaeva_Liyana",
             "люблю шахматы, обожаю танцы, хожу на плавание. люблю читать. "
             "слушаю в основном какие-нибудь английские песни🤷‍♀🤷‍♀🤷‍♀",
             "Panteleev_Oleg", "GuskovaMarya2010", "M9_999",
             "Zaynutdinov_Roman", "Fedor_Chekhovskikh", "Mikhail_Chekhovskikh", "mtm009", "Batikyan_Rafael",
             "Maksim_Khomik", "Gleb_Tuhzilkin", "Maksim_Rezyapkin", "Nikita_RezyapkiN", "jonibek23",
             "polinaSergeeva", "EgorkkG", "NuvaltsevVlad",
             "Создатель этого бота) Псевдонимы: Zetni/ZetniSuper/MCtop4ik",
             "Artem_Burdin_2",
             "Loshpedrus", "Ivanov_Maxim-63", "RomanStarkov", "T_44", "ArtemLazunin",
             "Shibanov-Konstantin1", "Saraev_Iliya", "Saraeva_Maya", "GlebF10", "Guskov-E_2012",
             "GordeyG", "Bogdanov_Makar", "OstapTuzhilkin", "svyatoslav_bokov", "Stas121213"]

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

team_id = 0

name_id = 0


def startBot():
    global team_id
    global name_id
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.from_user:
                print(event.text)
                if event.text.lower() == "hello" or event.text.lower() == "в начало":
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('ИНФА про Лигу Наций', color=VkKeyboardColor.PRIMARY)
                    write_msg(event.user_id, "Привет", keyboard)
                elif event.text.lower() == "инфа про лигу наций":
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('SamGTU Akademy DNK', color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('SamGTU DNK Akademy 2 team', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('SamGTU DNK 3 team', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('SamGTU DNK 4 team', color=VkKeyboardColor.POSITIVE)
                    write_msg(event.user_id, "Выбери команду из списка)", keyboard)
                elif event.text.lower() == 'samgtu akademy dnk':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('Blitz', color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('Bullet', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Team', color=VkKeyboardColor.POSITIVE)
                    team_id = 1
                    name_id = 2
                    write_msg(event.user_id, "Выбери режим)", keyboard)
                elif event.text.lower() == 'samgtu dnk akademy 2 team':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('Blitz', color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('Bullet', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Team', color=VkKeyboardColor.POSITIVE)
                    team_id = 2
                    name_id = 1
                    write_msg(event.user_id, "Выбери режим)", keyboard)
                elif event.text.lower() == 'samgtu dnk 3 team':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('Blitz', color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('Bullet', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Team', color=VkKeyboardColor.POSITIVE)
                    team_id = 3
                    name_id = 0
                    write_msg(event.user_id, "Выбери режим)", keyboard)
                elif event.text.lower() == 'samgtu dnk 4 team':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button('Blitz', color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('Bullet', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Team', color=VkKeyboardColor.POSITIVE)
                    team_id = 4
                    name_id = 3
                    write_msg(event.user_id, "Выбери режим)", keyboard)
                elif event.text.lower() == 'blitz':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_openlink_button('Ссылка на турнир 😎', links[1 + team_id * 2])
                    keyboard.add_line()
                    keyboard.add_openlink_button('Таблица 😣', links[0])
                    keyboard.add_line()
                    keyboard.add_button('В НАЧАЛО', color=VkKeyboardColor.POSITIVE)
                    write_msg(event.user_id, "Выбирай)", keyboard)
                elif event.text.lower() == 'bullet':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_openlink_button('Ссылка на турнир 😎', links[team_id * 2])
                    keyboard.add_line()
                    keyboard.add_openlink_button('Таблица 😣', links[1])
                    keyboard.add_line()
                    keyboard.add_button('В НАЧАЛО', color=VkKeyboardColor.POSITIVE)
                    write_msg(event.user_id, "Выбирай)", keyboard)
                elif event.text.lower() == 'team':
                    keyboard = VkKeyboard(one_time=False)
                    keyboard.add_button("#" + teams[name_id * 10], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_button("#" + teams[name_id * 10 + 1], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button("#" + teams[name_id * 10 + 2], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_button("#" + teams[name_id * 10 + 3], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button("#" + teams[name_id * 10 + 4], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_button("#" + teams[name_id * 10 + 5], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button("#" + teams[name_id * 10 + 6], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_button("#" + teams[name_id * 10 + 7], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button("#" + teams[name_id * 10 + 8], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_button("#" + teams[name_id * 10 + 9], color=VkKeyboardColor.SECONDARY)
                    keyboard.add_line()
                    keyboard.add_button('В НАЧАЛО', color=VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, "Члены команды)", keyboard)
                elif event.text.lower()[0] == '#':
                    for i in range(len(teams)):
                        if "#" + teams[i] == event.text:
                            keyboard = VkKeyboard(one_time=False)
                            keyboard.add_openlink_button('Ссылка на RuChess.Ratings 😎',
                                                         "https://ratings.ruchess.ru/people/" +
                                                         link_site_ruChess[i])
                            keyboard.add_line()
                            keyboard.add_openlink_button('Lichess 😣', "https://lichess.org/@/" + teams[i])
                            keyboard.add_line()
                            keyboard.add_button('В НАЧАЛО', color=VkKeyboardColor.POSITIVE)
                            write_msg(event.user_id, shortInfo[i], keyboard)
                else:
                    write_msg(event.user_id, "Введи hello для начала")
            elif event.from_chat:
                print(event.text)
                write_msg(event.сhat_id, event.random_id, "вторая фраза")


while True:
    while True:
        try:
            startBot()
        except Exception as e:
            time.sleep(3)
            print(e)
