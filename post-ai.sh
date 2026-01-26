#!/bin/bash
# Spokenly Post-AI Processing Script
# Cleans up LLM output AFTER processing, before insertion
# Usage: Paste path into Spokenly > Settings > AI Prompt > Bash Scripts > After
#
# Current behavior:
# - Strips leading/trailing whitespace
# - Removes markdown code fences if pasting plain text
# - Removes [No speech detected] placeholder
#
# Uncomment sections below to enable additional processing

input=$(cat)

# Remove [No speech detected] - output nothing instead
if [[ "$input" == "[No speech detected]" ]]; then
  exit 0
fi

# Strip <think>...</think> tags (Qwen/reasoning models) - handles multiline
input=$(echo "$input" | perl -0777 -pe 's/<think>.*?<\/think>//gs' 2>/dev/null || echo "$input" | sed -E 's/<think>.*<\/think>//g')
input=$(echo "$input" | sed '/^$/d')

# Strip leading/trailing whitespace
output=$(echo "$input" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

# Word replacements (proper nouns Whisper often gets wrong)
output=$(echo "$output" | sed \
  -e 's/Joel Gula/Joel Gullo/gi' \
  -e 's/Joel Gouda/Joel Gullo/gi' \
  -e 's/Mr\. Gula/Mr. Gullo/gi' \
  -e 's/Mr\. Gouda/Mr. Gullo/gi' \
  -e 's/Jai Hei/Jiahui/gi' \
  -e 's/Gia Hui/Jiahui/gi' \
  -e 's/Jia Hui/Jiahui/gi' \
)

# OPTIONAL: Strip markdown code fences (uncomment if pasting to plain text apps)
# output=$(echo "$output" | sed -e 's/^```[a-z]*$//' -e 's/^```$//' | sed '/^$/d')

# OPTIONAL: Convert markdown bold **text** to plain text (uncomment for plain text)
# output=$(echo "$output" | sed 's/\*\*\([^*]*\)\*\*/\1/g')

# OPTIONAL: Convert markdown italic *text* to plain text (uncomment for plain text)
# output=$(echo "$output" | sed 's/\*\([^*]*\)\*/\1/g')

# OPTIONAL: Strip all markdown formatting (aggressive - uncomment for pure plain text)
# output=$(echo "$output" | sed \
#   -e 's/^#+[[:space:]]*//' \
#   -e 's/\*\*\([^*]*\)\*\*/\1/g' \
#   -e 's/\*\([^*]*\)\*/\1/g' \
#   -e 's/`\([^`]*\)`/\1/g' \
#   -e 's/^-[[:space:]]*//' \
#   -e 's/^[0-9]\+\.[[:space:]]*//')

echo "$output"
