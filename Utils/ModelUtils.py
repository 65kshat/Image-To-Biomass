import cv2
import torch
import torch.nn as nn
import numpy as np

from PIL import Image #type: ignore

from torchvision import models #type: ignore
import torchvision.transforms as transforms #type: ignore

IMAGE_HEIGHT = 256
IMAGE_WIDTH = 512

TARGET_COLUMNS = ["Dry Clover (g)", "Dry Dead (g)", "Dry Green (g)", "Dry Total (g)", "GDM (g)"] #type: ignore

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.Resize((IMAGE_HEIGHT, IMAGE_WIDTH)),
    transforms.ToTensor(),

    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def build_model():

    weights = models.EfficientNet_B3_Weights.DEFAULT
    model = models.efficientnet_b3(weights = weights)

    in_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(0.30),
        nn.Linear(in_features, 512),
        nn.ReLU(),

        nn.Dropout(0.20),
        nn.Linear(512, 128),
        nn.ReLU(),

        nn.Linear(128, len(TARGET_COLUMNS))
    )

    return model


def load_model(model_path):
    model = build_model()
    model.load_state_dict(
        torch.load(model_path, map_location=DEVICE))

    model.to(DEVICE)
    model.eval()

    return model


def preprocess_image(image):
    image = image.convert("RGB")
    tensor = transform(image)
    tensor = tensor.unsqueeze(0)
    tensor = tensor.to(DEVICE)

    return tensor


def predict(model, image):
    input_tensor = preprocess_image(image)

    with torch.no_grad():
        prediction = model(input_tensor)

    prediction = prediction.squeeze().cpu().numpy()

    results = {}

    for label, value in zip(TARGET_COLUMNS, prediction):
        results[label] = round(float(value), 2)

    return results


PROJECT_INFORMATION = {

    "Model": "EfficientNet-B3",
    "Task": "Multi-Output Image Regression",
    "Training Images": 357,
    "Validation Images": 72,
    "Epochs": 50,
    "Image Size": "256 × 512",
    "Framework": "PyTorch",
    "Explainability": "Manual Grad-CAM"
}


def generate_gradcam(model, image, target_index):

    activations = None
    gradients = None

    def forward_hook(module, input, output):
        nonlocal activations
        activations = output

    def backward_hook(module, grad_input, grad_output):
        nonlocal gradients
        gradients = grad_output[0]

    target_layer = model.features[-1][0]
    forward_handle = target_layer.register_forward_hook(forward_hook)

    backward_handle = target_layer.register_full_backward_hook(backward_hook)

    rgb_image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    rgb_image = np.array(rgb_image).astype(np.float32) / 255.0
    input_tensor = preprocess_image(image)

    output = model(input_tensor)
    model.zero_grad()
    output[0, target_index].backward()

    weights = torch.mean(gradients, dim=(2, 3), keepdim=True)
    cam = torch.sum(weights * activations, dim=1)
    cam = torch.relu(cam)

    cam = cam.squeeze()
    cam = cam.detach()
    cam = cam.cpu().numpy()

    cam = cam - cam.min()
    cam = cam / (cam.max() + 1e-8)

    heatmap = cv2.resize(cam, (IMAGE_WIDTH, IMAGE_HEIGHT))
    heatmap_color = np.uint8(255 * heatmap)
    heatmap_color = cv2.applyColorMap(heatmap_color, cv2.COLORMAP_JET)
    heatmap_color = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2RGB)

    overlay = cv2.addWeighted(np.uint8(rgb_image * 255), 0.60, heatmap_color, 0.40, 0)
    forward_handle.remove()
    backward_handle.remove()

    return heatmap_color, overlay