# The-Eyes-Osint
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-green.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<pre align="center" style="color: #a855f7;">
████████╗██╗  ██╗███████╗    ███████╗██╗   ██╗███████╗███████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝
   ██║   ███████║█████╗      █████╗   ╚████╔╝ █████╗  ███████╗
   ██║   ██╔══██║██╔══╝      ██╔══╝    ╚██╔╝  ██╔══╝  ╚════██║
   ██║   ██║  ██║███████╗    ███████╗   ██║   ███████╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚══════╝╚══════╝
</pre>

<h3 align="center">🔍 Advanced Website OSINT Intelligence Tool</h3>

<p align="center">
  <b>The Eyes</b> is a powerful, all-in-one OSINT tool designed to extract comprehensive intelligence from any website. Simply enter a target domain and let The Eyes uncover everything.
</p>

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 🌐 **WHOIS Lookup** | Domain registration details, registrar info, expiration dates |
| 📝 **DNS Enumeration** | DNS records (A, AAAA, MX, NS, TXT, SOA, CNAME) |
| 🔎 **Subdomain Discovery** | Find subdomains using wordlist and certificate transparency |
| 🗺️ **IP Geolocation** | Physical location, ISP, ASN details of server IP |
| 🛠️ **Technology Detection** | CMS, frameworks, libraries, server software |
| 🔒 **SSL Certificate** | Certificate details, issuer, validity, SANs |
| 🛡️ **Security Headers** | Analyze HTTP security headers configuration |
| 🔌 **Port Scanning** | Scan common ports for exposed services |
| 📚 **Wayback Machine** | Historical URLs and archived snapshots |
| 🖥️ **Server Fingerprinting** | Server type, version, and operating system |

---

## 🚀 Installation

### Quick Install (Linux/macOS)

```bash
# Clone the repository
git clone https://github.com/yourusername/the-eyes.git
cd the-eyes

# Install dependencies
pip3 install -r requirements.txt

# Run The Eyes
python3 the_eyes.py
