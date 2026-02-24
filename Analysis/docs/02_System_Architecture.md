# 02 - System Architecture

## Overview

The system architecture represents how the Security Monitoring Web Application is structured and how different components interact to generate, store, and analyze logs.

The architecture follows a layered approach to separate:

- Application Layer
- Logging Layer
- Storage Layer
- Analysis Layer

---

## Architecture Components

### 1. Web Application Layer

Built using:

- Python
- Flask
- HTML + CSS + JavaScript

This layer handles:

- User authentication
- Dashboard rendering
- API requests
- User interactions

All user activities are captured and forwarded to the logging module.

---

### 2. Logging Layer

Implemented using Python’s logging module.

It captures:

- Timestamp
- IP Address
- Username
- Action performed

Logs are automatically written to:
# 02 - System Architecture

## Overview

The system architecture represents how the Security Monitoring Web Application is structured and how different components interact to generate, store, and analyze logs.

The architecture follows a layered approach to separate:

- Application Layer
- Logging Layer
- Storage Layer
- Analysis Layer

---

## Architecture Components

### 1. Web Application Layer

Built using:

- Python
- Flask
- HTML + CSS + JavaScript

This layer handles:

- User authentication
- Dashboard rendering
- API requests
- User interactions

All user activities are captured and forwarded to the logging module.

---

### 2. Logging Layer

Implemented using Python’s logging module.

It captures:

- Timestamp
- IP Address
- Username
- Action performed

Logs are automatically written to:
# 02 - System Architecture

## Overview

The system architecture represents how the Security Monitoring Web Application is structured and how different components interact to generate, store, and analyze logs.

The architecture follows a layered approach to separate:

- Application Layer
- Logging Layer
- Storage Layer
- Analysis Layer

---

## Architecture Components

### 1. Web Application Layer

Built using:

- Python
- Flask
- HTML + CSS + JavaScript

This layer handles:

- User authentication
- Dashboard rendering
- API requests
- User interactions

All user activities are captured and forwarded to the logging module.

---

### 2. Logging Layer

Implemented using Python’s logging module.

It captures:

- Timestamp
- IP Address
- Username
- Action performed

Logs are automatically written to:
# 02 - System Architecture

## Overview

The system architecture represents how the Security Monitoring Web Application is structured and how different components interact to generate, store, and analyze logs.

The architecture follows a layered approach to separate:

- Application Layer
- Logging Layer
- Storage Layer
- Analysis Layer

---

## Architecture Components

### 1. Web Application Layer

Built using:

- Python
- Flask
- HTML + CSS + JavaScript

This layer handles:

- User authentication
- Dashboard rendering
- API requests
- User interactions

All user activities are captured and forwarded to the logging module.

---

### 2. Logging Layer

Implemented using Python’s logging module.

It captures:

- Timestamp
- IP Address
- Username
- Action performed

Logs are automatically written to:
**log/app.log**

This layer ensures every important event inside the system is recorded.

---

### 3. Storage Layer

The system uses:

- SQLite database for storing user credentials
- Log file storage for activity tracking

Database stores:

- User accounts
- Authentication data

Logs store:

- Behavioral activity
- Security-relevant events

---

### 4. Analysis Layer

The analysis module processes:

This layer ensures every important event inside the system is recorded.

---

### 3. Storage Layer

The system uses:

- SQLite database for storing user credentials
- Log file storage for activity tracking

Database stores:

- User accounts
- Authentication data

Logs store:

- Behavioral activity
- Security-relevant events

---

### 4. Analysis Layer

The analysis module processes:
logs/app.log

It performs:

- Pattern detection
- Suspicious activity identification
- Threshold-based rule checking
- Incident classification

This layer simulates SOC-level monitoring.

---

## Data Flow

User Action → Web App → Logging Module → Log File → Analysis Script → Detection Rules → Alert / Report

---

## Conclusion

This architecture enables real-time log generation and structured security monitoring.

It creates a controlled environment where security events can be generated and analyzed systematically.