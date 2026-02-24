# 04 - Detection Logic

## Objective

Detection logic defines the security rules used to identify abnormal or suspicious behavior inside the web application.

These rules are applied on:
logs/app.log

The system uses threshold-based detection to generate alerts.

---

## Detection Rules

| Rule ID | Condition | Severity | Trigger Action |
|----------|----------|----------|--------------|
| D-01 | More than 3 LOGIN_FAILURE from same IP within 5 minutes | High | Generate Alert |
| D-02 | More than 10 API_REQUEST events within 2 minutes | Medium | Generate Alert |
| D-03 | Rapid LOGIN_SUCCESS followed by immediate LOGOUT (<1 min) | Medium | Flag Behavior |
| D-04 | Multiple actions (PAGE_VISIT + API_REQUEST) repeated rapidly | Low | Monitor |

---

## Rule Explanation

### D-01 – Brute Force Detection

If multiple login failures occur from the same IP in a short time:

It indicates:

- Brute-force attack
- Credential guessing
- Unauthorized access attempt

Action:
- Generate High Severity Alert
- Log incident for investigation

---

### D-02 – API Flood Detection

If API requests exceed threshold in short duration:

It may indicate:

- Automated script activity
- Data scraping attempt
- Abuse of API endpoints

Action:
- Trigger Medium Alert
- Monitor session activity

---

### D-03 – Suspicious Session Cycling

If user logs in and logs out repeatedly in short time:

Possible causes:

- Account testing
- Session manipulation
- Automated login script

Action:
- Flag for investigation

---

### D-04 – Activity Pattern Repetition

If multiple page visits and API requests repeat rapidly:

It may indicate:

- Automated bot behavior
- Script-based interaction
- Abnormal usage pattern

---

## Alert Output Example

When a rule triggers, system generates an alert:
```
ALERT GENERATED:
Rule: D-01
User: 1
IP: 127.0.0.1
Severity: High
Time Window: 05:30 - 05:35
Action: Investigate Login Activity
```

---

## Implementation Method

Detection logic is implemented using:

- Python script to parse log file
- Timestamp-based filtering
- Counting event frequency
- Threshold comparison

If condition matches → Alert is generated.

---

## Conclusion

The detection engine transforms raw logs into actionable security alerts.

This enables proactive monitoring of suspicious activity and strengthens system security posture.