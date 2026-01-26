# Spokenly Dictation Config

**Make voice-to-text actually work for technical writing.**

This configuration turns [Spokenly](https://spokenly.app) into a high-quality dictation tool that handles code, technical terms, and natural speech patterns correctly.

## What This Does

- **Fixes common mishearings**: "clawed code" becomes "Claude Code", "pie thon" becomes "Python"
- **Handles self-corrections**: "I mean", "actually", "wait" properly replace what you said before
- **Removes filler words**: "um", "uh", and stutters disappear automatically
- **Formats intelligently**: Detects when you're dictating lists, code, or prose

## Requirements

1. **Spokenly app** (macOS): [spokenly.app](https://spokenly.app)
2. **AI API key** (free): [Groq](https://console.groq.com) or [Cerebras](https://cloud.cerebras.ai) - see [API-SETUP.md](API-SETUP.md)

## Setup Guide

### Step 1: Get an API Key

Both Groq and Cerebras offer free API access. See [API-SETUP.md](API-SETUP.md) for setup instructions.

### Step 2: Download the Files

Download these files from this repo:
- `pre-ai.sh` - Fixes common dictation errors before AI processing
- `post-ai.sh` - Cleans up AI output before insertion
- `system-prompt.txt` - The AI instructions for transcription

Save them somewhere permanent (e.g., `~/Documents/spokenly-config/`).

### Step 3: Configure Spokenly Settings

Open **Spokenly > Settings > AI Prompt > Advanced Settings**

![Advanced Settings](images/12.png)

Configure these settings:

| Setting | Value |
|---------|-------|
| **Include active window contents** | ON (blue) |
| **Include Clipboard** | ON (blue) |
| **Include active app name** | ON (blue) |
| **Text Model** | `Google Gemini - gemini-2.0-flash` or `qwen/qwen3-32b` |
| **Fallback Text Model** | `OpenRouter - gemini-2.0-flash-001` |

### Step 4: Add the Bash Scripts

Scroll down to **Bash Script** and click to expand.

![Bash Script Settings](images/13.png)

1. Click on **Before AI Processing**
2. Paste the full path to `pre-ai.sh` (e.g., `/Users/yourname/Documents/spokenly-config/pre-ai.sh`)
3. Click **Test Script** to verify it works
4. Click on **After AI Processing**
5. Paste the full path to `post-ai.sh`
6. Click **Test Script** to verify

### Step 5: Add the System Prompt

Scroll to **System Prompt** and click **Custom** to edit.

![System Prompt](images/14.png)

1. Open `system-prompt.txt` in a text editor
2. Copy the entire contents
3. Paste into Spokenly's System Prompt field

## Customization

### Adding Your Own Word Corrections

Edit `pre-ai.sh` to add terms specific to your work. Add new lines following this pattern:

```bash
-e 's/heard/correct/gi' \
```

Examples:
```bash
# Your company name
-e 's/acme corp/ACME Corp/gi' \

# Technical terms in your field
-e 's/kubernetes/Kubernetes/gi' \
-e 's/terraform/Terraform/gi' \
```

The `gi` at the end means: **g**lobally replace (all occurrences) and **i**gnore case.

### Stripping Markdown Formatting

If you mostly dictate into plain text apps, uncomment this line in `post-ai.sh`:

```bash
# output=$(echo "$output" | sed -e 's/^```[a-z]*$//' -e 's/^```$//' | sed '/^$/d')
```

Remove the `#` at the start to activate it.

## Files in This Repo

| File | Description |
|------|-------------|
| `README.md` | This guide |
| `API-SETUP.md` | How to get API keys from Groq or Cerebras |
| `pre-ai.sh` | Pre-processing script (word replacements) |
| `post-ai.sh` | Post-processing script (cleanup) |
| `system-prompt.txt` | The AI prompt for high-fidelity transcription |
| `images/` | Setup screenshots |

## Troubleshooting

### Dictation not working at all
- Verify your API key is entered correctly in Spokenly
- Check that Spokenly has microphone permissions in System Settings > Privacy

### Scripts not running
- Make sure scripts are executable: `chmod +x pre-ai.sh post-ai.sh`
- Verify the full path is correct (use `ls` to check)
- Click **Test Script** in Spokenly to see errors

### Getting rate limited
- Free tiers have limits (see [API-SETUP.md](API-SETUP.md))
- The fallback model will activate automatically
- For heavy usage, consider a paid plan

### Words still being transcribed wrong
- Add corrections to `pre-ai.sh` following the pattern shown above
- Technical terms with unusual pronunciations need explicit mappings

## Credits

Based on my experiments fine-tuning Whisper for dictation. More details at:
https://gullo.ca/blog/whisper-fine-tuning

## License

MIT - Use freely, modify as needed.
