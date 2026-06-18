from flask import request, jsonify
from service import app
from service.models import AccountService

@app.route('/accounts', methods=['GET'])
def list_accounts():
    accounts = AccountService.list_all()
    return jsonify([{
        'id': a.id,
        'name': a.name,
        'email': a.email,
        'phone': a.phone
    } for a in accounts])

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    account = AccountService.create(
        data.get('name'),
        data.get('email'),
        data.get('phone')
    )
    return jsonify({
        'id': account.id,
        'name': account.name,
        'email': account.email,
        'phone': account.phone
    }), 201

@app.route('/accounts/<int:account_id>', methods=['GET'])
def read_account(account_id):
    account = AccountService.read(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return jsonify({
        'id': account.id,
        'name': account.name,
        'email': account.email,
        'phone': account.phone
    })

@app.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.get_json()
    account = AccountService.update(
        account_id,
        data.get('name'),
        data.get('email'),
        data.get('phone')
    )
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return jsonify({
        'id': account.id,
        'name': account.name,
        'email': account.email,
        'phone': account.phone
    })

@app.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = AccountService.delete(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    return '', 204
