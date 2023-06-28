Stock App Tasks

- Develop the Models in the given ERD and create relations
- Bonus Task: Develop a model GETTER property to calculate the total price in Sales and Purchase models.
- Develop Serializers
- Bonus Task: Develop a validator for SalesSerializer to validate you have enough stock to fulfill that sale.

- Create Views
- CategoryView
- apply a filter and search for the name
- Bonus Task: If the name parameter exists in the URL request then:
  Develop a different serializer for category that also displays the product details in that category
  Apply this serializer rather than the basic CategorySerializer.

FirmView

- apply a filter for the name, phone, and address fields
- apply a search for the name
- Add permission as IsAuthenticated
  Bonus Task: (Naming this bonus task as DjangoModelPermissionsTask and will ask this task again for the other following views)
  Define groups in Admin Dashboard
  Give Custom Permission to groups to access related models
  Apply permission as DjangoModelPermissions

BrandView
Add permission as IsAuthenticated
Bonus Task: DjangoModelPermissionsTask explained above

ProductView

PurchaseView
Add permission as IsAuthenticated
Bonus Task: DjangoModelPermissionsTask explained above
Automatically add the current user as the user field
When a purchase happens also update the current stock in the Product table
Bonus Task:
When a purchase record is updated also update the current stock in the Product table
When a purchase record is deleted also update the current stock in the Product table

SalesView:
Add permission as IsAuthenticated
Bonus Task: DjangoModelPermissionsTask explained above
Automatically add the current user as the user field
When a sales happens also update the current stock in the Product table
Bonus Task:
When a sales record is updated also update the current stock in the Product table
When a sales record is deleted also update the current stock in the Product table

Create URLs

Create Account_app and handle authorization
