# Python Playground

## Prepare

1. python3.8+

## How to use

1. `pip install -r requirements.txt`
2. `python script.py`

## Scenarios

各類情境主要使用的函式庫

- 網路爬蟲 [bs4](https://pypi.org/project/beautifulsoup4/), [selenium](https://pypi.org/project/selenium/), [requests](https://pypi.org/project/requests/)
- 資料處理 [matplotlib](https://pypi.org/project/matplotlib/), [pandas](https://pypi.org/project/pandas/), [numpy](https://pypi.org/project/numpy/)
- 機器學習 [numpy](https://pypi.org/project/numpy/), [scipy](https://pypi.org/project/scipy/)
- 深度學習 [tensorflow](https://pypi.org/project/tensorflow/), [keras](https://pypi.org/project/keras/), [torch](https://pypi.org/project/torch/)
- 自動化測試 [playwright](https://pypi.org/project/playwright/), [selenium](https://pypi.org/project/selenium/), [xlrd](https://pypi.org/project/xlrd2/), [pandas](https://pypi.org/project/pandas/)

## 套件管理

開發過程中會使用到許多套件，為了方便管理，可以使用 `pip` 或 `conda` 來安裝、移除、更新套件。

產生 `requirements.txt` 檔案，並將指定套件寫入檔案中：

```bash
# pip
pip freeze > requirements.txt
pip3 freeze > requirements.txt

# conda
conda list -e > requirements.txt
```

安裝 `requirements.txt` 中的套件：

```bash
pip install -r requirements.txt
```

移除當前環境中所有的套件：

```bash
# 將全域中所有套件寫入檔案中
pip freeze > python_modules.txt
# 解除安裝檔案中的套件
pip uninstall -r python_modules.txt -y
```
