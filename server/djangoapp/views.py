            if car.id == int(request.POST['car']):
                review_car = car  
        review = {}
        review["time"] = datetime.utcnow().isoformat()
        review["name"] = request.POST['name']
        review["dealership"] = dealer_id
        review["review"] = request.POST['content']
        review["purchase"] = was_purchased
        review["purchase_date"] = request.POST['purchasedate']
        review["car_make"] = review_car.make.name
        review["car_model"] = review_car.name
        review["car_year"] = review_car.year.strftime("%Y")
        json_payload = {}
        json_payload["review"] = review
        response = post_request(url, json_payload)
        return redirect("djangoapp:dealer_details", dealer_id=dealer_id)
