# Indian PII Detection System

## Overview

This project implements a hybrid **PII (Personally Identifiable Information) detection system** tailored for Indian data. It combines:
- Transformer-based Named Entity Recognition (NER) models (HuggingFace)
- Custom regex patterns for Indian-specific PII (Aadhaar, PAN, phone numbers, etc.)

Additionally, it provides an interactive **Streamlit web interface** that highlights detected PII in real-time and requires user acknowledgment before submission.

## Features

- Supports detection of names, phone numbers, emails, Aadhaar, PAN, Voter ID, Passport numbers, GSTIN, IFSC, PIN codes, and more.
- Combines regex and NER for robust and accurate detection.
- Real-time PII highlighting with types and tooltips.
- User consent workflow before submission.
- Dockerized for easy deployment and consistency.

## Tech Stack

- Python 3.10+
- HuggingFace Transformers (`pipeline` API)
- Streamlit for UI
- Regex for structured PII
- Docker for containerization

## Getting Started

### Prerequisites

- Python 3.10+
- `pip`
- Docker (optional, for containerized deployment)

### Installation (Local without Docker)

1. Clone the repo:
   ```
   git clone https://github.com//.git
   cd 
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. Open [http://localhost:8501](http://localhost:8501) in your browser.

### Running with Docker

1. Build the Docker image:
   ```
   docker build -t pii-streamlit-app .
   ```

2. Run the container mapping port 8501:
   ```
   docker run -p 8501:8501 pii-streamlit-app
   ```

3. Access the app at [http://localhost:8501](http://localhost:8501)

4. To stop the container:
   - Press `CTRL+C` in terminal if running in foreground, or
   - Use `docker stop ` if running detached

### Notes

- The app uses a HuggingFace transformer model; the first run might download the model weights.
- Regex patterns are customized for Indian PII formats and can be extended.
- Designed for production readiness with modular code and consent workflows.
- Docker helps isolate dependencies and simplifies deployment.

## Project Structure

```
├── app.py            # Main Streamlit app code
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker build instructions
├── README.md         # This file
└── .gitignore        # To ignore unnecessary files in git
```

## Extending the Project

- Add more regex patterns for other Indian PII types.
- Fine-tune or swap out NER models for improved Indian/NLP support.
- Integrate document/PDF upload and processing.
- Add anonymization/redaction pipelines.
- Deploy on cloud platforms with authentication layers.

## References

- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

_Developed by  – a robust AI-powered PII detection project tailored for Indian data privacy and compliance._

```
