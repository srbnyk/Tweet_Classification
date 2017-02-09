import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
# Hashtags
hash_regex = re.compile(r"#(\w+)")
def hash_repl(match):
	return '__HASH_'+match.group(1).upper()

# Handles
hndl_regex = re.compile(r"@(\w+)")
def hndl_repl(match):
	return '__HNDL'#_'+match.group(1).upper()

# URLs
url_regex = re.compile(r"(http|https|ftp)://[a-zA-Z0-9\./]+")
url_regex2 = re.compile(r"(http|https|ftp):.+[^\s]")
# Spliting by word boundaries
word_bound_regex = re.compile(r"\W+")

# Repeating words like hurrrryyyyyy
rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE);
def rpt_repl(match):
	return match.group(1)+match.group(1)

# Emoticons
emoticons = [	('__EMOT_SMILEY',	[':-)', ':)', '(:', '(-:', ] )	,\
		('__EMOT_LAUGH',		[':-D', ':D', 'X-D', 'XD', 'xD', ] )	,\
		('__EMOT_LOVE',		['<3', ':\*', ] )	,\
		('__EMOT_WINK',		[';-)', ';)', ';-D', ';D', '(;', '(-;', ] )	,\
		('__EMOT_FROWN',		[':-(', ':(', '(:', '(-:', ] )	,\
		('__EMOT_CRY',		[':,(', ':\'(', ':"(', ':(('] )	,\
	]

# Punctuations
punctuations = [ \
		('__PUNC_EXCL',		['!',  ] )	,\
		('__PUNC_QUES',		['?' ] )	,\
		('__PUNC_ELLP',		['...', '....', ] )	,\
	]

def rpt_repl(match):
	return match.group(1)+match.group(1)

#For emoticon regexes
def escape_paren(arr):
	return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

def regex_union(arr):
	return '(' + '|'.join( arr ) + ')'


emoticons_regex = [ (repl, re.compile(regex_union(escape_paren(regx))) ) \
					for (repl, regx) in emoticons ]


#For punctuation replacement
def punctuations_repl(match):
	text = match.group(0)
	repl = []
	for (key, parr) in punctuations :
		for punc in parr :
			if punc in text:
				repl.append(key)
	if( len(repl)>0 ) :
		return ' '+' '.join(repl)+' '
	else :
		return ' '

def processAll( 		text, subject='', query=[]):

	if(len(query)>0):
		query_regex = "|".join([ re.escape(q) for q in query])
		text = re.sub( query_regex, '__QUER', text, flags=re.IGNORECASE )

	text = re.sub( hash_regex, hash_repl, text )
	text = re.sub( hndl_regex, hndl_repl, text )
	text = re.sub( url_regex, ' __URL ', text )
	text = re.sub(url_regex2, ' __URL ', text)
	#print text
	for (repl, regx) in emoticons_regex :
		text = re.sub(regx, ' '+repl+' ', text)


	text = text.replace('\'','')
	text = re.sub( word_bound_regex , punctuations_repl, text )
	text = re.sub( rpt_regex, rpt_repl, text )
	sb_s = SnowballStemmer('english')
	w_lem = WordNetLemmatizer()
	stop = set(stopwords.words('english'))
	stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','__punc_excl','__punc_ques','__punc_ellp','__hndl','__url','__quer','tweet','tweeted:','follow','tweeted','RT'])
	b=[]
	for word in text.lower().split():
		if word not in stop:
			each_word = sb_s.stem(word)
			d=re.compile(r"u'")
			temp = re.sub(d,'',each_word)
			b.append(temp)
	#b = [sb_s.stem(word) for word in text.lower().split() if word not in stop]
	text = ' '.join(b)
	#print "yes", text
	return text

#print __name__,"name"
def main():
    text = "@srb This   is   gr8'''.... !!"
    print (processAll(text))
	#snowball_stemmer.stem('presumably')
	
	#wordnet_lemmatizer.lemmatize('dogs')

if __name__ == '__main__':
    main()