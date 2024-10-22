from employee import Writter, Boss
from section import Section

def fill_data(writer_news_list,writer_sport_list,sections_list):
    writer_news_list.append(
        Writter("Antonio",1)
    )
    writer_news_list.append(
        Writter("Daniel",2)
    )
    writer_news_list.append(
        Writter("Santiago",3)
    )
    writer_news_list.append(
        Writter("Erick",4)
    )
    writer_news_list.append(
        Writter("Jose",5)
    )
    writer_news_list.append(
        Writter("Pedro",6)
    )

    writer_sport_list.append(
        Writter("Juan",1)
    )
    writer_sport_list.append(
        Writter("Peter",2)
    )
    writer_sport_list.append(
        Writter("Jonathan",3)
    )
    writer_sport_list.append(
        Writter("Ray",4)
    )
    sections_list.append(
        Section("Sports",Boss("Ignacio",24,writer_sport_list))
    )
    sections_list.append(
        Section("News",Boss("Maria",26,writer_news_list))
    )

def main():
    writer_sport_list = []
    writer_news_list = []
    sections_list = []
    fill_data(writer_news_list,writer_sport_list,sections_list)
    for section in sections_list:
        section.boss_writer.supervise()

main()