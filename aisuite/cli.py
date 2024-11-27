import argparse
from aisuite import Client


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Interact with Generative AI models using aisuite.")
    parser.add_argument("--model", required=True, help="The model to use (e.g., openai:gpt-4).")
    parser.add_argument("--message", required=True, help="The message to send to the model.")
    return parser.parse_args()


def create_client():
    """
    Create and return an aisuite client.

    Returns:
        Client: An instance of aisuite.Client.
    """
    return Client()


def generate_response(client, model, messages):
    """
    Generate a response using the aisuite client.

    Args:
        client (Client): An initialized aisuite client.
        model (str): The model identifier (e.g., "openai:gpt-4").
        messages (list): List of messages to send to the model.

    Returns:
        str: The response content from the model.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content


def main():
    """
    Main entry point for the CLI.
    """
    args = parse_arguments()
    client = create_client()
    messages = [{"role": "user", "content": args.message}]
    response = generate_response(client, args.model, messages)
    print(response)


if __name__ == "__main__":
    main()
