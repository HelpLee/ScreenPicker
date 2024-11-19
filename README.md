# **ScreenPicker**

ScreenPicker is a GUI tool that allows you to capture the screen's mouse position and color in real-time. It displays the position in coordinates and the color in both RGB and hexadecimal formats.

---

## **Features**
- Real-time capture of the mouse's current position on the screen.
- Displays the color of the current position in RGB and hexadecimal formats.
- Simple and user-friendly graphical interface.

---

## **Project Requirements**
Before running or packaging the project, ensure the following Python libraries are installed:

1. **Dependencies**:
   - pyautogui
   - keyboard
   - tkinter (included in Python standard library)
   - Pillow (image processing library)

2. **Installation**:
   Run the following command to install the required libraries:
   
bash
   pip install pyautogui keyboard pillow


---

## **How to Run the Script**

### **Run in Development Mode**
1. Ensure you have Python and the required libraries installed.
2. Run the following command to start the program:
   
bash
   python xy-rgb.py


---

## **How to Package the Program**

To create an executable file (.exe), use the following command:

bash
pyinstaller --onefile --noconsole --icon=rgb.ico --exclude-module tkinter --exclude-module unittest --exclude-module distutils --exclude-module setuptools._vendor.jaraco.text --exclude-module setuptools._vendor.jaraco.functools --hidden-import=jaraco.text xy-rgb.py


---

## **Usage**
- Launch the application (via Python or .exe).
- Place your mouse at the desired position on the screen.
- Press Ctrl + Alt to capture the current mouse position and color.
- The application will display the position and color in the GUI.
