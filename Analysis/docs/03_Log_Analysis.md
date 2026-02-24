# 03 - Log Analysis

## Objective

The purpose of log analysis is to examine system-generated logs and identify normal vs suspicious behavior based on activity patterns.

The logs used for analysis are stored in:
**log/app.log**

These logs are generated automatically by the web application.

---

## Log Format

Each log entry contains structured information in JSON format:

Example:
```
{
"timestamp": "2026-02-24T05:30:03.451967",
"ip_address": "127.0.0.1",
"username": "1",
"action": "LOGIN_SUCCESS",
"taskName": null
}
```

### Log Fields Explanation

| Field | Description |
|--------|------------|
| timestamp | Time of event |
| ip_address | Source IP address |
| username | User performing action |
| action | Event type |
| taskName | Additional task info (if applicable) |

---

## Activity Observations

Based on analyzed logs, the following patterns were observed:

### 1. Frequent API Requests

Multiple `API_REQUEST` actions were recorded within short time intervals.

This indicates:

- Heavy interaction with backend
- Possible automated behavior
- Rapid data access attempts

---

### 2. Rapid Login & Logout Cycles

The logs show repeated sequence:

- LOGIN_SUCCESS
- PAGE_VISIT
- API_REQUEST
- LOGOUT

Frequent authentication cycles may indicate:

- Session testing
- Manual testing activity
- Or suspicious automation

---

### 3. Failed Login Attempts

Entries such as:
LOGIN_FAILURE

Indicate:

- Invalid credentials
- Unauthorized access attempts
- Potential brute-force activity

---

## Suspicious Patterns Identified

From the log data, potential anomalies include:

- High frequency API requests in short time window
- Repeated login/logout behavior
- Failed login attempts from same IP
- Rapid switching between actions

---

## Conclusion

The log analysis provides visibility into user behavior inside the system.

It forms the foundation for building detection rules and classifying incidents based on observed activity.

Future improvements may include automated anomaly detection and threshold-based alert generation.