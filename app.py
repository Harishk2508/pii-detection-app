import streamlit as st
import re
from transformers import pipeline

# 1. Set up models and regex patterns
ner_pipe = pipeline("ner", model="Jean-Baptiste/roberta-large-ner-english",
                    aggregation_strategy="simple", framework="pt")

INDIA_REGEX_PATTERNS = {
    "Indian Phone Number": r"\b(?:\+91[\-\s]?|0)?[6-9]\d{9}\b",
    "Aadhaar Number": r"\b\d{4}\s\d{4}\s\d{4}\b|\b\d{12}\b",
    "PAN Number": r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",
    "Voter ID": r"\b([A-Z]{3}[0-9]{7})\b",
    "Passport Number": r"\b([A-Z]{1}-?\d{7}|[A-Z]{2}\d{7})\b",
    "GSTIN": r"\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}\b",
    "Indian Bank IFSC": r"\b[A-Z]{4}0[A-Z0-9]{6}\b",
    "Indian PIN Code": r"(?i)\b(?:PIN|Pin|Post|Postal|Postal Code|PIN Code)[:\- ]?\s*[1-9][0-9]{5}\b",
    "Email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "URL": r"http[s]?://[^\s]+|www\.[^\s]+",
    "Credit Card": r"\b(?:\d[ -]*?){13,16}\b",
}


def extract_regex_entities(text):
    results = []
    for label, pattern in INDIA_REGEX_PATTERNS.items():
        for match in re.finditer(pattern, text):
            results.append({
                "label": label,
                "value": match.group(),
                "start": match.start(),
                "end": match.end()
            })
    return results

def extract_ner_entities(text):
    entity_map = {"PER": "Name", "ORG": "Organization", "LOC": "Address", "MISC": "Other"}
    entities = ner_pipe(text)
    results = []
    for e in entities:
        label = entity_map.get(e.get("entity_group"), e.get("entity_group"))
        results.append({
            "label": label,
            "value": text[e["start"]:e["end"]],
            "start": e["start"],
            "end": e["end"]
        })
    return results

def highlight_text(text, spans):
    spans = sorted(spans, key=lambda x: x['start'])
    curr = 0
    result = ""
    for span in spans:
        s, e = span['start'], span['end']
        if s > curr:
            result += text[curr:s]
        result += f"<span style='background-color:#ffdddd;color:#d00000;' title='{span['label']}'>{text[s:e]}</span>"
        curr = e
    result += text[curr:]
    return result

# 2. Streamlit UI
st.title("Indian PII Detection Demo ⚠️")
st.write("Type or paste your text. PII will be detected and highlighted in real-time.")

text = st.text_area("Your text:", height=200)

# 3. Real-time detection and highlighting
if text:
    regex_entities = extract_regex_entities(text)
    ner_entities = extract_ner_entities(text)
    all_entities = regex_entities + ner_entities

    if all_entities:
        unique_spans = {(e['start'], e['end']): e for e in all_entities}.values()
        html_text = highlight_text(text, list(unique_spans))
        st.markdown(html_text, unsafe_allow_html=True)
        st.warning("PII detected! Please review before submitting.")
    else:
        st.success("No PII detected.")

    # 4. Submit logic with consent
    if st.button("Submit"):
        if all_entities:
            if st.checkbox("I acknowledge the detected PII and wish to proceed."):
                st.success("Submission complete! (PII detected, user consented)")
            else:
                st.error("Submission blocked. Please acknowledge and consent to proceed.")
        else:
            st.success("No PII detected -- submission complete!")

else:
    st.info("Enter some text to begin PII detection.")

# Add further logic for Docker, PDF/docx input, API, etc., as next steps.
