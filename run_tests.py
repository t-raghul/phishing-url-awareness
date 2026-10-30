from phishing_checker import inspect_url
from pathlib import Path
import platform
import sys
from datetime import date

cases = [
    ("https://www.example.com/login",
     ["No listed warning signs"]),
    ("http://192.0.2.10/account",
     ["IP address", "HTTP"]),
    ("http://example.com@sample.invalid/login",
     ["@ symbol", "HTTP"]),
    ("https://a.b.c.d.e.example.invalid/path",
     ["many hostname segments"]),
    ("https://xn--example.invalid/",
     ["punycode-style"])
]

rows = [
    "# Test Results",
    "",
    f"Python: {platform.python_version()} | OS: {platform.system()} | Date: {date.today()}",
    "",
    "| # | Input | Expected result | Actual result | Pass/Fail |",
    "|---|---|---|---|---|"
]

passed = 0

for i, (url, expected) in enumerate(cases, 1):
    actual = inspect_url(url)
    success = all(
        any(word.lower() in finding.lower() for finding in actual)
        for word in expected
    )
    status = "PASS" if success else "FAIL"
    passed += success

    print(f"Test {i}: {status}")
    print("Input:", url)
    for finding in actual:
        print(" -", finding)

    rows.append(
        f"| {i} | {url} | {' + '.join(expected)} | "
        f"{'; '.join(actual)} | {status} |"
    )

rows.extend([
    "",
    "## Notes",
    "The checker identifies visible warning signs without visiting URLs.",
    "A URL with no listed warnings is not necessarily safe."
])

Path("tests/test_samples.md").write_text(
    "\n".join(rows), encoding="utf-8"
)

print(f"\nRESULT: {passed}/5 tests passed")
sys.exit(0 if passed == 5 else 1)
