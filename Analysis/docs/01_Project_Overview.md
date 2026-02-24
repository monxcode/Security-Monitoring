# 01 - Project Overview

## Project Purpose

This project is a Security Monitoring & Incident Response Web Application designed to simulate real-world SOC (Security Operations Center) operations.

The system demonstrates how web application activity can be monitored, logged, analyzed, and used to detect suspicious behavior.

---

## Objective

The main objectives of this project are:

- Develop a custom web application
- Generate structured logs from user activity
- Analyze logs for abnormal behavior
- Create detection rules based on real activity
- Classify incidents based on severity
- Define response procedures
- Improve security maturity through documentation

---

## System Functionality

The application includes:

- User authentication (Login / Logout)
- Dashboard interface
- API request simulation
- Automatic logging of:
  - Login attempts
  - Page visits
  - API requests
  - Logout events

All activity is recorded in [Log Data File](/logs/app.log) for analysis.

---

## Security Perspective

Instead of analyzing random internet logs, this project generates its own logs from a custom-built application.

This approach ensures:

- Real-time log generation
- Controlled environment
- Practical detection rule creation
- Accurate incident simulation

---

## Conclusion

The project demonstrates end-to-end implementation of:

Application → Log Generation → Log Analysis → Detection Rules → Incident Response

It reflects practical cybersecurity monitoring principles used in enterprise environments.