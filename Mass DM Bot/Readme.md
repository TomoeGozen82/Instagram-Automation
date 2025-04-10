# 📬 Instagram Mass DM Bot (Followers Only)

This bot allows you to automatically send multiple messages to your own Instagram followers using Python and Selenium.

It logs in to your Instagram account, reads a list of usernames from a file named after your own username, and sends direct messages to the followers you specify. You can also define the number of times each message should be sent.

---

## ✅ Getting Started

### 1️⃣ Create a Text File with Your Username

- You must create a file with the **same name as the Instagram username you will log in with**.
- Inside that file:
  - First line: **Your own username**
  - Following lines: **Usernames of the followers** you want to send messages to

📌 Example: If your Instagram username is `Ravi.txt`, then create a file named:
```
Ravi.txt
```

And inside that file, add:
```
user1_follower
user2_follower
user3_follower
```

> The bot will use this file to know who to message.

---

### 2️⃣ Setup `config.ini` File

Create or edit the `config.ini` file to include the following information:

```ini
[login]
username = your_instagram_username
password = your_instagram_password

[message]
text = Hey! Just reaching out. Hope you're doing great!

[Number of Messages you wanna send]
count = 3
```

🧾 What each field means:
- `username`: Your Instagram login username
- `password`: Your Instagram login password
- `text`: The message you want to send
- `count`: How many times the message should be sent to each user

> ⚠️ Never share your config.ini file publicly. It contains sensitive login info.

---

### 3️⃣ Install Requirements

Make sure Python is installed, then install Selenium:

```bash
pip install selenium
```

Also download the correct **ChromeDriver** based on your Chrome browser version:  
👉 https://chromedriver.chromium.org/downloads  
Place it in the same folder as your script or in your system path.

---

### 4️⃣ Run the Bot

```bash
python main.py
```

The bot will:
- Open Chrome
- Log in to your Instagram account
- Read usernames from your username file
- Send your message to each user in that list the number of times specified in `config.ini`

---

## 🔒 Important Rules

- ❗ This bot works **only with your own followers**.
- ❗ If you try to message random or non-following accounts, **Instagram may block, ban, or flag your account**.
- ✅ Only use this for personal outreach, engagement, or test purposes.

---

## ⚠️ Disclaimer

This project is built strictly for **educational purposes only**.

Please **do not misuse** this script to spam or violate Instagram's [Terms of Service](https://help.instagram.com/581066165581870).

By using this tool, you agree that:
- You are responsible for your own actions
- You understand the risks of account bans or restrictions
- **I, Junaid Mansoori, take no responsibility for any misuse, damage, or consequences caused by the use of this script**

---
