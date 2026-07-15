Analyze the Apache-style access log located at:

/app/access.log

Create a JSON report at:

/app/report.json

The report must contain exactly these fields:

1. total_requests
   Total number of log entries.

2. unique_ips
   Number of distinct client IP addresses.

3. top_path
   The request path that appears most frequently.

Success Criteria

1. /app/report.json exists.
2. The file contains valid JSON.
3. The JSON contains the required fields.
4. All values are correct.
