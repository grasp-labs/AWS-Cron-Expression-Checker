# AWS Cron Expression Checker

A collection of tools for validating AWS cron expressions. This repository provides utilities in multiple programming languages to check if a given cron expression matches the AWS cron syntax using accurate regular expressions.

## Features

- **Validate AWS cron expressions**  
- **Multi-language support**  
- **Importable modules for easy integration**  
- **Consistent validation logic across languages**

## Supported Languages

- Python
- JavaScript/TypeScript
- Java
- Go
- (More coming soon!)

## Usage

Each language-specific folder contains an importable module and usage instructions. Example usage in Python:

```python
from aws_cron_checker import is_valid_aws_cron

expression = "cron(0 12 * * ? *)"
if is_valid_aws_cron(expression):
  print("Valid AWS cron expression!")
else:
  print("Invalid AWS cron expression.")
```

## AWS Cron Expression Format

AWS cron expressions have the following format:

```
cron(Minutes Hours Day-of-month Month Day-of-week Year)
```

Refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) for details.

## Contributing

Contributions for new languages and improvements are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.