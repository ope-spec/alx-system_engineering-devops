# Nginx Port 80 Outage Postmortem

## Issue Summary

- **Duration**:
  - Start Date: 06-09-2023
  - End Date: 07-09-2023

- **Root Cause**:
  - Misconfiguration of Nginx server preventing it from listening on port 80.

## Timeline

- **Detection Time**:
  - 06-09-2023 06:00PM 

- **Detection Method**:
  - A surge in error logs and connection issues.

- **Actions Taken**:
  - Investigated Nginx server configurations.
  - Assumed a misconfiguration related to port 80.

- **Misleading Investigation**:
  - Initially suspected a DDoS attack due to increased traffic.
  - Explored potential issues with the server's hardware.

- **Resolution**:
  - Corrected Nginx server configuration to listen on port 80.

## Root Cause and Resolution

- **Root Cause**:
  - The root cause of the issue was a misconfiguration in the Nginx server, which prevented it from listening on port 80. The server was configured to listen on a different port.

- **Resolution**:
  - The issue was resolved by reconfiguring Nginx to listen on port 80. This was done by modifying the Nginx configuration file to specify the correct port.

## Corrective and Preventative Measures

- **Improvements/Fixes**:
  - Ensure that configuration files are regularly reviewed to prevent misconfigurations.

- **Tasks to Address the Issue**:
  - Regularly audit server configurations for accuracy.

In summary, the Nginx port 80 outage was caused by a misconfiguration in the Nginx server that prevented it from listening on the correct port. The issue was detected when an engineer noticed connection errors, and it was initially misattributed to a DDoS attack. The incident was escalated, and the root cause was identified and resolved by reconfiguring Nginx to listen on port 80. To prevent future occurrences, regular configuration audits and automated monitoring for critical service ports are recommended.
