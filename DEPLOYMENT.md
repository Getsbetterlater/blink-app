# Deploying Blink to the Web

This guide will help you deploy Blink so it's accessible from anywhere on the internet.

## Option 1: Railway (Recommended - Easiest)

Railway is a modern deployment platform with a free tier. Your code is already configured for Railway.

### Step 1: Create a Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up with your GitHub account (free)

### Step 2: Deploy Your App

**Via GitHub (Recommended):**

1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push
   ```

2. In Railway dashboard:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `blink-app` repository
   - Railway will auto-detect it's a Python app

**Via Railway CLI:**

1. Install Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```

2. Login and deploy:
   ```bash
   railway login
   railway init
   railway up
   ```

### Step 3: Add PostgreSQL Database

1. In your Railway project dashboard:
   - Click "New" → "Database" → "Add PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

### Step 4: Add Anthropic API Key

1. In Railway project dashboard:
   - Go to "Variables" tab
   - Click "New Variable"
   - Add: `ANTHROPIC_API_KEY` = `your-api-key-here`

### Step 5: Deploy!

- Railway will automatically deploy your app
- You'll get a URL like: `https://blink-app-production.up.railway.app`
- Visit that URL to use your app!

---

## Option 2: Render

Render offers a free tier with persistent storage.

### Steps:

1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add PostgreSQL database:
   - Click "New +" → "PostgreSQL"
   - Copy the "Internal Database URL"
6. Add environment variables:
   - `DATABASE_URL` = (your postgres URL)
   - `ANTHROPIC_API_KEY` = (your API key)
7. Click "Create Web Service"

---

## Option 3: Fly.io

Fly.io is great for apps that need global distribution.

### Steps:

1. Install Fly CLI:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. Login and launch:
   ```bash
   fly auth login
   fly launch
   ```

3. Add PostgreSQL:
   ```bash
   fly postgres create
   fly postgres attach <postgres-app-name>
   ```

4. Set API key:
   ```bash
   fly secrets set ANTHROPIC_API_KEY=your-api-key-here
   ```

5. Deploy:
   ```bash
   fly deploy
   ```

---

## Option 4: Heroku

Classic option, requires credit card for free tier.

### Steps:

1. Install Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. Login and create app:
   ```bash
   heroku login
   heroku create blink-app-yourname
   ```

3. Add PostgreSQL:
   ```bash
   heroku addons:create heroku-postgresql:essential-0
   ```

4. Set API key:
   ```bash
   heroku config:set ANTHROPIC_API_KEY=your-api-key-here
   ```

5. Deploy:
   ```bash
   git push heroku main
   ```

---

## Verifying Deployment

After deployment, your app will be accessible at a public URL like:
- Railway: `https://your-app.up.railway.app`
- Render: `https://your-app.onrender.com`
- Fly.io: `https://your-app.fly.dev`
- Heroku: `https://your-app.herokuapp.com`

Visit the URL in any browser to use Blink from anywhere!

## Troubleshooting

### App won't start
- Check that `DATABASE_URL` and `ANTHROPIC_API_KEY` environment variables are set
- Check deployment logs for errors

### Database connection errors
- Ensure the database URL format is correct
- Railway/Render handle this automatically

### API key errors
- Verify your Anthropic API key is valid
- Check it's set in environment variables, not hardcoded

## Cost

All mentioned platforms have free tiers:
- **Railway**: Free tier includes $5/month credit
- **Render**: Free tier (apps sleep after inactivity)
- **Fly.io**: Free tier includes 3 shared VMs
- **Heroku**: Free tier (requires credit card)

For production use, expect $5-20/month depending on usage.
