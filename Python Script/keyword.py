#coding=utf8
#keyword.py

def countKeyWords ( inputKeyWord, inputArticle ):
	returnNum = inputArticle.count(inputKeyWord, 0, len(inputArticle))
	return returnNum