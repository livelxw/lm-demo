# import os

# ENG_NEWS_2020_10K_DIR = os.getenv('ENG_NEWS_2020_10K_DIR')


# def prepare_eng_news_2020_10K():
#     with open(os.path.join(ENG_NEWS_2020_10K_DIR, 'eng_news_2020_10K-sentences.txt'), encoding="utf-8") as f:
#         lines = [i.split('\t')[-1] for i in f.readlines()]
#     if not os.path.exists('./data'):
#         os.mkdir('./data')
#     with open('./data/eng_news_2020_10K.txt', 'w', encoding="utf-8") as f:
#         f.writelines(lines)


# if __name__ == "__main__":
#     prepare_eng_news_2020_10K()
