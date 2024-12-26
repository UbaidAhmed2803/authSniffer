# AuthSniffer 🔍  

**AuthSniffer** is a Python script designed to identify unauthenticated endpoints from a list of available API endpoints. It helps security professionals and developers ensure their APIs are properly secured and prevents potential vulnerabilities due to unauthenticated access.

---

## Features  
- Automatically checks API endpoints for unauthenticated access.  
- Detects endpoints returning `200 OK` responses and verifies the response content for authentication errors (e.g., `Access Denied`).  
- Logs results in a clear format for further analysis.  
- Easy to configure and use with any list of endpoints.  

---

## Installation  

Clone the repository:  
   ```  
   git clone https://github.com/yourusername/AuthSniffer.git  
   cd AuthSniffer  
```
## Usage:

1. Prepare a text file containing your endpoints, one per line (e.g., endpoints.txt).
2. Run the script:
```
python authsniffer.py endpoints.txt  
```
3. Review the results:

- [UNAUTHENTICATED]: The endpoint is accessible without authentication.
- [SECURED]: The endpoint requires authentication.
- [ERROR]: Issues reaching the endpoint (e.g., network errors).


## Example Output
```
[UNAUTHENTICATED] https://api.example.com/v1/data is accessible without authentication.  
[SECURED] https://api.example.com/v1/user requires authentication (Status: 401).  
[UNKNOWN] https://api.example.com/v1/test returned status 500.
```
