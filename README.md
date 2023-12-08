# <p align="center">C-DOTS: Code Documenter, Optimizer, Translator, and Summarizer</p>

<p align="center">
    <img src="./c-dots.png" width=250 height=250 />
</p>

<p align="center">
    <p align="center">
        <a href="https://github.com/SusheelThapa/C-DOTS/" target="blank">
            <img src="https://img.shields.io/github/watchers/SusheelThapa/C-DOTS?style=for-the-badge&logo=appveyor" alt="Watchers"/>
        </a>
        <a href="https://github.com/SusheelThapa/C-DOTS/fork" target="blank">
            <img src="https://img.shields.io/github/forks/SusheelThapa/C-DOTS?style=for-the-badge&logo=appveyor" alt="Forks"/>
        </a>
        <a href="https://github.com/SusheelThapa/C-DOTS/stargazers" target="blank">
            <img src="https://img.shields.io/github/stars/SusheelThapa/C-DOTS?style=for-the-badge&logo=appveyor" alt="Star"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/SusheelThapa/C-DOTS/issues" target="blank">
            <img src="https://img.shields.io/github/issues/SusheelThapa/C-DOTS.svg?style=for-the-badge&logo=appveyor" alt="Issue"/>
        </a>
        <a href="https://github.com/SusheelThapa/C-DOTS/pulls" target="blank">
            <img src="https://img.shields.io/github/issues-pr/SusheelThapa/C-DOTS.svg?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/SusheelThapa/C-DOTS/blob/master/LICENSE" target="blank">
            <img src="https://img.shields.io/github/license/SusheelThapa/C-DOTS?style=for-the-badge&logo=appveyor" alt="License" />
        </a>
    </p>
</p>

[C-DOTS](https://github.com/SusheelThapa/C-DOTS) is a versatile tool designed to aid developers in documenting, optimizing, translating, and summarizing code. It supports multiple programming languages, including C, C++, Python, and JavaScript. With an intuitive user interface developed in PyQt, [C-DOTS](https://github.com/SusheelThapa/C-DOTS) streamlines the coding process, making it more efficient and accessible.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Documenter**: Automatically documents the provided code snippet.
- **Optimizer**: Optimizes the provided code for better performance.
- **Translator**: Translates code snippets from one supported language to another.
- **Summarizer**: Summarizes the code to highlight key functionalities.

## Demo

**Video will be added soon**

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Before running C-DOTS, you will need an OpenAI API key if the project utilizes OpenAI's services. You can obtain an API key by registering on the OpenAI platform.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/C-DOTS.git
```

2. Navigate to the cloned directory:

```bash
cd C-DOTS
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key in [api.py](./api.py#L4) files.

## Usage

Run the application by executing the main Python script:

```bash
python app.py
```

## Dependencies

- OpenAI API
- PyQt5
- Other dependencies listed in `requirements.txt`

## Contributing

We welcome contributions to enhance and improve [C-DOTS](https://github.com/SusheelThapa/C-DOTS)! Feel free to submit issues, feature requests, or pull requests. Please adhere to our Code of Conduct.

## License

This project is licensed under the [MIT License](/LICENSE).
