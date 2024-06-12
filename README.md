**Project Title: University at Buffalo 🦬🤘Campus Job Monitor**

**Overview:**
This project provides a Python script, `app.py`, designed to monitor job openings at the University at Buffalo's dining services website (https://ubdining.com/jobs/student-jobs). It utilizes web scraping techniques to detect changes in the webpage content, specifically looking for the presence of certain keywords related to job openings. Upon detection of relevant changes, the script triggers a push notification using the Pushover service, which can be received on mobile devices.

**Technologies Used:**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Pushover](https://img.shields.io/badge/Pushover-API-orange?logo=pushover&style=for-the-badge)](https://pushover.net/)
[![AWS EC2](https://img.shields.io/badge/AWS-EC2-yellow?logo=amazon-aws&style=for-the-badge)](https://aws.amazon.com/ec2/)

- **Python:** The script is written in Python, leveraging libraries such as `requests`, `BeautifulSoup`, and `datetime` for web requests, HTML parsing, and timestamp management, respectively.
- **Pushover:** Pushover is utilized for sending push notifications to mobile devices. The script integrates with Pushover's API to deliver notifications.
- **AWS EC2:** Amazon Web Services (AWS) Elastic Compute Cloud (EC2) is used for hosting the Python script. EC2 provides scalable computing capacity in the cloud, allowing for deployment and execution of the monitoring script.
- **GitHub:** The project is hosted on GitHub, facilitating version control and collaboration.

**How it Works:**
The `app.py` script periodically scrapes the specified webpage (`https://ubdining.com/jobs/student-jobs`) for changes in content. It searches for the presence of predefined keywords, such as "opened", indicating job availability. If a relevant change is detected, the script sends a push notification containing details of the job opening, including a timestamp and a direct link to the webpage. The script runs indefinitely, continuously checking for updates at regular intervals.

**Deployment on AWS EC2:**
To host the monitoring script, an AWS EC2 instance was provisioned. The script is deployed on this instance, allowing it to run autonomously in the cloud environment. By leveraging EC2's scalability and reliability, the monitoring process is ensured to be consistently available, regardless of the user's local machine status. This setup enables seamless job monitoring without the need for manual intervention.

**Ease of Job Monitoring:**
The project aims to simplify the process of tracking job openings at the University at Buffalo's dining services. By automating the monitoring task and delivering real-time notifications, users can stay informed about job opportunities without the need for constant manual checking. This approach enhances efficiency and competitiveness in accessing job listings, providing users with timely updates and a competitive advantage in the application process.
