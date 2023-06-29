import cv2
import numpy as np


def find_circles(image_path):
    # 读取图像
    image = cv2.imread('5.png')
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 高斯模糊处理
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用霍夫圆变换检测圆
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        # 将圆心坐标取整并转换为整数
        circles = np.round(circles[0, :]).astype("int")

        # 遍历检测到的圆
        for (x, y, r) in circles:
            # 绘制圆和圆心
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

            # 输出圆心坐标
            print("圆心坐标：", (x, y))

        # 显示绘制圆后的图像
        cv2.imshow("Circles", image)
        cv2.waitKey(0)
    else:
        print("未找到圆")

    cv2.destroyAllWindows()


# 调用函数并传入图像路径
find_circles("5.png")
