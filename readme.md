```markdown
# AI_ANYTIME Tutorial
This Repository was made following a tutorial posted on YouTube by the channel [ai_anytime](https://www.youtube.com/@AIAnytime). I included a Dockerfile, a Makefile and poetry package versioning.

## Overview
This is a Python application that utilizes Generative AI to answer questions about PDF documents. It is powered by the Hugging Face Transformers library and other language processing tools. The application is Dockerized for easy deployment.

## Docker Setup
To use this application with Docker, follow these steps:

### Build the Docker Image
Build the Docker image using the provided Dockerfile:
```bash
make build
```

### Run the Application
Run the Docker container to launch the PDF search application:
```bash
make run
```
This command will start the application and expose it on port 8501.

### Access the Application
Access the application by opening a web browser and navigating to `http://localhost:8501`.

## Dependencies
This project relies on various Python libraries and models, including:

- Streamlit
- Hugging Face Transformers
- SentenceTransformer
- PDFMiner

You can find the full list of dependencies in the `pyproject.toml` and `requirements.txt` files.

## Configuration
The application's configuration settings can be found in `constants.py` and `CHROMA_SETTINGS`.

## License
This project is distributed under the [MIT License](LICENSE.md).

## Acknowledgments
- The project uses state-of-the-art NLP models from Hugging Face.
- It makes use of PDFMiner for PDF document processing.

## About
This project is part of the "AI Anytime Open Source" initiative. Feel free to contribute, report issues, or provide feedback.
```
