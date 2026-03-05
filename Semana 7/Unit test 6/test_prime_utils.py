from prime_utils import filter_prime, show_primes

def test_filter_prime_true():
    assert filter_prime(2) is True
    assert filter_prime(3) is True
    assert filter_prime(13) is True

def test_filter_prime_false():
    assert filter_prime(0) is False
    assert filter_prime(1) is False
    assert filter_prime(-5) is False
    assert filter_prime(10) is False

def test_show_prime_mixed_list():
    numbers=[1,2,3,4,5,10,11]
    result=show_primes(numbers)
    assert result==[2,3,5,11]
    