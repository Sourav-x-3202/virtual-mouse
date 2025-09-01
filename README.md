# Virtual Mouse with Hand Gestures  

> Control your computer **without touching a mouse** – just by moving your hand in front of your webcam!  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to convert **hand gestures into real-time mouse actions**.  

---

##  Demo
<p align="center">
  <!-- Replace with your own GIF or video link -->
 <a href="https://github.com/user-attachments/assets/632f9a83-8303-40d2-9c3f-5b905e190be8">
    <img src="https://img.shields.io/badge/▶-Watch%20Demo-blue?style=for-the-badge&logo=screenrec" alt="Demo"/>
  </a>
</p>

---

##  Features
-  **Cursor Control** – Move the mouse pointer using just your index finger.  
-  **Left Click** – Tap gesture (Index + Middle fingers).  
-  **Right Click** – Extended (Index + Middle + Ring fingers).  
-  **Scrolling** –  
  -  Closed fist → Scroll Down  
  -  Open palm → Scroll Up  
- **Real-time performance** with optimized tracking.  
-  Works with standard webcams (no special hardware).  
- Easy to customize & extend with new gestures.  

---

##  Tech Stack
- **Python 3.10+** (recommended)  
- [OpenCV](https://opencv.org/) → Video frame processing  
- [MediaPipe](https://mediapipe.dev/) → Hand landmark detection  
- [PyAutoGUI](https://pyautogui.readthedocs.io/) → Mouse and scroll automation  

---

##  Project Structure
```bash
virtual-mouse/
│── virtual_mouse.py       # Main script (run this)
│── requirements.txt       # Dependencies
│── README.md              # Documentation
└── assets/                # (Optional) GIFs, videos, screenshots
```
---
## Installation Guide
###  Clone this repository
```bash
git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
```

###  (Optional but Recommended) Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```


###  Install Dependencies
```bash
pip install -r requirements.txt
```


###  Run the Program
```bash
python virtual_mouse.py
```
```
| Gesture                  | Action      |
| ------------------------ | ----------- |
| ☝️ Index Finger          | Move cursor |
| ✌️ Index + Middle        | Left click  |
| 🤟 Index + Middle + Ring | Right click |
| ✊ Fist                   | Scroll down |
| 🖐️ Open Palm            | Scroll up   |
```
---


##  Future Enhancements

- Dual-hand support (left & right hand).
- On-screen overlay showing recognized gestures.
- Extra controls (volume, brightness, app switching).
- AI-based gesture customization for different users.

---


## Contributing

Want to improve this project? Contributions are welcome!

- Fork the repo
- Create your feature branch → git checkout -b feature/my-feature
- Commit changes → git commit -m "Add my feature"
- Push branch → git push origin feature/my-feature
- Open a Pull Request

---
## Author

**Sourav Sharma**
Developer. Maker. Privacy-first AI enthusiast.
Find me on GitHub → [@Sourav-x-3202](https://github.com/Sourav-x-3202)

---


## Star This Project

If you found this useful, helpful, or inspiring — please consider starring the repository.
It helps others discover the project and keeps development going 

---
## License

This project is licensed under the MIT License.
© 2025 Sourav Sharma
