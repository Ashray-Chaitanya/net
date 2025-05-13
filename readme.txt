Here's a **step-by-step guide for Windows** to set up and run your Python script using the packages you listed:

---

## ✅ Step 1: Install Python

1. Go to: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Download the latest Python version (e.g., Python 3.11+).
3. **During installation**, make sure to:

   * ✅ Check "Add Python to PATH"
   * ✅ Choose “Customize installation” if you want to select installation location
4. Finish installation.

---

## ✅ Step 2: Set Up a Virtual Environment (Recommended)

1. Open **Command Prompt** or **PowerShell**.
2. Navigate to your project directory:

   ```bash
   cd path\to\your\project
   ```
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
4. Activate it:

   ```bash
   venv\Scripts\activate
   ```

---

## ✅ Step 3: Create `requirements.txt`

In the same folder as your script (`main.py`), create a file called `requirements.txt` with the following content:

```
requests
numpy
opencv-python-headless
pytesseract
Pillow
selenium
beautifulsoup4
pymongo
```

---

## ✅ Step 4: Install Python Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

## ✅ Step 5: Install Tesseract OCR

`pytesseract` requires **Tesseract-OCR** to be installed separately:

1. Download the Windows installer from here:
   👉 [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)

   Or direct link (as of 2024):
   👉 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

2. Install it (default path is usually `C:\Program Files\Tesseract-OCR`).

3. Add Tesseract to your **System PATH**:

   * Open Start → search for "Environment Variables"
   * Under "System Variables", find `Path`, click "Edit"
   * Add:

     ```
     C:\Program Files\Tesseract-OCR
     ```

4. Restart your terminal or IDE.

5. (Optional) In your Python script, explicitly set the path:

   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

---

## ✅ Step 6: Install ChromeDriver (for Selenium)

1. Check your Chrome version:

   * Open Chrome → Go to `chrome://settings/help`

2. Download **matching ChromeDriver**:
   👉 [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

3. Extract it somewhere (e.g., `C:\tools\chromedriver.exe`)

4. Either:

   * Add the folder to your **PATH**, **OR**
   * In your script, specify the driver path:

     ```python
     driver = webdriver.Chrome(executable_path="C:\\tools\\chromedriver.exe")
     ```

---

## ✅ Step 7: Run Your Script

If your script is named `main.py`, run:

```bash
python extraction.py
```

If you're using the virtual environment, make sure it's activated (`venv\Scripts\activate`) before running the script.

---

Would you like a template `main.py` that integrates all these pieces (Tesseract, Selenium, MongoDB, etc.) to test if everything is installed correctly?
