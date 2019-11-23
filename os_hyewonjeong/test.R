install.packages('tm')
install.packages('stringr')
install.packages('wordcloud')
install.packages('NLP')
install.packages('RColorBrewer')
install.packages('sp')
library(tm)
library(stringr)
library(wordcloud)
library(NLP)
library(RColorBrewer)
library(sp)
#파일 이름 설정
curwd <- "C:/Users/win10-a287/PycharmProjects/python37/outsource/os_hyewonjeong"
setwd(curwd)
filename <- "cheese.txt"
cloudname <- "cheese_cloud.png"
#내용 읽어오기
contents<-readLines(file(filename, encoding="UCS-2LE"))
#줄 병합
contents <- paste(contents, collapse = " ")
contents <- paste(contents, collapse = "\n")
#불필요 요소 제거
contents <- gsub("\"","", contents)
contents <- gsub('“',"", contents)
contents <- gsub('”',"", contents)
contents <- stripWhitespace(contents)

#모두 소문자 처리
contents <- tolower(content)
#불용어 처리
contents <- removeWord(contents, stopwords())
contents <- stripWhitespace(contents)
contents <- str_split(contents, pattern="\s+")
class_contents <- unlist(contents)
