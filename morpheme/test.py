from konlpy.tag import Kkma
from konlpy.utils import pprint

sentence = "대통령은 국가의 독립·영토의 보전·국가의 계속성과 헌법을 수호할 책무를 진다. 환경권의 내용과 행사에 관하여는 법률로 정한다. 국회의원의 수는 법률로 정하되, 200인 이상으로 한다."
kkma = Kkma()

#pprint(kkma.sentences(sentence)) #문장을 나눔
#pprint(kkma.nouns(sentence)) #단어를 추출
pprint(kkma.pos(sentence)) #품사를 추출
