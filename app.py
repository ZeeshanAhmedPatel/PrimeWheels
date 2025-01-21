from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='template')

# Dictionary to store user bids
bids = {"User 1": None, "User 2": None, "User 3": None, "User 4": None}
# Dictionary to store bids for Car 2
bids2 = {"User 1": None, "User 2": None, "User 3": None, "User 4": None}

# Route for Car 2 bidding page
@app.route("/bid2")
def bid2():
    return render_template("bid2.html", bids=bids2)


@app.route("/bid")
def bid():
    return render_template("bid.html", bids=bids)


#Submit Bit Logic Car 1

@app.route("/submit_bid", methods=["POST"])
def submit_bid():
    user = request.form.get("user")
    try:
        bid = float(request.form.get("bid"))
    except ValueError:
        return jsonify({"success": False, "message": "Invalid bid amount."})

    # Get the current highest bid
    highest_bid = max(filter(None, bids.values()), default=0)

    if bid <= highest_bid:
        return jsonify({"success": False, "message": f"Your bid must be greater than ${highest_bid:.2f}."})

    # Update the user's bid
    bids[user] = bid

    return jsonify({
        "success": True,
        "message": f"Bid of ${bid} placed by {user}!",
        "bids": bids
    })


# Submit bid logic for Car 2
@app.route("/submit_bid2", methods=["POST"])
def submit_bid2():
    user = request.form.get("user")
    try:
        bid = float(request.form.get("bid"))
    except ValueError:
        return jsonify({"success": False, "message": "Invalid bid amount. Please enter a valid number."})

    # Get the current highest bid for Car 2
    highest_bid = max(filter(None, bids2.values()), default=0)

    if bid <= highest_bid:
        return jsonify({"success": False, "message": f"Your bid must be greater than ${highest_bid:.2f}."})

    # Update the user's bid for Car 2
    bids2[user] = bid

    return jsonify({
        "success": True,
        "message": f"Bid of ${bid} placed by {user} on Car 2!",
        "bids": bids2
    })

#Logic for Auto Bid 1

@app.route("/auto_bid", methods=["POST"])
def auto_bid():
    user = request.form.get("user")
    if user:
        # Get the current highest bid after all updates
        highest_bid = max(filter(None, bids.values()), default=0)
        # Determine the next bid (increment by 50)
        next_bid = round(highest_bid + 50, 2)
        bids[user] = next_bid
        return jsonify({
            "success": True,
            "message": f"Auto-bid of ${next_bid} placed by {user}!",
            "bids": bids
        })
    return jsonify({"success": False, "message": "Invalid user!"})

# Auto-bid logic for Car 2
@app.route("/auto_bid2", methods=["POST"])
def auto_bid2():
    user = request.form.get("user")
    if user:
        # Get the current highest bid for Car 2
        highest_bid = max(filter(None, bids2.values()), default=0)
        # Determine the next bid (increment by 50)
        next_bid = round(highest_bid + 50, 2)
        bids2[user] = next_bid
        return jsonify({
            "success": True,
            "message": f"Auto-bid of ${next_bid} placed by {user} on Car 2!",
            "bids": bids2
        })
    return jsonify({"success": False, "message": "Invalid user!"})

#_________________________________________Navigation Pages Routes_______________________

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/featured')
def featured():
    return render_template('featured.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/bid')
# def bid():
#     return render_template('bid.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__=='__main__':
    app.run(debug = True)