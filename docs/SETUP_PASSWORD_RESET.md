# 🔐 Password Reset Feature Setup Guide

## Quick Fix for CORS & Database Error

You're seeing this error because the database needs to be updated with new columns for password reset functionality.

---

## 🚀 Quick Setup (Choose ONE method)

### Method 1: Update Existing Database (Recommended)

Run this command in your terminal:

```bash
python update_database.py
```

This will add the new columns to your existing database without losing data.

---

### Method 2: Use Migration Script

```bash
python migrate_password_reset.py
```

This adds the columns using ALTER TABLE commands.

---

### Method 3: Fresh Database (If you don't have important data)

```bash
# Delete the old database
rm instance/connect_link.db

# Create new database with updated schema
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

---

## ✅ Verify Setup

After running one of the methods above:

1. **Restart your Flask backend:**
   ```bash
   python run.py
   ```

2. **Test the forgot password feature:**
   - Go to http://localhost:5175/login
   - Click "Forgot password?"
   - Enter an email
   - Check the backend console for the reset link

---

## 📧 What Was Added

### Database Changes:
- `reset_token` - Stores the password reset token
- `reset_token_expiry` - Token expiration time (1 hour)

### New Routes:
- `POST /api/auth/forgot-password` - Request reset
- `POST /api/auth/reset-password` - Reset with token

### New Pages:
- `/forgot-password` - Request reset link
- `/reset-password?token=xxx` - Reset password

---

## 🔍 Troubleshooting

### Still seeing CORS error?
- Make sure Flask backend is running on port 5000
- Check that CORS is enabled in `app/__init__.py`

### Still seeing 500 error?
- Run the update script again
- Check backend console for detailed error
- Verify columns were added:
  ```bash
  sqlite3 instance/connect_link.db
  .schema user
  ```

### Can't find reset link?
- Check your backend console/terminal
- The link is printed there (until email is configured)
- Look for: "Password reset link for..."

---

## 📧 Email Configuration (Optional)

To send actual emails instead of console output:

1. Install Flask-Mail:
   ```bash
   pip install Flask-Mail
   ```

2. Configure in `app/config.py`:
   ```python
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = 'your-email@gmail.com'
   MAIL_PASSWORD = 'your-app-password'
   ```

3. Update `app/routes/auth.py` to send emails

---

## 🎉 You're All Set!

After running the update script, your password reset feature will work perfectly!

**Test it now:**
1. Go to login page
2. Click "Forgot password?"
3. Enter your email
4. Check console for reset link
5. Use the link to reset password
6. Login with new password

---

**Need help? Check the backend console for detailed error messages!**
