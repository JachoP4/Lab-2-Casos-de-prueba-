import ecommerce_form
import log_conf
import pytest

@pytest.fixture
def system():
    return ecommerce_form.OnlinePurchase()

@pytest.mark.unit
@pytest.mark.parametrize('quantity, expected', [(3, True), (-5, False), (0.67, False)])
def test_validate_quantity(system, quantity, expected):
    result = system.validate_quantity(quantity)
    assert result == expected

@pytest.mark.unit
@pytest.mark.parametrize('coupon, expected', [('DISCOUNT10', True), ('DISCOUNT20', True), ('DISCOUNT30', False)])
def test_validate_coupon(system, coupon, expected):
    result = system.validate_coupon(coupon)
    assert result == expected

@pytest.mark.system
def test_RF1_item_invalid(system): # Checamos que el numero de items sea valido.
    log_conf.logging.info('TEST CASE 1: RF1 (NEGATIVE)')
    
    #system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'Laptop': 0,
        'Mouse': 2
    }
    
    coupon = 'DISCOUNT10'
    
    address = 'Avenida Montevideo'
    
    result = system.process_purchase(cart, coupon, address)
    
    log_conf.logging.info(f'The purchase result is: {result}')
    
    assert 'greater than 0' in result

@pytest.mark.system
def test_RF3_invalid_coupon(): # Checamos el cupon.
    log_conf.logging.info('TEST CASE 1: RF3 (NEGATIVE)')

    system = ecommerce_form.OnlinePurchase()
        
    cart = {
        'Laptop': 1,
        'Mouse': 2
    }
        
    coupon = 'DISCOUNT50' # Ni siquiera es valido.
        
    address = 'Avenida Montevideo'
        
    result = system.process_purchase(cart, coupon, address)
        
    log_conf.logging.info(f'The purchase result is: {result}')
        
    assert 'Discount code in not valid' in result

@pytest.mark.system
def test_RF9_check_discuont(): # Checamos el cupon.
    log_conf.logging.info('TEST CASE 1: RF9 (POSITIVE)')

    system = ecommerce_form.OnlinePurchase()
        
    cart = {
        'Laptop': 1, # $1000
        'Mouse': 2 # 50
    }
        
    coupon = 'DISCOUNT10'
        
    address = 'Avenida Montevideo'
        
    result = system.process_purchase(cart, coupon, address)
        
    log_conf.logging.info(f'The purchase result is: {result}')
        
    assert '990' in result

if __name__ == "__main__":
    log_conf.logging.info('START')
    test_RF1_item_invalid()
    test_RF3_invalid_coupon() # Invalidazo
    test_RF9_check_discuont() # Invalidazo