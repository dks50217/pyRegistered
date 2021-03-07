# pyRegistered
適用於某家醫院的自動掛號

# config
1. Add config.ini at root
2. Add below config 

```
[url]
router = 網頁網址
dept = 部門
dr = 代碼
drname = 醫生名稱
schap = 1
chgdr = 
lang = C
idno = 掛號者身分證字號
birth = 掛號者出生年月日 YYMMDD
day = 掛幾天後的號
[system]
autoclick = 1 //是否自動點擊
screenshot = 1 //是否截圖
sendmail = 1 //是否寄信
checkdriver = 1 // 是否檢查版本
[path]
driver = Webdriver路徑
[email]
from = 寄件者
to = 收件者
key = Gmail的應用權限Key
```

## 編譯
python -m PyInstaller main.spec


