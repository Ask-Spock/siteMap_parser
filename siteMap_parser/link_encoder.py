"""
This Program file targets are
-------------------------------
1.encoding hebrew text to Utf-8
2.Grab and replace the Hebrew text with the Utf-8

Grabing - very simple i will just take the first part out because its a const : http://ask-tal.co.il/
and enter the rest to a varible
on the varible that has the hebrew i will menupilate to utf-8
and the mearge everthing togather


"""


base_Url = "http://www.ask-tal.co.il/"

hebrew_URL = "http://ask-tal.co.il/קניית-דירה"

#target = txt.strip("http://ask-tal.co.il/")

tempHebUrl = hebrew_URL.replace('http://ask-tal.co.il/','')


#This is the Hebrew format
print(tempHebUrl)

#now i Need to change encode to UTF-8

#utf8_Url = tempHebUrl.encode('utf8')  # encoded to UTF-8
utf8_Url = tempHebUrl.encode()
print(utf8_Url)
print(type(utf8_Url))

bytesToString = str(utf8_Url)

print(bytesToString)

print(type(bytesToString))



#i should replace \ with %
bytesToString = bytesToString.replace('\\','%')
print(bytesToString)

#remove first 2 tabs b'   and '
bytesToString = bytesToString.replace("b'",'')
print(bytesToString)


#remove the '  at the end of the string
bytesToString = bytesToString.replace("'",'')
print(bytesToString)

#remove the 'x' char
bytesToString = bytesToString.replace("x",'')
print(bytesToString)

#capitalize the string

bytesToString = bytesToString.upper() 
print(bytesToString)




#now i need to join the unicode url to base website url it to a link

finalLink = base_Url + str(bytesToString)

print(finalLink)


#print the URL


#open the new url to verify its ok.


#go over all the Hebrew url and and encode them and store them in a new file


