# Simplybot 🐍

A simple Python project with modular code structure.
The project demonstrates importing custom modules and making HTTP requests using the `requests` library.

---

## 📂 Project Structure

```
Simplybot/
├── main.py             # Entry point
├── modules/            # Custom modules
│   ├── calculation.py
│   ├── randf.py
│   └── __pycache__/    # Ignored (compiled files)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Simplybot.git
cd Simplybot
```

### 2. Create a virtual environment (recommended)

```bash
py -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
py main.py
```

---

## ⚙️ Requirements

* Python 3.13+
* Dependencies (from `requirements.txt`):

  * requests
  * urllib3
  * certifi
  * charset-normalizer
  * idna

---

## 📌 Notes

* The `modules/` folder contains your reusable functions.
* `__pycache__/` is ignored in `.gitignore`.
* If you add new libraries, update `requirements.txt` with:

  ```bash
  pip freeze > requirements.txt
  ```

---

## 🤝 Contributing

1. Fork the project
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a Pull Request

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
