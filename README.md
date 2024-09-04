# Parse Schedule for Google Calendar

1. Download the Schedule as a CSV (comma delimited)
2. Run the script
  - arguments: `--input-file` `--output-file` `--instructor-name`

example:

```
python3 ./parse-schedule.py --input-file ./cohort-19-schedule.csv --output-file ./test-file.ics --instructor-name "Scott B."
```