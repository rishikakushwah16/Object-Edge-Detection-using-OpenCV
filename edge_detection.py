import cv2  #importing Packages
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk


def choose_image():  #  Defining Choose_image
    #  catch a reference to the image panels
    global panelA, panelB
    # open a file choosing dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # upload the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)


        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            # while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)

        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged


# making the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=choose_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()
