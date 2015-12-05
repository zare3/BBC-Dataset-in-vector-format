import os
from json import loads, dumps





keywordsPath = '/Users/Home/AUC/Fall 15/Neural/Project/Article Classification/bag of words/all.vocabs.txt'
dictionary = []
with open(keywordsPath, "r") as word_list:
    dictionary = word_list.read().split('\n')


category  = ['business','entertainment','politics','sport', 'tech']

for address in category:
	rootdir = '/Users/Home/AUC/Fall 15/Neural/Project/Article Classification/bbc dataset/'+address+'/'
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			relDir = os.path.relpath(subdir,rootdir)
			relFilePath = os.path.join(relDir, file)
			filePath = os.path.join(subdir, file)
			fileObject = open (filePath,'r')
			fileContent = fileObject.read()
			fileObject.close()

			outputPath = '/Users/Home/AUC/Fall 15/Neural/Project/Article Classification/bbc dataset/vector representation/' + address + '/' + relFilePath
			outputPathFileObject = open(outputPath,'w')

			ans = []
			for el in dictionary:
				cnt = fileContent.count(el)
				if cnt > 0 :
					ans.append(cnt)
			for z in ans:
				outputPathFileObject.write(str(z))
				outputPathFileObject.write(' ')
			outputPathFileObject.write("\n\n\n")
			outputPathFileObject.close()
			print outputPath
			

