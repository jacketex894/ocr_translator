# ocr_translator
## 簡介
![程式畫面](https://i.imgur.com/5A9o4xW.jpeg)

這是一個翻譯程式，使用者可以通過應用程式選取畫面上的指定範圍，利用 OCR 技術識別範圍內的日文文字，並透過本地部署的 LLM 進行翻譯。

目前此程式只適合在 windows 上執行。

## 操作流程
1. 按下 Start OCR 按鈕後，可以按畫面上任意位置拉取擷取範圍，應用程式便會開始顯示辨認文字。
2. 按下 Start translate ，會開始載入 LLM 並開始翻譯。
    - 如果 local 沒有指定 LLM ，會跳出一個 CMD 視窗開始自動下載模型。

## Reference
* 目前使用LLM : [sakura model](https://huggingface.co/SakuraLLM/Sakura-1.5B-Qwen2.5-v1.0-GGUF)
* https://github.com/PiDanShouRouZhouXD/Sakura_Launcher_GUI
* https://github.com/SakuraLLM/SakuraLLM

## Need
本專案需要事先安裝 Tesseract。

### windows 安裝方法
請至 [Tesseract](https://github.com/tesseract-ocr/tesseract)下載安裝程式，本專案目前使用 5.5.0版本。
請在安裝時的 Additional language data(download) 選擇 japanese 跟 japanese(vertical)。
## Run

本專案目前使用 poetry 作為環境管理工具，所以請照以下指令輸入建立環境。
1. poetry lock
2. poetry install
3. poetry shell 即可啟用本專案環境
4. python -m app.main 可以執行本專案
## TODO
- ✅ OCR
- ✅ ScreenCapture
- ✅ OCR with ScreenCapture
- ✅ Connect to LLM for translation.
- ✅ GUI
- ⬜ Refactoring UI
- ⬜ Refactoring LLM relate code
- ⬜ Packaged into an executable file
- ⬜ api