API Endpoints POST /add_cart/ - Add a product to the cart - http://127.0.0.1:8000/restapi/add_cart

GET /restapi/view_cart - View the user's cart, including total price - http://127.0.0.1:8000/restapi/view_cart

GET /restapi/view_product/ - List all products - http://127.0.0.1:8000/restapi/view_product

GET /restapi/view_users/ - Get a list of all users - http://127.0.0.1:8000/restapi/view_users

POST /restapi/register/ - Register a new user - http://127.0.0.1:8000/restapi/register

POST /restapi/login/ - Log in an existing user - http://127.0.0.1:8000/restapi/login


view_product

{
  "products": [
    {
      "id": 1,
      "Name": "Orange",
      "Description": "This is a sample",
      "Price": "20.90",
      "Image": "/media/media/products/orange.jpg"
    },
    {
      "id": 2,
      "Name": "Apple",
      "Description": "This is another sample",
      "Price": "40.00",
      "Image": "/media/media/products/apple.jpg"
    }
  ]
}
#balance have no output
