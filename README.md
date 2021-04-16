# wit-core

wit-core is a message processor for wit.ai.

Organize your intents by defining actions and responses.

## Getting Started

### Prerequisites

- Python 3.6+

### Instalation

```bash
pip install wit-core
```

## Documentation

### Domain

The **domain.yaml** defines how the chatbot should operate according to the definition of the intents.

In the domain you specify the intents, actions and responses.

```python
greet:
    response: 
        text: "Hello, there!"

temperature_get
    action: custom_action
    response:
        text: "The temperature today is {action_return}"

temperature_set
    action: custom_action
    response:
        template: custom_template
```

### Actions

Actions are ways for you to write your own codes. For example, manipulating entities, make an API call, or to query a database.

```python
def custom_action(resource):
    temperature = resource.get_entity("wit$temperature")

    return temperature.value
```

The **resource** parameter allows accessing the properties of the wit.ai response.

#### **Resource properties**

#### `get_latest_message()`

Returns the message sent by the user.

#### `get_intent()`

Returns the properties of the intent.

#### `get_entity("entity_name")`

Returns the properties of the specified entity.

#### `get_trait("trait_name")`

Returns to the properties of the specified trait.

### Responses

It is possible to define two types of responses: plain text and templates.

#### **Text**

You can directly in the domain specify in the **response** a text response quickly.

#### **Templates**

Templates serve to give you the possibility to add some logic to the answer. Templates receive the return value of an action.

```python
def custom_template(action_return):
    # Template logic...

    return "Some response"
```

## Command Line Interface

### **wit-core init**

Creates the directory structure.

```bash
wit-core init
```

### **wit-core shell**

Loads the domain and allows interaction with the chatbot.

```bash
wit-core shell
```

### **wit-core http-server**

Creates a http server that can be used for custom integrations. They provide a URL where you can post messages.

```bash
wit-core http-server
```

### **wit-core websocket-server**

Create a websocket server for real-time interaction with the chatbot. They provide an endpoint where you can send messages.

```bash
wit-core websocket-server
```

## How to use

Creates the folder structure needed for the project.

```bash
wit-core init
```

Create a .env at the root of the application with your secret wit.ai key.

```bash
# Wit.ai
ACCESS_TOKEN=YOUR-SECRET-KEY
```

Interact with the chatbot.

```bash
wit-core shell
```

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Development

Clone the repository:

```bash
git clone https://github.com/LucasOliveiraS/wit-core
```

Install the dependencies:

```bash
poetry install
```

Run tests:

```bash
make tests
```
