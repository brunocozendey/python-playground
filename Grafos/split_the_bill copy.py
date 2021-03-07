#!/usr/bin/python
import sys, getopt,json

def calculate_each_item(item):
    return item['amount']*item['price']

def calculate_total_amount(list):
    total = 0
    for item in list:
        total += calculate_each_item(item)
    return total

def divide_honestly(total_amount,amount_people):
    amount_per_cents = total_amount*100
    amount_per_person = amount_per_cents//amount_people
    total_amount_splitted = amount_per_person*amount_people
    amount_greater_values = int(amount_per_cents%amount_people)
    
    if total_amount_splitted != total_amount:
        return amount_per_person/100, (amount_per_person+1)/100, amount_greater_values
    else:
        return amount_per_person/100, amount_per_person/100, 0

def distribuir_valor_por_email(email_list,grocery_list):
    email_and_amount = {}
    valor_normal, rounded_value, amount_greater_values = divide_honestly(calculate_total_amount(grocery_list),len(set(email_list)))
    for email in email_list:
        email_and_amount[email]=valor_normal
    for value in range(amount_greater_values):
        email_and_amount[email_list[value]] = rounded_value
    return email_and_amount

def grocery_file_validate(groceryfile):
    if groceryfile != "":
        return True
    else:
        raise ValueError("Grocery list is empty!")

def email_file_validate(emailfile):
    if emailfile != "":
        return True
    else:
        raise ValueError("Email list is empty!")

def main(argv):
    groceryfile = ''
    emailfile = ''
    try:
       opts, _ = getopt.getopt(argv,"hgl:el:",["glfile=","elfile="])
    except getopt.GetoptError:
        print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
        print ('Please provide input files or -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('split_the_bill.py --gl <grocerylist.txt> --el <emaillist.txt>')
            sys.exit()
        elif opt in ("-gl", "--glfile"):
            groceryfile = arg
        elif opt in ("-el", "--elfile"):
            emailfile = arg
   
    try:
        mf = open(groceryfile, "r", encoding='utf-8')
        mf.seek(0)
        grocery_list = mf.read()
        print(grocery_list)
        if grocery_list == '':
            grocery_list = "[]"
        grocery_list_json = json.loads(grocery_list)
    except:
        raise FileNotFoundError('Grocery list not found!')
    finally:
        mf.close()

    try:
        ef = open(emailfile, "r", encoding='utf-8')
        ef.seek(0)
        email_list = ef.read().splitlines()
        if email_list == []:
            email_list = ["Total"]
    except:
        raise FileNotFoundError('Email list not found!')
    finally:
        ef.close()
    print(json.dumps(distribuir_valor_por_email(email_list,grocery_list_json)))    
'''
    try:
        if email_file_validate and grocery_file_validate:
                print(json.dumps(distribuir_valor_por_email(email_list,grocery_list_json)))
    except:
        print("{}")
'''
    

if __name__ == "__main__":
   main(sys.argv[1:])   