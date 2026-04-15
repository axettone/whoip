# whoip

A minimal command-line tool that takes a list of IP addresses and returns geolocation and ownership information for each one, using the [ipinfo.io](https://ipinfo.io) API and local reverse DNS lookup.

## Features

- Looks up country, city, and ASN/org for each IP via ipinfo.io
- Performs reverse DNS resolution locally (no extra API calls)
- Reads from stdin — pipe-friendly and easy to compose with other tools
- No external dependencies — pure Python standard library
- Respects ipinfo.io free tier rate limits automatically

## Requirements

- Python 3.6+
- No third-party packages needed

## Installation (macOS / Linux)

```bash
sudo cp whoip.py /usr/local/bin/whoip
sudo chmod +x /usr/local/bin/whoip
```

You can then call it from anywhere as `whoip`.

## Usage

Pipe a newline-separated list of IPs:

```bash
echo "8.8.8.8
1.1.1.1
95.233.61.219" | whoip
```

Or from a file:

```bash
whoip < ip_list.txt
```

### Example output

```
8.8.8.8               US  Mountain View         dns.google                                AS15169 Google LLC
1.1.1.1               AU  Sydney                one.one.one.one                           AS13335 Cloudflare, Inc.
95.233.61.219         IT  Milan                 n/d                                       AS1234 Some ISP
```

Columns: `IP · Country · City · Hostname (reverse DNS) · Org/ASN`

## API key (optional)

The tool works without an API key up to **50,000 requests/month** on the ipinfo.io free tier. If you have an account, add your token to the URL in the script:

```python
url = f"https://ipinfo.io/{ip}/json?token=YOUR_TOKEN_HERE"
```

## License

MIT
