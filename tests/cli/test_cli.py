from aisuite.cli import parse_arguments, generate_response, create_client
from unittest.mock import patch
from unittest.mock import MagicMock
from aisuite import Client

def test_parse_arguments():
    test_args = ["--model", "openai:gpt-4", "--message", "Hello, world!"]
    with patch("argparse._sys.argv", ["cli.py"] + test_args):
        args = parse_arguments()
        assert args.model == "openai:gpt-4"
        assert args.message == "Hello, world!"



def test_generate_response():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Test response"
    mock_client.chat.completions.create.return_value = mock_response

    model = "openai:gpt-4"
    messages = [{"role": "user", "content": "Hello"}]

    result = generate_response(mock_client, model, messages)
    assert result == "Test response"
    mock_client.chat.completions.create.assert_called_once_with(
        model=model, messages=messages
    )



def test_create_client():
    client = create_client()
    assert isinstance(client, Client)
