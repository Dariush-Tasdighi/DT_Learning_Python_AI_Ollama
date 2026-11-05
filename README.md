# Learning 'ollama' Package

## This program was developed by

- **Dariush Tasdighi**
  - Mobile Number: +98 912 108 7461
  - Email Address: <DariushT@GMail.com>
  - Telegram ID: <https://t.me/Dariush_Tasdighi>
  - Virgool: <https://virgool.io/@dariush-tasdighi>
  - Aparat: <https://www.aparat.com/IranianExperts>
  - LinkedIn: <https://www.linkedin.com/in/tasdighi>
  - Instagram: <https://www.instagram.com/dariushtasdighi>
  - Telegram Channels:
    - <https://t.me/IranianExperts>
    - <https://t.me/DT_PYTHON_LEARNING>

## Used Packages

### 'rich' package

- <https://pypi.org/project/rich>
- <https://github.com/Textualize/rich>
- **More:**
  - <https://rich.readthedocs.io/en/latest>

### 'ollama' package

- <https://pypi.org/project/ollama>
- <https://github.com/ollama/ollama-python>
- **More:**
  - <https://ollama.com>

### 'googletrans' package

- <https://pypi.org/project/googletrans>
- <https://github.com/ssut/py-googletrans>

### 'dotenv-python' package

- <https://pypi.org/project/dotenv-python>
- <https://github.com/TsuiJie/dotenv-python>

### 'deep-translator' package

- <https://pypi.org/project/deep-translator>
- <https://github.com/nidhaloff/deep-translator>

## References

- Package: 'googletrans'
  - دارد Conflict این کتابخانه خیلی مشهور است، ولی متاسفانه

- Package: 'deep-translator'
  - <https://deep-translator.readthedocs.io/en/latest>

## Setup Environment

```bash
# python -m venv .venv
# .\.venv\Scripts\activate

# python -m pip list
# python -m pip install -r .\requirements.txt -U
# python -m pip list

# deactivate
```

```bash
# py install 3.13 -u

# py -3.13 -m venv .venv.3.13
# .\.venv.3.13\Scripts\activate

# py -m pip list
# py -m pip install -r .\requirements.3.13.txt -U
# py -m pip list

# deactivate
```

```bash
# py install 3.14 -u

# py -3.14 -m venv .venv.3.14
# .\.venv.3.14\Scripts\activate

# py -m pip list
# py -m pip install -r .\requirements.3.14.txt -U
# py -m pip list

# deactivate
```

```bash
py install 3.15 -u

py -3.15 -m venv .venv.3.15
.\.venv.3.15\Scripts\activate

py -m pip list
py -m pip install -r .\requirements.3.15.txt -U
py -m pip list

deactivate
```

## Notes

- نکته بسیار مهم! برای بر طرف کردن تداخل کتابخانه‌ها
- به طور هم‌زمان، نسبت به نصب کتابخانه‌ها، اقدام می‌کنیم
  - python -m pip install -U ollama deep-translator

## Download & Install CUDA Toolkit (If you have a Nvidia GPU)

- In Windows PowerShell:
  - check the Nvidia (CUDA) version and VRAM, with below command:
    - nvidia-smi.exe

- Compare:
  - <https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html>
  - <https://www.nvidia.com/en-us/geforce/graphics-cards/compare>
  - <https://benchmarks.ul.com/compare/best-gpus>
  - <https://benchmarks.ul.com/hardware/gpu/NVIDIA%20GeForce%20GTX%201650%20Ti%20(Notebook)>

- [nvidia.com](https://developer.nvidia.com/cuda-downloads)
  - Operating System: Windows
  - Architecture: x86_64
  - Version: 11
  - Installer Type: exe (local)
    - Download (3.0 GB)
      - cuda_12.6.2_560.94_windows.exe
      - [nvidia.com](https://developer.download.nvidia.com/compute/cuda/12.6.2/local_installers/cuda_12.6.2_560.94_windows.exe)
- [OR]
- winget install "Nvidia.CUDA"

- You should set the path for 'nvcc.exe' file:
  - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\bin
    - nvcc --version

### Go to HaggingFace site and create a Access Token

- [https://huggingface.co](https://huggingface.co)

- First Register and Login
- Select your model and 'Accept the License Agreement'

- Click on Left Top Circle!
- Click on 'Settings' menu item
- Click on 'Access Tokens' anchor
- Click on 'Create new Access Token' button
- Set 'Token name'
- Set 'Read access to contents of all public gated repos you can access' checkbox
- Click on 'Copy' button

- In PowerShell:
- pip install huggingface-hub
- huggingface-cli login
- Ask for 'Access Token': Right+Click -> For Pasting

## Learning Order

- learn.py
- app.py
  - dt_ollama.py
  - dt_llm_utility.py
- display_all_downloaded_models.py
- update_all_downloaded_models.py
- dictionary.py
  - dictionary_constants.py
- translator.py
  - translator_constants.py
- generate_code.py
  - generate_code_constants.py
- learning_json.py

---
