amazon_return_policy = {
    "Return Window": {
        "Most items": "30 days of delivery",
        "Exceptions": {
            "Digital books": "7 days",
            "Digital textbooks, workbooks, and other educational content": "7 days",
            "Songs or albums": "7 days",
            "Apple Brand products and Boost Infinite Brand products": "15 days",
            "Amazon Haul store items over $3": "15 days",
            "Amazon Renewed products in 'Acceptable', 'Good', or 'Excellent' condition types": "90 days",
            "Most nonperishable Baby products": "90 days",
            "Amazon Birthday and/or Custom Gift List items purchased by someone other than the registry owner": "90 days",
            "Mattresses (excluding crib mattresses)": "90 days",
            "Amazon Wedding Registry items purchased by someone other than the registry owner": "180 days",
            "Amazon Renewed products in 'Premium' condition": "365 days",
            "Amazon Baby Registry items purchased by someone other than the registry owner": "365 days"
        }
    },
    "Items That You Can't Return": [
        "Perishables",
        "Products that may pose potential health and safety risks once sold",
        "Products with shipping restrictions",
        "Customized products made specifically for you",
        "Redeemable products",
        "Amazon Pharmacy products",
        "Pet medication products",
        "Certain digital products",
        "Automobiles",
        "Products listed as 'Final Sale'"
    ],
    "Refund Timeline": {
        "Description": [
            "A refund will be provided after we process your returned item at our Amazon or third-party seller facilities."
        ]
    },
    "Return Process": {
        "Steps": [
            {"Step 1": ["Go to Your Orders to display your recent orders.", {"Gift Return": ["Go to Return a Gift."]}]},
            {"Step 2": ["Choose the order and select Return or Replace Items."]},
            {"Step 3": ["Select the item that you want to return.", {"Reason for return menu": ["Select an option from the Reason for return menu."]}]},
            {"Step 4": ["Choose how to process your return.", {"Refund or replacement": ["If applicable, select to issue a refund or replacement."]}]},
            {"Step 5": ["Submit a return request for items sold from an Amazon seller.", {"Seller review": ["The Amazon seller reviews return requests before issuing a refund or replacement."]}]},
            {"Step 6": ["Request an A-to-z Guarantee Refund if you don't receive a response within two business days."]},
            {"Step 7": ["Select your preferred return method."]},
            {"Step 8": ["Print your return label and return authorization.", {"Return label instructions": ["Add your return label (if applicable) and package your items for return.", {"Important information about return labels": [{"Description": ["Each return label is assigned to a specific return.", "To receive the correct refund, don't include items from multiple orders or shipments in the same box."]}]}]}]},
            {"Step 9": ["Complete a label-free, box-free return location after initiating your return through Your Orders.", {"QR code instructions": [{"Description": ["After completing the steps, you’ll receive a QR code.", "Bring it to the drop-off location with the item that you want to return.", "You don’t have to package your item in a shipping box."]}]}]},
            {"Step 10": ["Erase any personal information from items that you’re returning, such as laptops, cameras, and electronic devices."]},
            {"Step 11": ["Add comments to your return request.", {"Comment instructions": [{"Description": ["When you request a return, you will find a box where you can describe any issues or reasons why you are returning the item.", "Make sure to leave accurate and detailed information so we can improve your customer experience.", {"Second comment box instructions": [{"Description": ["You may receive a second comment box to clarify your feedback in the first comment box."]}]}]}]}]},
            {"Step 12": ["Charge for items you are expected to return.", {"Charge instructions": [{"Description": ["If you have already received a refund, you will be charged if the item is not sent back to us.", "If you have already sent it back, we will reverse the charge when we process the return."]}]}]}
        ]
    }
}

def get_retail_return_policy():
    return amazon_return_policy