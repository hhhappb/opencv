import cv2
import numpy as np

# 指定颜色的范围
color_lower = np.array([0, 100, 100])
color_upper = np.array([10, 255, 255])

# 获取摄像头输入
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, frame = cap.read()

    # 转换为HSV颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 根据颜色范围创建掩码
    mask = cv2.inRange(hsv, color_lower, color_upper)

    # 对掩码进行形态学操作，去除噪声
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 寻找最大轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        # 找到最大轮廓的外接矩形框
        x, y, w, h = cv2.boundingRect(max_contour)

        # 在图像上画出矩形框和中心点
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        # 在窗口上显示中心点坐标
        cv2.putText(frame, f"({center_x}, {center_y})", (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # 在窗口上显示图像
    cv2.imshow("Color Block Detection", frame)

    # 按下q键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源和关闭窗口
cap.release()
cv2.destroyAllWindows()
