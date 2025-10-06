
import streamlit as st
from PIL import Image
import numpy as np
import io

# TensorFlow / Keras MobileNetV2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as kimage

@st.cache_resource
def load_model():
    model = MobileNetV2(weights="imagenet")
    return model

def predict_image(img: Image.Image, model, top=5):
    # MobileNetV2 expects 224x224
    img_resized = img.convert("RGB").resize((224, 224))
    x = kimage.img_to_array(img_resized)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=top)[0]  # list of tuples
    # decode_predictions returns tuples like (class_id, class_name, prob)
    results = [{"id": cid, "label": name, "probability": float(prob)} for cid, name, prob in decoded]
    return results

def main():
    st.set_page_config(page_title="Resim Tanıma (ImageNet)", layout="centered")
    st.title("📷 Resim Tanıma — Basit Python Projesi")
    st.markdown(
        "Fotoğraf yükle, önceden eğitilmiş MobileNetV2 modeli ile fotoğrafın ne olduğuna dair en olası sonuçları gör."
    )

    model = load_model()

    uploaded = st.file_uploader("Bir fotoğraf yükleyin (jpg, png)", type=["jpg", "jpeg", "png"])
    if uploaded is not None:
        try:
            image_data = uploaded.read()
            img = Image.open(io.BytesIO(image_data))
            st.image(img, caption="Yüklenen görüntü", use_column_width=True)

            with st.spinner("Tahmin yapılıyor..."):
                results = predict_image(img, model, top=5)

            st.subheader("Tahminler (ImageNet etiketleri)")
            for i, r in enumerate(results, start=1):
                st.write(f"{i}. **{r['label']}** — {r['probability']*100:.2f}%")
            
            st.markdown(
                "⚠️ Not: Bu model **ImageNet** sınıflarıyla eğitildi. Yani sonuçlar İngilizce sınıf isimleri olur ve her zaman %100 doğru olmayabilir."
            )

        except Exception as e:
            st.error(f"Resim işlenirken hata: {e}")

    st.sidebar.title("İpuçları / Geliştirme fikirleri")
    st.sidebar.markdown(
        """
- Daha doğru sonuç için transfer learning (kendi verinizle yeniden eğitme).
- Hugging Face `CLIP` veya ViT modelleri ile zero-shot etiketleme.
- Google Vision / AWS Rekognition gibi servislerle daha geniş sınıflar ve etiketler.
- Türkçe etiket istiyorsanız, decode sonuçlarını sözlükle eşleştirip Türkçe'ye çevirebilirsiniz.
"""
    )

if __name__ == "__main__":
    main()