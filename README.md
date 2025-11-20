# Homeschool Time Tracker

A simple, local-first time tracking app for homeschool families. Track time spent on each student and subject using plain markdown files and hashtags.

## Features

- ⏱️ **Inline Timer**: Start/pause/stop timer with automatic time recording
- 🏷️ **Smart Hashtags**: Autocomplete for students (#alice, #bob) and subjects (#math, #core/reading)
- 📝 **Markdown-Based**: All data stored as plain `.md` files (works with Obsidian!)
- ⚙️ **Easy Setup**: Edit students and subjects in the built-in Settings tab
- 📊 **CSV Export**: Export all logged time to CSV with the included Python script
- 🔒 **100% Local**: No server, no account, no internet required

## Quick Start

1. **Download the files** or clone this repository
2. **Open `timer.html`** in Chrome or Edge
3. **Click "Select Project Folder"** and choose the `homeschool-timer` folder
4. **Start tracking!** Type `#` to see autocomplete suggestions

## Usage

### Inline Timer Workflow

1. Click "New Timer Entry" or type: `- [Timer] #student #subject`
2. Add notes on the next line (optional)
3. Click "Start Timer"
4. Click "Stop Timer" when done - it replaces `[Timer]` with actual times

**Example:**
```markdown
- [Timer] #alice #core/math
  Working on multiplication tables
```

Becomes:
```markdown
- 09:15 – 09:32 → #alice #core/math
  Working on multiplication tables
```

### Hashtag Autocomplete

- Type `#c` → see all tags starting with "c"
- Type `#core/` → see nested tags like #core/math, #core/reading
- Use ↑/↓ arrows to navigate, Enter to select

### Customize Students & Subjects

1. Go to **Settings** tab
2. Edit students and subjects
3. Format: `#tagname - Description`
4. Click Save to update autocomplete

### Export to CSV

Run the Python script to generate a CSV report:

```bash
python export-times.py
```

Opens `homeschool-time-report.csv` with all logged time.

## File Structure

```
homeschool-timer/
├── timer.html           # Main app (open this!)
├── export-times.py      # CSV export script
├── Students/
│   └── students.md      # Student hashtag definitions
├── Subjects/
│   └── subjects.md      # Subject hashtag definitions
├── Logbook/
│   ├── 2025-11-19.md   # Daily log files
│   └── 2025-11-20.md
└── Templates/
    └── Daily Log.md     # Template for new logs
```

## Why This Approach?

- **Future-proof**: Plain text files work everywhere
- **Flexible**: Use with any text editor or Obsidian
- **Simple**: No complicated setup or learning curve
- **Portable**: Works offline, no vendor lock-in
- **Privacy**: All data stays on your computer

## Browser Compatibility

Requires a browser with File System Access API support:
- ✅ Chrome/Edge (recommended)
- ❌ Firefox (not supported yet)
- ❌ Safari (not supported yet)

## License

Free to use and modify for personal or educational purposes.

---

**Happy Homeschooling!** 📚✏️
