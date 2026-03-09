# M542 Cryptology — TLS/SSL Cryptographic Attacks

**Institution:** Gisma University of Applied Sciences  
**Department:**BusinessManagement and CyberSecurity 
**Module:** M542 Cryptology | **Semester:** Winter 2025  
**Author:** Rahul Ponnaluri | **GitHub:** RaHuLo40  

---

## 📋 Project Overview

This project analyses and demonstrates real-world cryptographic
vulnerabilities in the TLS/SSL protocol family as part of the
M542 Cryptology individual project assessment.

The following attacks are studied, implemented, and analysed:

| Attack | CVE | Protocol Affected | Risk |
|--------|-----|-------------------|------|
| BEAST | CVE-2011-3389 | TLS 1.0 CBC | 🔴 Critical |
| POODLE | CVE-2014-3566 | SSLv3 | 🔴 Critical |
| LUCKY13 | — | TLS CBC MAC | 🟡 High |
| HEARTBLEED | CVE-2014-0160 | OpenSSL | 🔴 Critical |

---

## 🗂️ Repository Structure
```
m542-tls-ssl-cryptology/
├── code/
│   ├── tls_scanner.py       # Python TLS vulnerability scanner
│   └── nginx.conf           # Deliberately weak Nginx TLS config
├── screenshots/
│   ├── 01_docker_server.png
│   ├── 02_scanner_output.png
│   ├── 03_wireshark_handshake.png
│   └── 04_wireshark_clienthello.png
├── report/
│   └── TLS_SSL_Report.pdf
└── README.md
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 + SSLyze | TLS vulnerability scanner |
| Docker + Nginx 1.14 | Vulnerable HTTPS lab server |
| OpenSSL | Self-signed certificate generation |
| Wireshark | Packet capture and handshake analysis |
| Kali Linux | Attack and testing platform |

---

## 🚀 How to Reproduce

### 1. Set up the vulnerable lab server
```bash
docker run -d \
  --name vulnerable-tls \
  -p 443:443 \
  -v ~/cryptology/tls-project/certs:/etc/nginx/certs \
  -v ~/cryptology/tls-project/nginx-config/nginx.conf:/etc/nginx/nginx.conf \
  nginx:1.14
```

### 2. Install dependencies
```bash
pip3 install sslyze colorama
```

### 3. Run the scanner
```bash
python3 code/tls_scanner.py
```

---

## 📊 Scan Results Summary

| Protocol | Status | Vulnerability | Risk Level |
|----------|--------|--------------|------------|
| SSLv2 | ✅ Disabled | None | Safe |
| SSLv3 | ✅ Disabled | POODLE Safe | Safe |
| TLS 1.0 | ❌ ENABLED | BEAST Attack | 🔴 HIGH |
| TLS 1.1 | ⚠️ ENABLED | Deprecated | 🟡 MEDIUM |
| TLS 1.2 | ✅ Supported | None | Safe |
| TLS 1.3 | ℹ️ Not Supported | N/A | Informational |
| Heartbleed | ✅ Not Vulnerable | None | Safe |

---

## 📸 Screenshots

### 1. Docker Vulnerable Server Running
![Docker Server](screenshots/01_docker_server.png)

### 2. TLS Scanner Output
![Scanner Output](screenshots/02_scanner_output.png)

### 3. Wireshark — TLS Handshake Capture
![Wireshark Handshake](screenshots/03_wireshark_handshake.png)

### 4. Wireshark — ClientHello Packet Detail
![ClientHello](screenshots/04_wireshark_clienthello.png)

---

## 📚 References

- Rizzo, J. and Duong, T. (2011) *BEAST Attack* — TLS 1.0 CBC vulnerability
- Moller, B., Duong, T. and Kotowicz, K. (2014) *POODLE* — SSLv3 padding oracle
- Al Fardan, N. and Paterson, K. (2013) *Lucky Thirteen* — TLS timing side-channel
- Codenomicon (2014) *Heartbleed* — OpenSSL memory disclosure
```
```

## 📂 Step 5 — Create Folders and Upload Files

### Create the `code/` folder:
1. Click **"Add file"** → **"Create new file"**
2. In the filename box type: `code/tls_scanner.py`
3. Paste your full scanner Python code in the editor
4. Scroll down → **"Commit changes"**

### Create the `code/nginx.conf`:
1. Click **"Add file"** → **"Create new file"**
2. Filename: `code/nginx.conf`
3. Paste your Nginx config
4. **"Commit changes"**

---

## 🖼️ Step 6 — Upload Screenshots

1. Click into the `screenshots/` folder (or create it by clicking **"Add file"** → **"Create new file"** → type `screenshots/.gitkeep` → commit)
2. Then click **"Add file"** → **"Upload files"**
3. Drag and drop your screenshots
4. Name them exactly:
   - `01_docker_server.png`
   - `02_scanner_output.png`
   - `03_wireshark_handshake.png`
   - `04_wireshark_clienthello.png`
5. Click **"Commit changes"**

---

## 📄 Step 7 — Upload Your Report PDF

1. Go into `report/` folder
2. **"Add file"** → **"Upload files"**
3. Upload your PDF report
4. **"Commit changes"**

---

## ✅ Final Result

```
https://github.com/RaHuLo40/m542-tls-ssl-cryptology
