# # 모폴로지 연산
# # 형태소(Structing element)의 크기와 형태를 지정
# # 크기 : 3x3 5x5 7x7 9x9
# # 형태 : 십자가모양(cv2.MORPH_CROSS), 직사각형(cv2.MORPH_RECT), 타원(cv2.MORPH_ELLIPSE)
#
# # kernel = cv2.getStucturingElement( 형태, 형태소크기(9,9))
#
# # Erosion 코드
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
# img_gray = cv2.bitwise_not(img_gray)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
# img_erode = cv2.erode(img_gray, kernel, iterations=3)
#
# img_dst = cv2.hconcat([img_gray,img_erode])
# cv2.imshow('dst',img_dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# #Dilation 코드
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
# img_gray = cv2.bitwise_not(img_gray)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
#
# img_dilate = cv2.dilate(img_gray, kernel, iterations=3)
# img_dst = cv2.hconcat([img_gray,img_dilate])
#
# cv2.imshow('dst',img_dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # OPENING : erode후 dilate진행
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
# img_gray = cv2.bitwise_not(img_gray)
#
# img_morp = img_gray.copy()
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
#
# # OPENING 5번은 erode 5번 진행후 dilate 5번 진행하는것과 같다.
# img_morp1 = cv2.morphologyEx(img_morp, cv2.MORPH_OPEN,
#                 kernel, iterations=5)
#
# img_morp2 = cv2.erode(img_morp, kernel, iterations=5)
# img_morp2 = cv2.dilate(img_morp2, kernel, iterations=5)
#
# img_dst = cv2.hconcat([img_morp1,img_morp2])
#
# cv2.imshow('dst',img_dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
#
# # CLOSING : dilate 후 erode 진행
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
# img_gray = cv2.bitwise_not(img_gray)
#
# img_morp = img_gray.copy()
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
#
# # CLOSING 5번은 dilate5번 진행후 erode5번 진행하는것과 같다.
# img_morp1 = cv2.morphologyEx(img_morp, cv2.MORPH_CLOSE,
#                 kernel, iterations=5)
# img_morp2 = cv2.dilate(img_morp, kernel, iterations=5)
# img_morp2 = cv2.erode(img_morp2, kernel, iterations=5)
#
# img_dst = cv2.hconcat([img_morp1,img_morp2])
#
# cv2.imshow('dst',img_dst)
# cv2.waitKey(0)