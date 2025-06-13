# AWS Cron Expression Checker

A collection of tools for validating AWS cron expressions. This repository provides utilities in multiple programming languages to check if a given cron expression matches the AWS cron syntax using accurate regular expressions.

## Features

- **Validate AWS cron expressions**  
- **Multi-language support**  
- **Importable modules for easy integration**  
- **Consistent validation logic across languages**

## Supported Languages

- Python
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

# AWS Cron Expression Field Rules
## AWS Cron Expression Format

AWS cron expressions have the following format:

```
cron(Minutes Hours Day-of-month Month Day-of-week Year)
```

## Minute Field (`0-59`)

| Allowed Syntax               | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| `*`                         | Every minute                                                               |
| `*/n`                       | Every n minutes (n: positive integer ≤ 59)                                 |
| `m`                         | Single minute (0–59)                                                       |
| `m1,m2,...`                 | Comma-separated list of minute values                                      |
| `m1-m2`                     | Minute range (inclusive)                                                   |
| `m1-m2/n` or `m/n`          | Step values after a range or single value                                  |

### Disallowed:
- Values outside 0–59
- Expressions like `*/5,10` (mix of step and explicit values with `*`)
- Empty segments or leading/trailing commas (e.g., `,10` or `10,`)

---

## Hour Field (`0-23`)

| Allowed Syntax               | Description                                                               |
|-----------------------------|---------------------------------------------------------------------------|
| `*`                         | Every hour                                                                |
| `*/n`                       | Every n hours (1 ≤ n ≤ 23)                                                |
| `h`                         | Single hour (0–23)                                                        |
| `h1,h2,...`                 | Comma-separated list of hours                                             |
| `h1-h2`                     | Hour range                                                                |
| `h1-h2/n` or `h/n`          | Step values based on a single hour or range                               |

### Disallowed:
- Values outside 0–23
- Steps/ranges with invalid numbers (e.g., `25`, `0-30`, `*/0`)

---

## Day of Month Field (`1-31`)

| Allowed Syntax         | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `*`                    | Every day of the month                                                      |
| `?`                    | No specific value (used when field is ignored)                             |
| `L`                    | Last day of the month                                                      |
| `d`                    | Day of month (1–31)                                                        |
| `dW`                   | Nearest weekday to day `d`                                                 |
| `d1-d2`                | Day range                                                                  |
| `d1-d2/n`              | Step values within day range                                               |
| `d1,d2,d3,...`         | Comma-separated values                                                     |

### Restrictions:
- `W` only after a single day (e.g., `15W`)
- `L` must be used alone
- No `#` or combinations with `L`
- No `W` in ranges or with steps

### Invalid Examples:
- `0`, `32`, `1-32` — invalid day values
- `L,15`, `15/L`, `15W-20`, `15W/2`
- Leading/trailing commas: `,15`, `15,`

---

## Month Field (`1-12` or `JAN-DEC`)

| Allowed Syntax       | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `*`                  | Every month                                                                 |
| `*/n`                | Every n months (1 ≤ n ≤ 12)                                                 |
| `m` / `MON`          | Month number (1–12) or name (JAN–DEC)                                       |
| `m1-m2` / `JAN-MAR`  | Ranges in numeric or name mode (no mixing)                                  |
| `m/n` / `JAN/n`      | Step values starting at m or JAN                                            |
| `m1,m2,...`          | Comma-separated list of months (all numeric or all named)                   |

### Restrictions:
- Cannot mix numeric and named months (e.g., `1,JAN`)
- Valid names: `JAN` to `DEC`
- No zero-padded numbers (e.g., `05`)
- No spaces allowed
- No invalid names like `FOO`

### Invalid Examples:
- `JAN-12`, `1,JUN`, `0`, `13`, `JAN,FOO`, ` 1-10 `, `5,,10`, `5/2/3`

---

## Day of Week Field (`1-7` or `SUN-SAT`)

| Allowed Syntax     | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `*`                | Every day                                                                   |
| `?`                | No specific day                                                             |
| `L`                | Last specific weekday of the month                                          |
| `d` / `MON`        | Day of week number (1–7, Sunday = 1) or name (SUN–SAT)                      |
| `dL`               | Last instance of weekday `d` (e.g., `5L` = last Thursday)                   |
| `d#n`              | nth occurrence of day `d` (e.g., `FRI#3` = third Friday)                    |
| `d1-d2` / `MON-FRI`| Range of days                                                               |
| `d1-d2/n`          | Step through day range                                                      |
| `d1,d2,...`        | Comma-separated values                                                      |

### Restrictions:
- Valid days: 1–7 or SUN–SAT only
- No spaces, decimals, multiple slashes, or trailing commas
- No step values with `*` (e.g., `*/2` invalid)
- Only one modifier per item (`L` or `#`)
- `#` values must be 1–5 only

### Invalid Examples:
- `0`, `8`, `*/4`, `1,8`, `MON,FOO`, `5,,7`, `5,7,`, `5/2/3`, `5.5`, `5#6`, `FRI#0`, `8L`, empty string

---

## Year Field (`1970-2199`)

| Allowed Syntax         | Description                                                               |
|------------------------|---------------------------------------------------------------------------|
| `*`                    | Every year                                                                |
| `*/n`                  | Every n years from 1970                                                   |
| `y`                    | Specific year (1970–2199)                                                 |
| `y1-y2`                | Year range                                                                |
| `y/n` or `y1-y2/n`     | Step values after single year or range                                    |
| `y1,y2,...`            | Comma-separated year expressions                                          |

### Disallowed:
- Years <1970 or >2199
- Invalid ranges (e.g., `2030-2020`)
- Invalid step values: `*/0`, `/-5`
- Leading/trailing commas, empty segments

Refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) for details.

## License

This project is licensed under the MIT License.