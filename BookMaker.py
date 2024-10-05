# Created by Imgur user PetSven
# 8/30/24

# Imports
# from PIL import ImageFont, ImageDraw, Image
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Load in the TrueType font
# font = ImageFont.truetype(font='TengwarAnnatar-RpaW.ttf', size=44)

# Create an image with a white background
# Letter is 612 by 792 at 72 pixels per inch
border = 2
ppi = 216  # 108
textW = int((8.5 - border) * ppi)
textH = int((11 - border) * ppi)
pageW = int(8.5 * ppi)
pageH = int(11 * ppi)

# canvas.Canvas : myCanvas


def startBook(title):
    global myCanvas
    myCanvas = canvas.Canvas(title+".pdf", pagesize=(pageW, pageH))
    # print(type(myCanvas))


def addTitlePage(title):

    # Set the default line width
    # myCanvas.setLineWidth(1)

    myCanvas.setFont('Helvetica', 70)
    myCanvas.drawCentredString(pageW/2, pageH*3/4, title[0])
    myCanvas.drawCentredString(pageW/2, (pageH*3/4)-80, title[1])

    myCanvas.setFont('Helvetica', 40)
    myCanvas.drawCentredString(pageW/2, (pageH/2), title[2])
    myCanvas.drawCentredString(pageW/2, (pageH/2)-50, title[3])
    myCanvas.drawCentredString(pageW/2, (pageH/2)-100, title[4])
    myCanvas.drawCentredString(pageW/2, (pageH/2)-150, title[5])
    myCanvas.showPage()


def addPage(page):

    # Load in the font
    pdfmetrics.registerFont(TTFont('TengwarAnnatar', 'TengwarAnnatar-RpaW.ttf'))
    myCanvas.setFont('TengwarAnnatar', 44)

    # I think it starts in the bottom left-hand corner
    textobject = myCanvas.beginText((ppi*border)/2, pageH-(ppi*border)/2)
    textobject.setLeading(70)
    textobject.textLines(page)
    myCanvas.drawText(textobject)

    # Save the page
    myCanvas.showPage()


def saveBook():
    myCanvas.save()
