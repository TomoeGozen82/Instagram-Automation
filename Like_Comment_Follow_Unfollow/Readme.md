# 🤖 Instagram Automation Toolkit (Like, Comment, Follow, Unfollow)

This toolkit includes multiple Python + Selenium-based automation scripts to perform **likes, comments, follows, and unfollows** on Instagram accounts using your own credentials.

It is built for users who want to engage with their audience or test automation features on their own accounts.

---


## 🔧 Configuration: `config.ini`

You need to create or update a file named `config.ini` with your login and settings:

```ini
[login]
username = your_instagram_username
password = your_instagram_password

[settings]
delay_between_actions = 2  ; time in seconds
max_actions_per_session = 50

[Message]
messages = Nice post!,Awesome content!,🔥🔥🔥
```

📝 Explanation:
- `username` & `password`: Your Instagram login info
- `delay_between_actions`: Pause between each like/follow/comment to look natural
- `max_actions_per_session`: Total actions per script run
- `messages`: Messages to use when commenting (comma-separated)
- `tags`: Hashtags to use in like/follow/comment scripts

---

## ⚙️ Installation

Install Python dependencies using:

```bash
pip install -r requirements.txt
```

Sample `requirements.txt`:

```
selenium
configparser
```

Also, download the **correct ChromeDriver** version from:  
👉 https://chromedriver.chromium.org/downloads  
Put it in the same folder as the script or add it to your system PATH.

---

## 🚀 How to Run

### Comment , Like and Follow on posts:
```bash
python like_cmt_follow.py
```

### Follow users:
```bash
python follow_bot.py
```

### Unfollow users:
```bash
python unfollow_bot.py
```

Each script will:
- Log in to your account
- Perform the action using the info in `config.ini`
- Respect delays and action limits to reduce risk

---

## ⚠️ Important Rules

- ❗ Only use this on **your own account** for testing or engagement.
- ❗ Avoid excessive use. Instagram has strict rate limits and automation detection.
- ✅ Keep your `delay_between_actions` reasonable (e.g., 2–5 seconds).
- ✅ Use realistic messages and hashtags to avoid being flagged.

---

## 📌 Disclaimer

> This project is made for **educational purposes only**.  
> Please **do not misuse** these scripts to spam, violate Instagram’s [Terms of Service](https://help.instagram.com/581066165581870), or perform unauthorized actions.  
> By using this tool, you agree that:
> - You take full responsibility for your actions
> - You understand the risk of your account being flagged, banned, or rate-limited
> - **I, Junaid Mansoori, am not liable** for any consequences caused by the use of this automation toolkit

