import gradio as gr
import cv2
from detect import detect_objects


def detect(image):

    # Save uploaded image
    input_path = "uploads/input.jpg"
    cv2.imwrite(input_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Detect objects
    output_image, counts = detect_objects(input_path)

    # Convert image for Gradio
    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

    # Create output text
    output_text = ""

    total = 0

    for name, count in counts.items():
        output_text += f"{name} : {count}\n"
        total += count

    output_text += f"\nTotal Objects : {total}"

    return output_image, output_text


demo = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="numpy", label="Upload Image"),
    outputs=[
        gr.Image(label="Detected Image"),
        gr.Textbox(label="Detected Objects")
    ],
    title="AI Vision Detector",
    description="Upload any image and detect objects."
)

demo.launch()