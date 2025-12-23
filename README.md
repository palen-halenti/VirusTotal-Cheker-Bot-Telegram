# VirusTotal Checker Telegram Bot

A professional Telegram bot for security analysis of IP addresses, URLs, and domains using the VirusTotal API!

## Project Overview

VirusTotal Checker Bot is a powerful cybersecurity analysis tool that enables users to check IP addresses, URLs, and domains through integration with the VirusTotal API. The bot provides detailed reports on reputation and threats, helping assess the security of network resources.

BOT BY: [GitHub](https://github.com/arhkypGitProject/ArkhypDanylov-Portfolio)

## Key Features

- **IP Analysis** — Check IP addresses for threats and suspicious activity
- **URL Scanning** — Analyze web links through VirusTotal
- **Domain Analysis** — Verify domain reputation and security
- **Detailed Reporting** — Statistics on malicious, suspicious, and harmless assessments
- **Asynchronous Processing** — Fast responses without blocking operations
- **State Management** — User session handling with FSM (Finite State Machine)

## Technology Stack

- **Python 3.8+** — Core programming language
- **aiogram 3.x** — Asynchronous Telegram Bot API framework
- **VirusTotal API** — Security intelligence and threat detection
- **Asyncio** — Asynchronous I/O operations
- **Requests** — HTTP library for API communication

## Installation

### Prerequisites

1. Python 3.8 or higher
2. Telegram Bot Token from [@BotFather](https://t.me/botfather)
3. VirusTotal API key from [VirusTotal](https://www.virustotal.com)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/arhkypGitProject/VirusTotal-Cheker-Bot-Telegram.git
cd VirusTotal-Cheker-Bot-Telegram
```

2. Install required dependencies:
```bash
pip install aiogram==3.11.1 requests
```

3. Configure API credentials:
   - Open `config.py`
   - Replace `TOKEN` with your Telegram Bot token
   - Replace `API_KEY` with your VirusTotal API key

4. Run the bot:
```bash
python main.py
```

## Usage Guide

### Available Commands

- **/start** — Launch the bot and display the main menu
- **IP SCAN** — Analyze IP addresses for security threats
- **URL CHECK** — Scan URLs for malicious content
- **DOMAIN CHECK** — Verify domain security and reputation
- **FILE CHECK** — Check your files for viruses!

### How It Works

1. Users interact with the bot through inline keyboard buttons
2. The bot requests the target (IP, URL, or domain) from the user
3. The request is sent to VirusTotal API for analysis
4. Results are parsed and presented in a structured format
5. Detailed security statistics are displayed to the user

## API Integration

The bot integrates with the following VirusTotal API endpoints:

- `GET /api/v3/ip_addresses/{ip_address}` — IP address analysis
- `POST /api/v3/urls` — URL scanning and analysis
- `GET /api/v3/domains/{domain}` — Domain reputation check

## Important Notes

- This tool provides **informational data only** and is not a replacement for antivirus software
- Rate limits apply based on your VirusTotal API plan
- Always respect privacy and legal regulations when scanning third-party resources
- The bot does not store or log user data or scan results

## Security Considerations

- API keys are stored locally in configuration files
- Input validation is performed on user-provided data
- The bot uses official VirusTotal API with encrypted connections
- No sensitive user data is persisted

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the project documentation

**Disclaimer**: This bot utilizes the VirusTotal API. Users must comply with VirusTotal's terms of service and usage policies. The developer is not responsible for misuse of this tool!
