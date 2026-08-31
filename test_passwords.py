import pytest
from passwords import *
from genarete import *


def test_add_password():
    assert add_password({"website":"github.com","username":"brain","password" : "12345678"}) == {"github.com": {"username":"brain","password" : "12345678"}}
    assert add_password({"website":"google.com","username":"zAck0","password" : "gg53dsd3"}) == {"google.com":{"username":"zAck0","password" : "gg53dsd3"}}
    assert add_password({"website":"meta.com","username":"Gran","password" : "Gran5.t54"}) == {"meta.com":{"username":"Gran","password" : "Gran5.t54"}}
    assert add_password({"website":"news.com","username":"Liam","password" : "zxcvbb"}) == {"news.com":{"username":"Liam","password" : "zxcvbb"}}
    
    
def test_search_password():
    assert search_password({},{"website":"github.com"} ) == {}
    assert search_password({"google.com":{"username":"zAck0","password" : "gg53dsd3"},
                            "github.com": {"username":"brain","password" : "12345678"},
                            "meta.com":{"username":"Gran","password" : "Gran5.t54"},
                            "news.com":{"username":"Liam","password" : "zxcvbb"}},{"website":"github.com"} ) == {"github.com": {"username":"brain","password" : "12345678"}}
    
    assert search_password({"google.com":{"username":"zAck0","password" : "gg53dsd3"},
                                "github.com": {"username":"brain","password" : "12345678"},
                                "meta.com":{"username":"Gran","password" : "Gran5.t54"},
                                "news.com":{"username":"Liam","password" : "zxcvbb"}},{"website":"gog.com"} ) == {}
    
    

def test_delete_password():
    assert delete_password({"google.com":{"username":"zAck0","password" : "gg53dsd3"},
                                "github.com": {"username":"brain","password" : "12345678"},
                                "meta.com":{"username":"Gran","password" : "Gran5.t54"},
                                "news.com":{"username":"Liam","password" : "zxcvbb"}},{"website":"github.com"} ) == {"google.com":{"username":"zAck0","password" : "gg53dsd3"},"meta.com":{"username":"Gran","password" : "Gran5.t54"},"news.com":{"username":"Liam","password" : "zxcvbb"}}
    
    assert delete_password({"google.com":{"username":"zAck0","password" : "gg53dsd3"},
                                "github.com": {"username":"brain","password" : "12345678"},
                                "meta.com":{"username":"Gran","password" : "Gran5.t54"},
                                "news.com":{"username":"Liam","password" : "zxcvbb"}},{"website":"steam.com"}) == {"google.com":{"username":"zAck0","password" : "gg53dsd3"},
                                                                                                                    "github.com": {"username":"brain","password" : "12345678"},
                                                                                                                    "meta.com":{"username":"Gran","password" : "Gran5.t54"},
                                                                                                                    "news.com":{"username":"Liam","password" : "zxcvbb"}}
                                
def test_genarete():
    random.seed(1)
    assert genarete_password({"password length" : "13"}) == """r+iGp"58@WAm!"""