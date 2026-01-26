# API Setup Guide

Spokenly needs an AI provider to process your dictation. Both options below have free tiers.

## Option 1: Groq (Recommended)

Groq offers fast inference with generous free limits.

### Get Your API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Click **API Keys** in the left sidebar
4. Click **Create API Key**
5. Copy the key (starts with `gsk_`)

### Add to Spokenly

1. Open **Spokenly > Settings > AI Prompt**
2. Find **API Key** field
3. Paste your Groq API key

### Recommended Models

| Setting | Model |
|---------|-------|
| **Text Model** | `qwen/qwen3-32b` or `llama-3.3-70b-versatile` |
| **Fallback** | `llama-3.1-8b-instant` |

### Free Tier Limits

| Model | Requests/min | Tokens/min |
|-------|--------------|------------|
| qwen/qwen3-32b | 60 | 6K |
| llama-3.3-70b-versatile | 30 | 12K |
| llama-3.1-8b-instant | 30 | 6K |

For heavy usage, Groq offers a [Developer plan](https://console.groq.com/settings/billing/plans) with higher limits.

---

## Option 2: Cerebras

Cerebras also offers free AI inference.

### Get Your API Key

1. Go to [cloud.cerebras.ai](https://cloud.cerebras.ai)
2. Sign up or log in
3. Navigate to **API Keys**
4. Create a new key
5. Copy the key

### Add to Spokenly

1. Open **Spokenly > Settings > AI Prompt**
2. Find **API Key** field
3. Paste your Cerebras API key
4. Set the API provider to Cerebras (if available) or use the base URL

### Recommended Models

Check [Cerebras documentation](https://cloud.cerebras.ai/docs) for current model availability.

---

## Troubleshooting

### "Rate limit exceeded" errors

- You've hit the free tier limit
- Wait a minute, or switch to your fallback model
- Consider upgrading to a paid plan for heavy usage

### "Invalid API key" errors

- Double-check you copied the full key
- Make sure there are no extra spaces
- Verify the key hasn't been revoked

### Slow responses

- Try a smaller/faster model
- Check your internet connection
- Both Groq and Cerebras are generally very fast
