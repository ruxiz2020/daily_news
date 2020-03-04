from nltk.parse import CoreNLPParser
from util import all_df_cn_news

parser = CoreNLPParser('http://localhost:9001')

def parse_chinese(chinese_str):

    return list(parser.tokenize(chinese_str))


all_df_cn_news["parsed"] = all_df_cn_news["title"].apply(parse_chinese)

list_tokens = [a for b in all_df_cn_news.parsed.tolist() for a in b]
print(list_tokens)
