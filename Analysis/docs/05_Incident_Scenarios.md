# 05 - Incident Scenarios & Response Steps

## Objective

This section defines practical security incident scenarios based on detected abnormal behavior in the system.

Each scenario includes:

- Detection trigger
- Severity level
- Impact analysis
- Response steps

---

## Scenario 1: Brute Force Login Attempt

### Detection Trigger
- More than 3 failed login attempts from same IP within 5 minutes

### Severity
High

### Impact
- Account compromise risk
- Unauthorized access attempt
- Credential guessing activity

### Response Steps
1. Block IP address temporarily
2. Lock the affected account
3. Review authentication logs
4. Notify system administrator
5. Reset password if required

---

## Scenario 2: API Request Flooding

### Detection Trigger
- More than 10 API_REQUEST events within 2 minutes

### Severity
Medium

### Impact
- System resource abuse
- Potential automated attack
- Data extraction attempt

### Response Steps
1. Monitor session activity
2. Apply rate limiting
3. Identify source IP
4. Investigate user behavior
5. Add IP to watchlist

---

## Scenario 3: Suspicious Session Cycling

### Detection Trigger
- LOGIN_SUCCESS followed by immediate LOGOUT repeatedly
- Short session duration (<1 minute)

### Severity
Medium

### Impact
- Session testing
- Automated login script
- Possible credential misuse

### Response Steps
1. Track session history
2. Validate user legitimacy
3. Check IP consistency
4. Enable additional authentication checks

---

## Scenario 4: Rapid Page + API Interaction

### Detection Trigger
- PAGE_VISIT + API_REQUEST repeated rapidly in short time window

### Severity
Low to Medium

### Impact
- Automated user interaction
- Bot-like behavior
- Potential reconnaissance

### Response Steps
1. Log behavior for monitoring
2. Increase threshold sensitivity
3. Observe if pattern repeats
4. Escalate if combined with other anomalies

---

## Conclusion

Defining structured incident scenarios improves preparedness and enables faster response to detected threats.

These scenarios simulate real-world security incidents encountered in enterprise environments.