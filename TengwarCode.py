# Created by Imgur user PetSven
# 7/25/24

# My imports
import TengwarConverter
import BookMaker


# Open the text file
bookName = 'Around the World in Eighty Days'
file = open(bookName + '.txt', 'r', encoding='utf-8')
lines = file.readlines()

# Manually enter the title
title = [lines[0][0:-1],
         lines[2][0:-1],
         "Transliterated into the Elvish script, Tengwar, by Imgur user PetSven",
         "Using the Annatar Tengwar font created by Johan Winge (© 2004 – 2005)",
         "Based on the Tengwar script created by J.R.R. Tolkien for the Lord of the Rings",
         "This file was created on 10/4/24"]


# Create a string
numberOfLines = len(lines)
print("Total Lines: " + str(numberOfLines))

# Start the book file
BookMaker.startBook(bookName)

# Add a title page
BookMaker.addTitlePage(title)

# Transliterate the rest of the book
linesPerPage = 28
i = 0
for pageNumber in range(int(numberOfLines/linesPerPage)+1):
# for pageNumber in range(1):
    page = ""
    startLines = linesPerPage*pageNumber
    stopLines = (linesPerPage*pageNumber)+linesPerPage
    if stopLines > len(lines):
        stopLines = len(lines)
    # print(startLines)
    nextLines = lines[startLines:stopLines]
    # print(nextLines)
    for line in nextLines:
        result = TengwarConverter.convertToTengwar(line)
        page = page + result
        i = i + 1
        # print(i)
    # print(page)
    BookMaker.addPage(page)
BookMaker.saveBook()
