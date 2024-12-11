import math

PreExponentialFactors = {
    'Fresh Apple': 645092.1348576404, 'Fresh Banana': 15370.169119416576, 'Fresh Bellpepper': 23330.754782432436, 
    'Fresh Cucumber': 277.94296916110966, 'Fresh Grapes': 23330.754782432436, 'Fresh Indian Green Chile': 23330.754782432436, 
    'Fresh Mango': 277.94296916110966, 'Fresh Orange': 5.995771324920545, 'Fresh Potato': 295.3274908449173, 
    'Fresh Tomato': 15370.169119416576, 'Moderate Apple': 15370.169119416576, 'Moderate Banana': 11139.41897966447, 
    'Moderate Bell Pepper': 113.07685698928096, 'Moderate Cucumber': 3494.564827089312, 'Moderate Grapes': 440004.8432500969, 
    'Moderate Indian Green Chile': 113.07685698928096, 'Moderate Mango': 208.10538328031532, 'Moderate Orange': 277.94296916110966, 
    'Moderate Potato': 1747.282413544656, 'Moderate Tomato': 440004.8432500969
}

ActivationEnergies = {
    'Fresh Apple': 38867.22294049396, 'Fresh Banana': 27885.777266933837, 'Fresh Bellpepper': 29754.351047873723, 
    'Fresh Cucumber': 18772.9053743136, 'Fresh Grapes': 29754.351047873723, 'Fresh Indian Green Chile': 29754.351047873723, 
    'Fresh Mango': 18772.9053743136, 'Fresh Orange': 10981.445673560118, 'Fresh Potato': 20641.479155253488, 
    'Fresh Tomato': 27885.777266933837, 'Moderate Apple': 27885.777266933837, 'Moderate Banana': 24816.431036967108, 
    'Moderate Bell Pepper': 15156.397555273734, 'Moderate Cucumber': 22947.857256027222, 'Moderate Grapes': 33929.302929587335, 
    'Moderate Indian Green Chile': 15156.397555273734, 'Moderate Mango': 16191.564734321395, 'Moderate Orange': 18772.9053743136, 
    'Moderate Potato': 22947.857256027222, 'Moderate Tomato': 33929.302929587335
}

def calculate_rate_constant(Ea, A, T):
    R = 8.314  # Universal gas constant in J/(mol*K)
    return A * math.exp(-Ea / (R * T))

def predict_shelf_life(predicted_class, temperature):
    Ea = ActivationEnergies[predicted_class]
    A = PreExponentialFactors[predicted_class]
    k = calculate_rate_constant(Ea, A, temperature)
    return 1 / k
