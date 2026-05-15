
import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import torch.nn.functional as F

LABELS = {0: "Normal", 1: "Depression", 2: "Anxiety", 3: "PTSD"}
LABEL_COLORS = {
    "Normal":     "🟢",
    "Depression": "🔵",
    "Anxiety":    "🟡",
    "PTSD":       "🔴"
}

@st.cache_resource
def load_model():
    tokenizer = BertTokenizer.from_pretrained("best_model_saved")
    model = BertForSequenceClassification.from_pretrained("best_model_saved")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

st.set_page_config(page_title="Mental Health Classifier", page_icon="🧠")
st.title("🧠 Mental Health Status Classifier")
st.write("Classify social media text into: **Normal, Depression, Anxiety, PTSD**")
st.markdown("---")

user_input = st.text_area("✍️ Enter a social media post:", height=180,
                           placeholder="e.g. I've been feeling really hopeless lately...")

if st.button("🔍 Classify"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            inputs = tokenizer(user_input, return_tensors="pt",
                               truncation=True, padding=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)[0]
            pred_id = torch.argmax(probs).item()
            pred_label = LABELS[pred_id]
            confidence = probs[pred_id].item() * 100

        st.markdown("---")
        st.subheader("Result:")
        st.markdown(f"### {LABEL_COLORS[pred_label]} Predicted Status: **{pred_label}**")
        st.markdown(f"**Confidence:** {confidence:.1f}%")
        st.markdown("#### Confidence across all classes:")
        for i, label in LABELS.items():
            st.progress(float(probs[i]), text=f"{label}: {probs[i]*100:.1f}%")
    else:
        st.warning("Please enter some text first.")

st.markdown("---")
st.caption("⚠️ This tool is for educational purposes only and is not a clinical diagnosis.")
