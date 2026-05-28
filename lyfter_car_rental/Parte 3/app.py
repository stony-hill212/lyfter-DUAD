from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify
from possum import get_connection

app= Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data=request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        INSERT INTO lyfter_car_rental.users
        (
            full_name,
            email,
            username,
            password,
            account_status,
            DOB
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values=(
        data["full_name"],
        data["email"],
        data["username"],
        data["password"],
        data["account_status"],
        data["DOB"]
    )
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User created successfully"}), 201

@app.route("/vehicles", methods=["POST"])
def create_vehicle():
    data=request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        INSERT INTO lyfter_car_rental.vehicles
        (
            make,
            model,
            year,
            vehicle_condition,
            vehicle_status
        )
        VALUES(%s, %s, %s, %s, %s)
    """
    values=(
        data["make"],
        data["model"],
        data["year"],
        data["vehicle_condition"],
        data["vehicle_status"]
    )
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Vehicle created successfully"}), 201

@app.route("/rentals", methods=["POST"])
def create_rental():
    data=request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    rental_query= """
        INSERT INTO lyfter_car_rental.rentals
        (
            user_id,
            vehicle_id,
            rental_status
        )
        VALUES(%s, %s, %s)
    """
    rental_values=(
        data["user_id"],
        data["vehicle_id"],
        data["rental_status"]
    )
    cursor.execute(rental_query, rental_values)
    update_vehicle= """
        UPDATE lyfter_car_rental.vehicles
        SET vehicle_status= 'rented'
        WHERE vehicle_id= %s
    """
    cursor.execute(update_vehicle, (data["vehicle_id"],))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Rental registration created successfully"}), 201

@app.route("/vehicles/<int:vehicle_id>", methods=["PUT"])
def update_vehicle_status(vehicle_id):
    data=request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        UPDATE lyfter_car_rental.vehicles
        SET vehicle_status= %s
        WHERE vehicle_id= %s
    """
    cursor.execute(query, (data["vehicle_status"], vehicle_id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Vehicle updated"}), 200

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user_status(user_id):
    data=request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        UPDATE lyfter_car_rental.users
        SET account_status= %s
        WHERE user_id= %s
    """
    cursor.execute(query, (data["account_status"], user_id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User updated"}), 200

@app.route("/rentals/<int:rental_id>", methods=["PUT"])
def update_rental_status(rental_id):
    data= request.json
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        UPDATE lyfter_car_rental.rentals
        SET rental_status= %s
        WHERE rental_id= %s
        RETURNING vehicle_id, rental_status
    """
    cursor.execute(query, data["rental_status"], rental_id)
    result=cursor.fetchone()
    vehicle_id=result[0]
    rental_status=result[1]
    if rental_status=="completed":
        vehicle_query= """
            UPDATE lyfter_car_rental.vehicles
            SET vehicle_status= 'available'
            WHERE vehicle_id= %s
        """
        cursor.execute(vehicle_query, (vehicle_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Rental status updated"}), 200

@app.route("/users/<int:user_id>/overdue", methods=["PUT"])
def mark_overdue(user_id):
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= """
        UPDATE lyfter_car_rental.users
        SET overdue= TRUE
        WHERE user_id= %s
    """
    cursor.execute(query, (user_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User marked overdue"}), 200

@app.route("/users", methods=["GET"])
def get_users():
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= "SELECT * FROM lyfter_car_rental.users WHERE 1=1"
    filters=request.args
    for key, value in filters.items():
        query+= f" AND {key}= %s"
    cursor.execute(query, tuple(filters.values()))
    users=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users), 200

@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= "SELECT * FROM lyfter_car_rental.vehicles WHERE 1=1"
    filters=request.args
    for key, value in filters.items():
        query+= f" AND {key}= %s"
    cursor.execute(query, tuple(filters.values()))
    vehicles=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(vehicles), 200

@app.route("/rentals", methods=["GET"])
def get_rentals():
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    query= "SELECT * FROM lyfter_car_rental.rentals WHERE 1=1"
    filters=request.args
    for key, value in filters.items():
        query+= f" AND {key}= %s"
    cursor.execute(query, tuple(filters.values()))
    rentals=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rentals), 200

@app.route("/vehicles", methods=["DELETE"])
def delete_vehicles():
    connection=get_connection()
    cursor=connection.cursor(cursor_factory=RealDictCursor)
    filters=request.args
    query= """DELETE FROM lyfter_car_rental.vehicles WHERE 1=1"""
    for key, value in filters.items():
        query+= f" AND {key}= %s"
    cursor.execute(query, tuple(filters.values()))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Vehicle deleted"}), 200

if __name__=="__main__":
    app.run(debug=True)
