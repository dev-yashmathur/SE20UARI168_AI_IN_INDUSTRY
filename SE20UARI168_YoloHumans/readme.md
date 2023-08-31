The file to be executed is SE20UARI168_YoloPerson.ipynb

This file is configured to run on google collab.
to run it locally,
-> comment line 4 and 24 in the last cell.
append the following lines to the end:
    cv2.imshow("Yolo detected", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

