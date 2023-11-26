from flask import Flask, request, jsonify

app = Flask(__name__)






@app.route('/', methods=['POST'])
def get_map_url():
    user_data = request.json
    
    # Pastikan user_data tidak kosong dan memiliki data koordinat yang diperlukan
    if user_data and 'latitude' in user_data and 'longitude' in user_data:
        latitude = user_data['latitude']
        longitude = user_data['longitude']
        
        # Membuat URL Google Maps dengan koordinat dinamis dari data pengguna
        url = f"https://www.google.com/maps/place/{latitude},{longitude}"
        
        return jsonify({'location': url})
    else:
        return jsonify({'error': 'Invalid data format or missing coordinates'}), 400

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify({
        'message': "Hello Users API"
    })


# Contoh data wisata untuk setiap lokasi
places_data = {
    "Jakarta": ["Monas", "Taman Mini Indonesia Indah", "Kota Tua"],
    "Bali": ["Pantai Kuta", "Tegalalang Rice Terrace", "Pura Tanah Lot"],
    "Yogyakarta": ["Candi Borobudur", "Candi Prambanan", "Keraton Yogyakarta"]
}

class RecommendationModel:
    def __init__(self):
        pass

    def recommend(self, user_data):
        location = user_data.get('location')
        preferences = user_data.get('preferences')

        if not location:
            return {'error': 'Location not provided'}, 400
        
        if location not in places_data:
            return {'error': 'Location not found'}, 404
        
        recommended_places = places_data[location]

        # Jika ada preferensi, filter rekomendasi berdasarkan preferensi
        #if preferences:
         #   recommended_places = [place for place in recommended_places if any(pref.lower() in place.lower() for pref in preferences)]

        return recommended_places

model = RecommendationModel()

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    user_data = request.json
    
    if not user_data:
        return jsonify({'error': 'No data received'}), 400
    
    recommended_places = model.recommend(user_data)
    
    return jsonify({'recommended_places': recommended_places})  

if __name__ == '__main__':
    app.run(debug=True)
