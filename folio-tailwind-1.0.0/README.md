# Olatunde Portfolio

A personal portfolio website built with Flask, Tailwind CSS, and Alpine.js. The site includes a hero section, services, selected projects, about section, and a contact form that sends messages via email.

## Live Demo

- Local development: http://localhost:5000

## Tech Stack

- Python
- Flask
- Tailwind CSS
- Alpine.js
- SMTP email integration

## Getting Started

1. Clone the repository
   ```bash
   git clone <your-repository-url>
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install flask
   ```

4. Run the app
   ```bash
   python main.py
   ```

5. Open the app in your browser
   ```bash
   http://localhost:5000
   ```

## Environment Variables

Create a local `.env` file or set the variables in your terminal before running the app:

```bash
SENDER_EMAIL=tundexwealth@gmail.com
RECEIVER_EMAIL=tundexwealth@gmail.com
SENDER_PASSWORD=your-gmail-app-password
```

> For Gmail, use an app password instead of your normal account password.

## Contact Form

The contact form sends emails through Gmail SMTP and includes the sender's name, email, phone number, subject, and message.

## Credits and Template Attribution

This project uses a design template originally created by Laurent Begey and distributed via ThemeWagon.

- Original design and code: [Laurent Begey](https://lbegey78.gumroad.com/)
- Distribution: [ThemeWagon](https://themewagon.com/)
- This portfolio has been customized and adapted for personal use.

## License

The original template is copyright © Laurent Begey and is distributed through ThemeWagon. The design and code are subject to the applicable license terms for the template.

This project retains credit to the original creator and includes the template attribution above. If you are using or redistributing the original template, please preserve the creator credit and license terms.

---

This README is tailored for the current portfolio project while preserving proper credit to the template author.
