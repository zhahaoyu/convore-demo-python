
### Running the Demo

To run the Gmail Assistant demo, execute the following command:

```bash
poetry install
poetry run python -m gmail_assistant
```

This will start the assistant, which will listen for incoming emails and automatically label them based on the predefined criteria.

### Development and Maintenance
- Adding new labels: To add new labels, update the `list_agent_managed_label_specs` function in `utils.py` with the new label specifications.
- Modifying triage criteria: To change how emails are triaged, modify the `triage_conversation` function in `triage_conversation.py` and adjust the prompt template or the logic for choosing labels.
