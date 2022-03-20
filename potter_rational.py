import os
_path= r"C:\Users\noase\Downloads\potter_chapters"
chapter_lists = os.listdir(r"C:\Users\noase\Downloads\potter_chapters")
forbidden_characters = '"*/:<>?\|'
unicode_characters = '”⁎∕꞉‹›︖＼⏐'
for old_chapter in chapter_lists:
    potter_chapter =open(os.path.join(_path, old_chapter),"r")
    chapter =""
    for i in range(7):
        if i==6:
            i = potter_chapter.readline()
            lst = i.split("Chapter ")
            lst1 = lst[1].split(":", 1)
            chapter = lst1[0].zfill(3)
            title = lst1[1][:-9]
            final_title = chapter + title + ".html"
            for a, b in zip(forbidden_characters, unicode_characters):
                final_title = final_title.replace(a, b)
            print(chapter + title)
        potter_chapter.readline()
    potter_chapter.close()
    os.rename(os.path.join(_path, old_chapter), os.path.join(_path, final_title))

