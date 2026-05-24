#!/bin/bash
# Push script for portuguese-coder-finetune
# Run this on a machine with GitHub authentication

set -e

echo "🚀 Pushing to impacte-tech/portuguese-coder-finetune"

# Check if we're in the right directory
if [ ! -f "train.py" ]; then
    echo "❌ Error: Run this script from the portuguese-coder-finetune directory"
    exit 1
fi

# Add remote if not exists
git remote get-url origin &>/dev/null || git remote add origin https://github.com/impacte-tech/portuguese-coder-finetune.git

# Ensure we're on main branch
git branch -M main

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main

echo "✅ Successfully pushed to https://github.com/impacte-tech/portuguese-coder-finetune"
