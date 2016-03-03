#coding=utf8
import os
import keyword
import string

dirName = "./../SourceArticles/"
resultDir = "./../Results/"

# get files
files = os.listdir( dirName );

# get keywords and catefory nums
keywordFile = open( "../keywordSetting", "r" );
keywordsLine = keywordFile.read().split('\r\n');
keywords = [];
categories = [];

for i in range( len(keywordsLine) ):
	lineSplit = keywordsLine[i].split(',');
	keywords.append(lineSplit[0]);

	# if there is category setting
	if( len(lineSplit) > 1 ):
		categories.append( int(lineSplit[1]) );
	else:
		categories.append(0);

totalCounter = [];
totalCategoryCounter = [0,0,0,0,0,0,0,0,0,0];

# init list
for i in range( len(keywords) ):
	totalCounter.append( 0 );

# read articles
for fileName in files:

	# if it is hidden file in macos
	if fileName[0] != '.' :
		
		print( "正在解析 " + fileName + " 檔案 ..." )

		openObj = open( dirName + fileName, "r" )
		article = openObj.read()
		article = article.lower()

		resultStr = ""
		categoryStr = ""
		categoryCounter = [0,0,0,0,0,0,0,0,0,0];


		for i in range( len(keywords) ):

			targetKey = keywords[i]
			num = keyword.countKeyWords( targetKey.lower(), article)
			resultStr += targetKey + ',' + str(categories[i]) + ',' + str(num) + '\r\n'

			#add result into total counter
			totalCounter[i] += num;

			#add result into categories
			categoryCounter[categories[i]] += num;

		# process category str
		for i in range( len(categoryCounter) ):
			categoryStr += "Category " + str(i) + ',' + str(categoryCounter[i]) + '\r\n'

			#add result into total category counter
			totalCategoryCounter[i] += categoryCounter[i];

		resultStr += " , \r\n" + categoryStr

		# save file
		writeFile = open( resultDir + fileName + ".csv", "w" )
		writeFile.write( resultStr )
		writeFile.write
		writeFile.close()


# write into total result
totalStr = ""

for i in range( len(keywords) ):
	keyName = keywords[i]
	totalStr += keyName + ',' + str(categories[i]) + ',' + str( totalCounter[i] ) + '\r\n'

totalStr += " , \r\n"

for i in range( len(totalCategoryCounter) ):
	totalStr += "Category " + str(i) + ',' + str(totalCategoryCounter[i]) + '\r\n';

totalResultFile = open( resultDir + "TotalResult.csv", "w")	
totalResultFile.write( totalStr )
totalResultFile.close()

print ("計算完成！")

