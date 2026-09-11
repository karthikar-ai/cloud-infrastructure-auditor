 ## Cloud Infrastructure Auditor \& Cost Optimizer



A Python-based CLI tool that audits cloud infrastructure resources and identifies potential cost-optimization opportunities.



## Features



-  Audits cloud resources for potential cost waste

-  Estimates possible monthly savings

-  Generates JSON and CSV audit reports

-  Uses a safe dry-run cleanup approach

-  Designed for AWS cloud infrastructure auditing

-  Supports mock resources for testing without a real AWS account

-  Simple command-line interface using Typer



##  Current Audit Checks



The project currently identifies:



| Resource | Condition | Example |

|---|---|---|

| EBS Volume | Unattached | `vol-001` |

| Elastic IP | Unused | `eip-001` |

| EC2 Instance | Underutilized | `i-001` |



## 🛠️ Tech Stack



- Python

- Typer

- Boto3

- Moto

- JSON

- CSV

- Git \& GitHub



##  Project Structure



```text

cloud-infrastructure-auditor/

│

├── main.py

├── requirements.txt

├── audit\_report.json

├── audit\_report.csv

├── .gitignore

└── README.md

