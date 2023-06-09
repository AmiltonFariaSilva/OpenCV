import cv2

classificador = cv2.CascadeClassifier(
    'cascades\haarcascade_frontalface_default.xml')

#imagem = cv2.imread('pessoas\\beatles.jpg')
#imagem = cv2.imread('pessoas\\pessoas1.jpg')
imagem = cv2.imread('pessoas\\pessoas3.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.17, minNeighbors=11, minSize=(30,30))

# print(len(facesDetectadas)) #quantity of faces
# print(facesDetectadas) #position of faces

for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

cv2.imshow("Faces encontradas", imagem)

cv2.waitKey()
