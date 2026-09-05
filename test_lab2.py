import ecommerce_form
import log_conf

def test_RF1_item_invalid(): # Checamos que el numero de items sea valido.
    log_conf.logging.info('TEST CASE 1: RF1 (NEGATIVE)')
    
    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'Laptop': 0,
        'Mouse': 2
    }
    
    coupon = 'DISCOUNT10'
    
    address = 'Avenida Montevideo'
    
    result = system.process_purchase(cart, coupon, address)
    
    log_conf.logging.info(f'The purchase result is: {result}')
    
    assert 'greater than 0' in result

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
    test_RF3_invalid_coupon() # Invalisdazo
    test_RF9_check_discuont() # Invalidazo