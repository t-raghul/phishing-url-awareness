# Test Results

Python: 3.11.8 | OS: Windows | Date: 2026-10-30

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain.; Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully.; Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | punycode-style | Contains a punycode-style hostname. | PASS |

## Notes
The checker identifies visible warning signs without visiting URLs.
A URL with no listed warnings is not necessarily safe.