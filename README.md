# Convore Python Repository

This repository contains several packages for interacting with the Convore API in Python.

## Packages

- `convore_api_client`: A Python client for the Convore API. It is responsible for making low-level API calls.
- `convore_sdk`: A Python SDK for the Convore API. It builds upon the `convore_api_client` to provide higher-level abstractions for easier interaction with the API.
- `demo`: A demo application showcasing the usage of the `convore_sdk` to interact with the Convore API.

## Getting Started

### Running the Demo

To run the demo application, follow these steps:

1. Navigate to the `demo` folder:

   ```bash
   cd demo
   ```

2. Install the required dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Run the demo application:

   ```bash
   poetry run python -m demo_app
   ```

   Replace `demo_app` with the name of your demo application module. e.g. `gmail_assistant`.

### Developing demos

To work on demos, you can follow these steps:

1. Open the `demo` folder in IntelliJ IDEA.
2. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

3. To develop: Configure Poetry in IntelliJ IDEA following the instructions in the [JetBrains documentation](https://www.jetbrains.com/help/idea/poetry.html).

### Developing the Python SDK

To work on the `convore_sdk`, you can follow these steps:

1. Open the `convore_sdk` folder in IntelliJ IDEA.
2. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Configure Poetry in IntelliJ IDEA following the instructions in the [JetBrains documentation](https://www.jetbrains.com/help/idea/poetry.html).

### Generating the Convore Client

If the Convore API changes, you need to regenerate the `convore_api_client`:

1. Install the OpenAPI Generator if you haven't already:

   ```bash
   brew install openapi-generator
   ```

2. Ensure that the backend server is running.
3. Run the OpenAPI Generator:

   ```bash
   openapi-generator generate -i http://localhost:8080/openapi -g python --additional-properties=packageName=convore_api_client,datetimeFormat=%Y-%m-%dT%H:%M:%SZ -o ./convore_api_client
   ```

