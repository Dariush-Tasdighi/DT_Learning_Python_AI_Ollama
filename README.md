# Working with Ollama

## Packages

- 'rich' package:
  - [pypi.org](https://pypi.org/project/rich)
  - [github.com](https://github.com/Textualize/rich)
  - Extra
    - [Site](https://rich.readthedocs.io/en/latest)

- 'ollama' package:
  - [pypi.org](https://pypi.org/project/ollama)
  - [github.com](https://github.com/ollama/ollama-python)
  - Extra
    - [Site](https://ollama.com)

- 'googletrans' package:
  - [pypi.org](https://pypi.org/project/googletrans)
  - [github.com](https://github.com/ssut/py-googletrans)

- 'dotenv-python' package:
  - [pypi.org](https://pypi.org/project/dotenv-python)
  - [github.com](https://github.com/TsuiJie/dotenv-python)

- 'deep-translator' package:
  - [pypi.org](https://pypi.org/project/deep-translator)
  - [github.com](https://github.com/nidhaloff/deep-translator)

## References

- Package: 'googletrans'
  - دارد Conflict این کتابخانه خیلی مشهور است، ولی متاسفانه

- Package: 'deep-translator'
  - <https://deep-translator.readthedocs.io/en/latest>

## Setup Environment

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```

```bash
python -m pip install -r .\requirements.txt -U
```

```bash
python -m pip list
```

```bash
python -m pip install -U pip
```

```bash
python -m pip install -U rich
```

```bash
python -m pip install -U ollama
```

```bash
python -m pip install -U python-dotenv
```

```bash
python -m pip install -U deep-translator
```

```bash
python -m pip list
```

Now! We Create / Modify / Delete / Run the Source Codes...

```bash
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
