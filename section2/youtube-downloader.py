import pytube

down_url1 = str(input("다운받을 주소 입력 :"))
yt = pytube.YouTube(down_url1)
videos = yt.streams.all()

#print('video',videos)

for i in range(len(videos)) :
   print(i, ' , ', videos[i])

cNum = int(input("영상의 화질을 선택해주세요(0~21 선택)"))

down_dir = "/Users/jeongho/Documents/youtube"

videos[cNum].download(down_dir)

#
# newFileName = input("변환 할 mp3 파일명은?")
# oriFileName = videos[cNum].default_filename
#
#
# print("동영상 다운로드 및 mp3 변환완료!!")
