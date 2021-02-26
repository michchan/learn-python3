import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    if image.startswith("resized_") == False:
        # 1 : color image
        # 0 : grayscale
        # -1 : color image with alpha channel (with transparency)
        img = cv2.imread(image, 0)

        print(img)
        print("Resolution: ", img.shape)
        print("Dimensions of the array: ", img.ndim)

        resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

        # Pass "Galaxy" as the window name
        cv2.imshow(image, resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(f"resized_{image}", resized_image)