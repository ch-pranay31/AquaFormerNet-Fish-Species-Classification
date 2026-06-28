from flask import Flask, render_template, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
import os
from aquaformer_model import AquaFormerNet

app = Flask(__name__)

device = torch.device("cpu")


from torchvision import datasets

dataset = datasets.ImageFolder("fish_dataset/train")
classes = dataset.classes

print("Class order:", classes)

model = AquaFormerNet(len(classes))
model.load_state_dict(torch.load("models/aquaformer_epoch_15.pth", map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

fish_info = {

"Type 1 Pomfret":{
"name":"Pomfret",
"scientific":"Pampus argenteus",
"category":"Marine Fish",
"protein":"18 g",
"fat":"3 g",
"omega3":"High",
"calories":"120 kcal",
"habitat":"Indian Ocean coastal waters",
"taste":"Mild and slightly sweet",
"price":"₹400–₹900 per kg",
"availability":"Andhra Pradesh, Kerala, Tamil Nadu, Goa",
"benefits":[
"Improves heart health due to omega-3 fatty acids",
"Supports brain development",
"Helps muscle growth",
"Improves immune system"
],
"disadvantages":[
"Can increase cholesterol if fried excessively",
"Seafood allergy risk in sensitive individuals"
],
"who_should_eat":[
"Children for brain development",
"Athletes for protein intake",
"Pregnant women for omega-3"
],
"who_should_avoid":[
"People allergic to seafood",
"People on strict cholesterol-controlled diet"
],
"best_cooking_methods":[
"Grilled",
"Fried",
"Fish curry",
"Tandoori pomfret"
]
},

"Type 2 Mackerel":{
"name":"Mackerel",
"scientific":"Rastrelliger kanagurta",
"category":"Marine Fish",
"protein":"20 g",
"fat":"5 g",
"omega3":"Very High",
"calories":"140 kcal",
"habitat":"Warm coastal waters",
"taste":"Strong rich flavor",
"price":"₹250–₹500 per kg",
"availability":"Kerala, Maharashtra, Karnataka, Goa",
"benefits":[
"Very high omega-3 for heart health",
"Improves brain function",
"Helps reduce inflammation",
"Supports healthy skin"
],
"disadvantages":[
"Contains purines which may worsen gout",
"Can spoil quickly if not refrigerated"
],
"who_should_eat":[
"Adults for heart health",
"Elderly people",
"Athletes"
],
"who_should_avoid":[
"People with gout",
"People allergic to seafood"
],
"best_cooking_methods":[
"Grilled",
"Pan fried",
"Spicy fish curry"
]
},

"Type 3 Black Snapper":{
"name":"Black Snapper",
"scientific":"Lutjanus spp.",
"category":"Marine Fish",
"protein":"19 g",
"fat":"2 g",
"omega3":"Moderate",
"calories":"110 kcal",
"habitat":"Coral reefs and coastal waters",
"taste":"Firm texture with mild taste",
"price":"₹600–₹1200 per kg",
"availability":"Andhra Pradesh, Tamil Nadu, West Bengal",
"benefits":[
"Lean protein source",
"Good for muscle development",
"Contains vitamin D",
"Supports bone strength"
],
"disadvantages":[
"Possible mercury accumulation if eaten frequently"
],
"who_should_eat":[
"Athletes",
"Adults needing protein",
"Elderly for bone health"
],
"who_should_avoid":[
"Pregnant women should limit consumption"
],
"best_cooking_methods":[
"Grilled",
"Steamed",
"Baked"
]
},

"Type 4 Indian Carp":{
"name":"Indian Carp",
"scientific":"Catla catla",
"category":"Freshwater Fish",
"protein":"17 g",
"fat":"2 g",
"omega3":"Moderate",
"calories":"115 kcal",
"habitat":"Freshwater rivers and ponds",
"taste":"Soft and slightly sweet",
"price":"₹200–₹350 per kg",
"availability":"Telangana, Andhra Pradesh, West Bengal",
"benefits":[
"Rich protein for growth",
"Improves bone health",
"Good source of calcium",
"Easily digestible"
],
"disadvantages":[
"Contains many small bones",
"Requires careful cleaning before cooking"
],
"who_should_eat":[
"Children",
"Adults",
"People recovering from illness"
],
"who_should_avoid":[
"People who dislike bony fish"
],
"best_cooking_methods":[
"Fish curry",
"Fried",
"Steamed"
]
},

"Type 5 Prawn":{
"name":"Prawn",
"scientific":"Penaeus monodon",
"category":"Shellfish",
"protein":"24 g",
"fat":"1 g",
"omega3":"Moderate",
"calories":"99 kcal",
"habitat":"Coastal waters and aquaculture farms",
"taste":"Sweet and delicate",
"price":"₹400–₹800 per kg",
"availability":"Coastal India",
"benefits":[
"Very high protein",
"Rich in selenium",
"Supports muscle building",
"Boosts metabolism"
],
"disadvantages":[
"High cholesterol if eaten excessively",
"Allergy risk for shellfish-sensitive people"
],
"who_should_eat":[
"Fitness enthusiasts",
"Athletes",
"People on high-protein diets"
],
"who_should_avoid":[
"People allergic to shellfish"
],
"best_cooking_methods":[
"Prawn curry",
"Grilled prawns",
"Butter garlic prawns"
]
},

"Type 6 Pink Perch":{
"name":"Pink Perch",
"scientific":"Nemipterus japonicus",
"category":"Marine Fish",
"protein":"18 g",
"fat":"2 g",
"omega3":"Moderate",
"calories":"115 kcal",
"habitat":"Coastal waters of Indian Ocean",
"taste":"Mild and slightly sweet",
"price":"₹250–₹450 per kg",
"availability":"Kerala, Andhra Pradesh, Karnataka",
"benefits":[
"Low fat fish good for dieting",
"High quality protein",
"Improves heart health"
],
"disadvantages":[
"Spoils quickly if not refrigerated"
],
"who_should_eat":[
"Diet conscious people",
"Athletes"
],
"who_should_avoid":[
"People allergic to seafood"
],
"best_cooking_methods":[
"Grilled",
"Fried",
"Fish curry"
]
},

"Type 7 Indian Carp":{
"name":"Indian Carp (Rohu)",
"scientific":"Labeo rohita",
"category":"Freshwater Fish",
"protein":"17 g",
"fat":"2 g",
"omega3":"Moderate",
"calories":"110 kcal",
"habitat":"Rivers and lakes",
"taste":"Mild and tender",
"price":"₹200–₹350 per kg",
"availability":"Telangana, Andhra Pradesh, West Bengal",
"benefits":[
"High protein",
"Supports muscle growth",
"Easy to digest"
],
"disadvantages":[
"Many bones"
],
"who_should_eat":[
"Children",
"Adults"
],
"who_should_avoid":[
"People who dislike bony fish"
],
"best_cooking_methods":[
"Curry",
"Fried",
"Steamed"
]
},

"Type 8 Black Pomfret":{
"name":"Black Pomfret",
"scientific":"Parastromateus niger",
"category":"Marine Fish",
"protein":"19 g",
"fat":"4 g",
"omega3":"High",
"calories":"135 kcal",
"habitat":"Coastal waters",
"taste":"Rich flavor",
"price":"₹700–₹1500 per kg",
"availability":"Gujarat, Maharashtra, Andhra Pradesh",
"benefits":[
"Rich omega-3 fatty acids",
"Improves heart health",
"Supports brain function"
],
"disadvantages":[
"Expensive compared to other fish"
],
"who_should_eat":[
"Adults",
"Elderly"
],
"who_should_avoid":[
"People allergic to seafood"
],
"best_cooking_methods":[
"Grilled",
"Tandoori",
"Fried"
]
},

"Type 9 Tuna":{
"name":"Tuna",
"scientific":"Thunnus albacares",
"category":"Marine Fish",
"protein":"26 g",
"fat":"1 g",
"omega3":"Very High",
"calories":"132 kcal",
"habitat":"Deep ocean waters",
"taste":"Firm and meaty",
"price":"₹600–₹1200 per kg",
"availability":"Kerala, Tamil Nadu, Lakshadweep",
"benefits":[
"Extremely high protein",
"Excellent for muscle growth",
"Improves heart health",
"Boosts metabolism"
],
"disadvantages":[
"High mercury if consumed frequently"
],
"who_should_eat":[
"Athletes",
"Bodybuilders"
],
"who_should_avoid":[
"Pregnant women should limit consumption"
],
"best_cooking_methods":[
"Grilled tuna steak",
"Sushi",
"Pan seared"
]
}

}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['image']

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    img = Image.open(filepath).convert("RGB")
    img = transform(img).unsqueeze(0)

    with torch.no_grad():

        output = model(img)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        pred = torch.argmax(probabilities).item()

        result = classes[pred]

        confidence = probabilities[pred].item()

    info = fish_info.get(result, {})

    return jsonify({
    "prediction": result,
    "confidence": round(confidence*100,2),
    "details": info
    })


if __name__ == "__main__":
    app.run(debug=True)