# ocr_translator
## Need
本專案需要事先安裝 Tesseract。

### windows 安裝方法
請至 [Tesseract](https://github.com/tesseract-ocr/tesseract)下載安裝程式，本專案目前使用 5.5.0版本。
請在安裝時的 Additional language data(download) 選擇 japanese 跟 japanese(vertical)。
## Run

本專案目前使用 poetry 作為環境管理工具，所以請照以下指令輸入建立環境。
1. poetry lock
2. poetry install
3. poetry shell
即可啟用本專案環境
## TODO
- ✅ OCR
- ⬜ ScreenCapture
- ⬜ OCR with ScreenCapture
- ⬜ Connect to LLM for translation.
- ⬜ GUI
