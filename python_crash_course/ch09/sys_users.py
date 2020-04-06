from users import User
from admin import Admin

ellie = User('ellie', 'maguire', '14', '07/07/2005', 'ellie.maguire@testdomain.com', 'cookstown')
ellie.describe_user()
ellie.greet_user()

print("\n")

nathan = User('nathan', 'colhoun', '34', '01/011984', 'nathan@natedogg.com', 'carrick')
nathan.describe_user()
nathan.greet_user()

admin = Admin('admin', 'admin', 'N/A', 'N/A', 'admin@test.com', 'N/A')
admin.describe_user()
admin.show_privileges()
print("-----------------------------------------------------------")
admin.privileges.append('update')
admin.show_privileges()