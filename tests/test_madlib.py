from madlib_cli.madlib import read_template, parse, merge

def test_read_func():
    expected = open('../assets/template.txt','r').read()
    received = read_template()
    assert expected == received

def test_parse_func():
    expected = ["first name","adjective"]
    received = parse("my name is {first name} and I am {adjective}")
    assert expected == received

def test_merge_func():
    inputs = ['mais', '23', 'python']
    words_lis = ['name', 'age', 'language']
    text = 'my name is %s and my age is %s I love %s'
    received = merge(text, inputs,words_lis)
    expected = 'my name is mais and my age is 23 I love python'
    assert expected == received