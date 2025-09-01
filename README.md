#  Virtual Mouse with Hand Gestures
[![Python](https://img.shields.io/badge/python-3.10%20--%203.13-blue)](https://www.python.org/)  
[![OpenCV](https://img.shields.io/badge/OpenCV-4.12+-green?logo=opencv)](https://opencv.org/)  
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-blueviolet)](https://mediapipe.dev/)  
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.54-orange)](https://pyautogui.readthedocs.io/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

> Control your computer **without touching a mouse** – simply move your hand in front of your webcam!  
> This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to convert **hand gestures into real-time mouse actions**.

---

##  Demo Video

<p align="center">
  <!-- Replace with your own GIF or video link -->
  <a href="https://github.com/user-attachments/assets/632f9a83-8303-40d2-9c3f-5b905e190be8" target="_blank">
    <img src="https://img.shields.io/badge/▶-Watch%20Demo-blue?style=for-the-badge&logo=screenrec" alt="Demo"/>
  </a>
</p>

<p align="center">
  <b><i> Experience real-time hand gesture control – interact with your computer <u>without touching a mouse</u>! </i></b>
</p>



---

##  Features

- **Cursor Movement** → Move the pointer using your **index finger**.  
- **Left Click** → Tap gesture: **Index + Middle fingers**.  
- **Right Click** → Tap gesture: **Index + Middle + Ring fingers**.  
- **Scrolling** →  
  -  **Fist** → Scroll Down  
  -  **Open Palm** → Scroll Up  
- **Real-time performance** with optimized gesture recognition.  
- Works with **standard webcams** (no extra hardware needed).  
- Easy to extend with **custom gestures**.  

---

##  Tech Stack

- **Python 3.10+** (recommended for best MediaPipe performance)  
- [OpenCV](https://opencv.org/) → Video capture & frame processing  
- [MediaPipe](https://mediapipe.dev/) → Hand landmark detection  
- [PyAutoGUI](https://pyautogui.readthedocs.io/) → Mouse movement, clicks, and scroll automation  

---

##  Project Structure

```bash
virtual-mouse/
│── virtual_mouse.py       # Main script (run this to start the app)
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
└── assets/                # Optional: GIFs, videos, screenshots
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

---
<table>
  <thead>
    <tr>
      <th>Gesture</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color:#f2f2f2;">
      <td>Index Finger</td>
      <td>Move Cursor</td>
    </tr>
    <tr>
      <td>Index + Middle Fingers</td>
      <td>Left Click</td>
    </tr>
    <tr style="background-color:#f2f2f2;">
      <td>Index + Middle + Ring</td>
      <td>Right Click</td>
    </tr>
    <tr>
      <td>Fist</td>
      <td>Scroll Down</td>
    </tr>
    <tr style="background-color:#f2f2f2;">
      <td>Open Palm</td>
      <td>Scroll Up</td>
    </tr>
  </tbody>
</table>

---
##  Future Enhancements

- **Dual-hand support** – Enable recognition of both hands simultaneously.
- **On-screen overlay** – Show detected gestures in real time.
- **Extended controls** – Volume, brightness, and application switching.
- **AI gesture customization** – Personalize gestures per user for accessibility.

---


## Contributing

Want to improve this project? Contributions are welcome!

- Fork the repo
- Create your feature branch → ```git checkout -b feature/my-feature```
- Commit changes → ```git commit -m "Add my feature"```
- Push branch → ```git push origin feature/my-feature```
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
