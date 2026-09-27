import json
import os
menu = ("1.Add Contact\n2.Show Contacts\n3.Search Contact\n4.Edit Contact\n5.Delete Contact\n6.Exit")
contact = [
    {
        "name" : "Sara",
        "phone" : "09123456781"
    },
    {
        "name" : "Reza" ,
        "phone" : "09351234567"
    },
    {
        "name" : "Faeze",
        "phone" : "09901234568"
    }
]
def add_contact():
    name_contact = input("Enter contact name :")
    phone_contact = input("Enter contact phone :")
    my_dic = {
        "name" : name_contact,
        "phone" : phone_contact
    }
    contact.append(my_dic)
    print("Contact added successfully !")
def show_contact() :
    if contact:
        for item in contact:
            print("Name:",item["name"])
            print("Phone:",item["phone"])
    else:
        print("No contacts found!")        
def search_contact():
    user_input = input("search...:") 
    found = False 
    if contact :
        for char in contact:
            if user_input.lower()  in char["name"].lower() :
                print("Name:",char["name"])
                print("Phone:",char["phone"])
                found = True    
        if not found :    
            print("Contact not found!") 
            return
    else:
        print("No contacts found!")    
def edit_contact(): 
    contact_name1  = input("Enter contact name to edit :")
    found = False 
    if contact:
        for cont in contact :
            if contact_name1.lower() == cont["name"].lower() :
                found = True
                edit_menu = ("1.Change name\n2.change phone\n3.Cancel")  
                print(edit_menu) 
                edit_input = input("Enter your choice :") 
                update = False
                if edit_input == "1" :
                    contact_name = input("Enter new contact name :")
                    cont["name"] = contact_name
                    update = True
                elif edit_input == "2":
                    contact_phone = input("Enter new contact phone :")
                    cont["phone"] = contact_phone
                    update = True
                if update :
                    print("Contact updated successfully! ")    
                elif edit_input == "3" :
                    return                
        if not found :
            print("contact not found!") 
            return       
    else:
        print("No contacts found!")    
def delete_contact():
    user_input = input("Enter contact name to delete :")
    found = False 
    if contact:
        for con in contact :
            if user_input.lower() == con["name"].lower() :
                contact.remove(con)
                print("Contact deleted successfully!")
                found = True
                break
        if not found :
            print("contact not found!")  
            return 
    else:
        print("No contacts found!")    
if os.path.exists("Contact_Management.json") :
    with open("Contact_Management.json","r") as file :  
        contact = json.load(file)   
else:
    with open("Contact_Management.json","w") as file :
            json.dump(contact ,file) 
def save_contacts() :
    with open("Contact_Management.json","w") as file :
            json.dump(contact ,file ,indent = 4) 
while True:
    print(menu)
    try:
        choice = int(input("Enter your choice :"))
    except ValueError:
        print("Enter a valid number!")  
        continue    
    if choice in range(1,7) :
        if choice == 1 :
            add_contact()
            save_contacts()
        elif choice == 2 :
            show_contact()
        elif choice == 3 :
            search_contact()   
        elif choice == 4 :
            edit_contact()
            save_contacts()  
        elif choice == 5 :
            delete_contact()
            save_contacts()
        elif choice == 6 :
            break  
    else:
        print("your choice must be between 1 to 6 !") 
        continue   
           
        

