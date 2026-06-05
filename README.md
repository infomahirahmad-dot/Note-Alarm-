# Note Alarm — Windows Desktop App

> pywebview দিয়ে তৈরি frameless Windows app
> URL: https://notealarm.lovable.app

---

## ফাইল তালিকা

| ফাইল | কাজ |
|------|-----|
| `app.py` | মূল Python app |
| `NoteAlarm.spec` | PyInstaller build config |
| `version_info.txt` | .exe এর metadata (নাম, ভার্সন) |
| `build.bat` | এক-ক্লিকে .exe বানানোর script |
| `icon.ico` | App icon (নিজে যোগ করুন, optional) |

---

## .EXE বানানোর ধাপ

### পদ্ধতি ১ — সহজ (build.bat)

1. এই folder টি আপনার PC-তে রাখুন
2. `build.bat` ফাইলে **double-click** করুন
3. কিছুক্ষণ অপেক্ষা করুন
4. `dist\NoteAlarm.exe` তৈরি হয়ে যাবে ✅

### পদ্ধতি ২ — Manual (Command Prompt)

```batch
:: প্রথমে এই folder এ যান
cd C:\path\to\NoteAlarm

:: Package install করুন
pip install pywebview pyinstaller

:: .exe বানান
pyinstaller NoteAlarm.spec --clean --noconfirm
```

### App সরাসরি run করতে (test)

```batch
pip install pywebview
python app.py
```

---

## App চালানো

- `dist\NoteAlarm.exe` — যেকোনো Windows PC-তে চলবে
- Internet connection প্রয়োজন (website load করার জন্য)
- App window drag করে move করা যাবে (frameless হওয়ায়)

---

## Icon যোগ করতে চাইলে

1. যেকোনো `.ico` ফাইল নিন (256×256 px ভালো)
2. নাম দিন `icon.ico`
3. এই folder এ রাখুন
4. আবার `build.bat` চালান

ICO converter: https://convertio.co/png-ico/

---

## সমস্যা হলে

| সমস্যা | সমাধান |
|--------|--------|
| `pip` command not found | Python PATH-এ add করুন |
| Build fail | `pip install pywebview --upgrade` চালান |
| App খুলছে না | `pythonnet` install করুন: `pip install pythonnet` |
| White screen | Internet connection চেক করুন |

---

## Requirements

- Windows 10 / 11
- Python 3.8 বা উপরে
- Internet connection
