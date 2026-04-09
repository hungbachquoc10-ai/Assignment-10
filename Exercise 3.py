from flask import Flask, jsonify
app = Flask(__name__)
def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = is_prime(number)
    response = {
        "Number": number,
        "isPrime": result
    }
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)