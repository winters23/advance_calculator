message=input(">")
words=message.split(' ')
emojis={
      ":)": "\U0001F642",

      ":D": "\U0001F603",
      ";)": "\U0001F609",
":(": "\U0001F612",
   }
output=""
for word in words:
    output+= emojis.get(word,word)+ " "
print(output)