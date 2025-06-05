# 🎨 Turtle GUI Creative Drawing in Python

Welcome to **Turtle GUI Creative Drawing**, a fun and interactive project that uses Python's `turtle` module to generate mesmerizing shapes, vibrant spirographs, and dynamic random walks—all with a splash of randomness and color! 🐢

This project showcases three main drawing features, blending programming with creativity:

---

## ✨ What This Project Does

This project is a **creative drawing tool** built using Python's `turtle` graphics module. It creates:

- **Polygon Art** – Draws multiple polygons (triangles to decagons) in random colors.
- **Random Walks** – A colorful, bouncing line that explores the canvas in unpredictable patterns.
- **Spirographs** – Rotating circular patterns, drawn in every direction with dazzling colors.

The result? A beautiful fusion of mathematics, programming, and art.

---

## 🖼️ Visual Output

Below are sample outputs from this program:

### 🌀 Spirograph Example
<img width="321" alt="spirograph" src="https://github.com/user-attachments/assets/5522b75b-5df3-45dd-b1f0-335d0a80350c" />

### 🔷 Polygon Drawing
<img width="315" alt="polygons" src="https://github.com/user-attachments/assets/a4f551e5-80be-441a-9de0-53377fb14d34" />

### 🚶‍♂️ Random Walk in Color
<img width="221" alt="randomwalk" src="https://github.com/user-attachments/assets/a93d5e95-a28b-4c49-941f-8a80e9822c2d" />


---

## 🧠 How It Works

### 1. `random_walk()`
- The turtle randomly chooses a new direction (up, down, left, right).
- Each step is drawn in a new random color.
- If it hits a boundary, it "bounces" back in the opposite direction.
- Continues for 1,000 steps.

### 2. `draw_shape()`
- Draws polygons from triangle (3 sides) to hendecagon (11 sides).
- Each shape is rendered in a new random color.

### 3. `draw_spirograph()`
- Draws a series of 72 circles, each rotated by 5°.
- Results in a colorful, symmetric circular pattern.

---

## 🧰 Project Structure

```text
📁 turtle-grapich/
│
├── main.py                 # Main drawing logic
├── polygons.py             # turtle_direction array for directional logic
└── README.md               # This file
