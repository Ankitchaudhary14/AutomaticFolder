import os
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")


files = os.listdir()
files.remove("AutomaticFileCleaner.py")

createIfNotExists("Images")
createIfNotExists("Docs")
createIfNotExists("Media")
createIfNotExists("Others")

imgExts = [".png",".jpg",".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt",".pdf","doc","docx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4",".mp3",".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in mediaExts) and (ext not in mediaExts) and os.path.isfile(file):
        others.append(file)
move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)


