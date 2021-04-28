import cv2 as cv

if __name__ == '__main__':
    img = cv.imread('11.png',0)
    cv.imshow('image',img)
    k = cv.waitKey(0)
    if k == 27: # 等待ESC退出
        cv.destroyAllWindows()
    elif k == ord('s'): # 等待关键字，保存和退出
        cv.imwrite('11.png',img)
        cv.destroyAllWindows()