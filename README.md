## LIVE API

USER REGISTRATION

https://safe-chamber-55286.herokuapp.com/rest-auth/registration/

`{
    "email": "tinahuang@gmail.com",
    "password1": "KindaTina",
    "password2": "KindaTina"
}`


https://safe-chamber-55286.herokuapp.com/rest-auth/login/


`{
	"email": "nimo1234@gmail.com",
	"password": "Nimoqwerty"
}`

https://safe-chamber-55286.herokuapp.com/users/list


https://safe-chamber-55286.herokuapp.com/wallet/create


`{
    
        "balance": "230.00",
        "account_name": "BOKBank",
        "account_number": "3213567",
        "bank": "DepositBankAccount",
        "phone_number": "0700000000",
        "password": "MOnalisa",
        "user": 39
    
}`


https://safe-chamber-55286.herokuapp.com/wallet/deposit

`{
    "deposit_amount":"10" ,
    "wallet": "92032560-4d12-4e46-b205-e8690f623ec9"

}`


https://safe-chamber-55286.herokuapp.com/wallet/withdraw

`{
    "amount_withdraw": "5.00",
    "wallet": "92032560-4d12-4e46-b205-e8690f623ec9"
}`


https://safe-chamber-55286.herokuapp.com/wallet/transfer

`{
    "amount": "20.00",
    "sender_wallet": "92032560-4d12-4e46-b205-e8690f623ec9",
    "receiver_user": 37
}`

## DEVELOPMENT

clone the project

`git clone https://github.com/naiyoma/MLFA_API.git`


#### Make virtual environment
`sudo apt-get install python3-venv`
`python3 -m venv env`
`source env/bin/activate`

#### Install requirements
`pip install -r requirements.txt`

#### cd malakoff_api
`python3 manage.py runserver`

### API ENDPOINTS


#### User Management

`user registration payload` ==> `http://127.0.0.1:8000/rest-auth/registration/`


`{
    "email": "tinahuang@gmail.com",
    "password1": "KindaTina",
    "password2": "KindaTina"
}`

`user login payload` ==> `http://127.0.0.1:8000/rest-auth/login/`

`{
	"email": "nimo1234@gmail.com",
	"password": "Nimoqwerty"
}`

`user list payload` ==> `http://127.0.0.1:8000/users/list`

List all created users

#### Wallet Management

`create a wallet ` ==> `http://127.0.0.1:8000/wallet/create`

`{
    
        "balance": "230.00",
        "account_name": "BOKBank",
        "account_number": "3213567",
        "bank": "DepositBankAccount",
        "phone_number": "0700000000",
        "password": "MOnalisa",
        "user": 39
    
}`


`wallet deposit` => `http://127.0.0.1:8000/wallet/deposit`

`{
    "deposit_amount":"10" ,
    "wallet": "92032560-4d12-4e46-b205-e8690f623ec9"

}`

`withdraw wallet` => `http://127.0.0.1:8000/wallet/withdraw`

`{
    "amount_withdraw": "5.00",
    "wallet": "92032560-4d12-4e46-b205-e8690f623ec9"
}`

`transfer to user` => `http://127.0.0.1:8000/wallet/transfer`

`{
    "amount": "20.00",
    "sender_wallet": "92032560-4d12-4e46-b205-e8690f623ec9",
    "receiver_user": 37
}`


